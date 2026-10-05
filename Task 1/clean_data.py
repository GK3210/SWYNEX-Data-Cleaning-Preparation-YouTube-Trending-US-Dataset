"""
SWYNEX Task 1 - Data Cleaning & Preparation
Dataset : YouTube Trending Videos (US), Kaggle "Trending YouTube Video Statistics"
Run     : python src/clean_data.py   (from the repository root)
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw/youtube_trending_us_raw.csv"
OUT_CSV = ROOT / "data/cleaned/youtube_trending_us_cleaned.csv"
OUT_XLSX = ROOT / "data/cleaned/youtube_trending_us_cleaned.xlsx"
REPORTS = ROOT / "reports"

log = []  # (step, issue, action, rows_or_cells_affected)


def record(step, issue, action, n):
    log.append({"step": step, "issue": issue, "action": action, "records_affected": int(n)})
    print(f"[{step}] {issue} -> {action}: {n}")


df = pd.read_csv(RAW, dtype={"video_id": "string"})
rows_in = len(df)
profile_before = {
    "rows": rows_in,
    "columns": df.shape[1],
    "missing_cells": int(df.isna().sum().sum()),
    "exact_duplicates": int(df.duplicated().sum()),
}

# ---------------------------------------------------------------- 1. Duplicates
exact = df.duplicated(keep="first")
df[exact].to_csv(REPORTS / "removed_duplicates.csv", index=False)
record(1, "Exact duplicate rows (all 23 columns identical)", "Removed, first occurrence kept", exact.sum())
df = df[~exact].copy()

# Same video listed twice on the same trending date with slightly different counters
# (two snapshots of the same video) -> keep the snapshot with the highest view count.
key = ["video_id", "trending_date"]
snap = df.duplicated(key, keep=False)
df = df.sort_values(key + ["views"], ascending=[True, True, False])
dup_snap = df.duplicated(key, keep="first")
pd.concat([pd.read_csv(REPORTS / "removed_duplicates.csv"), df[dup_snap]]).to_csv(
    REPORTS / "removed_duplicates.csv", index=False)
record(2, "Same video_id + trending_date with different counters (snapshot duplicates)",
       "Removed, row with highest views kept", dup_snap.sum())
df = df[~dup_snap].copy()

# ---------------------------------------------------------------- 2. Data types
df["publish_time"] = pd.to_datetime(df["publish_time"], utc=True).dt.tz_localize(None)  # UTC, naive
df["trending_date"] = pd.to_datetime(df["trending_date"]).dt.date
for c in ["video_id", "title", "channel_title", "category_name", "country", "publish_day"]:
    df[c] = df[c].astype("string")
df["category_id"] = df["category_id"].astype("int16")
df["publish_hour"] = df["publish_hour"].astype("int8")
df["tag_count"] = df["tag_count"].astype("int16")
df["title_length"] = df["title_length"].astype("int16")
for c in ["comments_disabled", "ratings_disabled"]:
    df[c] = df[c].astype(bool)
record(3, "publish_time / trending_date stored as text; ints & flags with wide dtypes",
       "Converted to datetime (UTC), date, compact int and boolean types", 2)

# ---------------------------------------------------------------- 3. Inconsistent text
# 3a. whitespace in titles
bad_ws = df["title"].str.contains(r"\s{2,}", regex=True) | (df["title"] != df["title"].str.strip())
df["title"] = df["title"].str.replace(r"\s+", " ", regex=True).str.strip()
df["title_length"] = df["title"].str.len().astype("int16")


def caps_ratio(s):
    a = [ch for ch in s if ch.isalpha()]
    return round(sum(ch.isupper() for ch in a) / len(a), 6) if a else 0.0


df.loc[bad_ws, "title_caps_ratio"] = df.loc[bad_ws, "title"].map(caps_ratio)
record(4, "Repeated / leading / trailing spaces inside titles",
       "Collapsed to single spaces; title_length & title_caps_ratio recalculated", bad_ws.sum())

# 3b. channel names that differ only by letter-case
lower = df["channel_title"].str.lower()
canon = df.groupby(lower)["channel_title"].agg(lambda s: s.value_counts().idxmax())
new_names = lower.map(canon)
changed = df["channel_title"] != new_names
df["channel_title"] = new_names
record(5, "Same channel written with different capitalisation (e.g. 'marshmello' / 'Marshmello')",
       "Standardised to the most frequent spelling", changed.sum())

# ---------------------------------------------------------------- 4. Hidden missing values
# When ratings / comments are disabled the source stores 0 (and ratio 0 / 1.0) as a placeholder.
rd = df["ratings_disabled"]
for c in ["likes", "dislikes"]:
    df[c] = df[c].astype("Int64")
    df.loc[rd, c] = pd.NA
for c in ["like_ratio", "dislike_ratio", "like_dislike_ratio"]:
    df.loc[rd, c] = np.nan
record(6, "ratings_disabled = True but likes/dislikes/ratios filled with fake 0 / 1.0",
       "Set to missing (NaN) so averages are not distorted", rd.sum())

cd = df["comments_disabled"]
df["comment_count"] = df["comment_count"].astype("Int64")
df.loc[cd, "comment_count"] = pd.NA
record(7, "comments_disabled = True but comment_count filled with 0",
       "Set to missing (NaN)", cd.sum())

zero_ld = (~rd) & ((df["likes"].fillna(0) + df["dislikes"].fillna(0)) == 0)
df.loc[zero_ld, "like_dislike_ratio"] = np.nan
record(8, "like_dislike_ratio = 1.0 although likes + dislikes = 0 (undefined ratio)",
       "Set to missing (NaN)", zero_ld.sum())

# ---------------------------------------------------------------- 5. Flags (kept, not deleted)
df["days_to_trend"] = df["days_to_trend"].round(1)
df["days_to_trend_outlier"] = df["days_to_trend"] > 365
record(9, "Videos that trended > 365 days after upload (old videos revived)",
       "Kept; flagged in new column days_to_trend_outlier", df["days_to_trend_outlier"].sum())

n_ch = df.groupby("video_id")[["channel_title", "publish_time"]].nunique()
conflict_ids = n_ch[(n_ch > 1).any(axis=1)].index
df["video_id_conflict"] = df["video_id"].isin(conflict_ids)
record(10, "video_id shared by different channels / upload times (ID collision)",
       "Kept; flagged in new column video_id_conflict", df["video_id_conflict"].sum())

# ---------------------------------------------------------------- 6. Validation
assert not df.duplicated().any()
assert not df.duplicated(key).any()
assert (df["likes"].dropna() <= df["views"][df["likes"].notna()]).all()
assert (df["title_length"] == df["title"].str.len()).all()
assert df["category_id"].groupby(df["category_name"]).nunique().max() == 1
assert (df["days_to_trend"] >= 0).all()

df = df.sort_values(["trending_date", "video_id"]).reset_index(drop=True)
profile_after = {
    "rows": len(df),
    "columns": df.shape[1],
    "missing_cells": int(df.isna().sum().sum()),
    "exact_duplicates": int(df.duplicated().sum()),
}

# ---------------------------------------------------------------- 7. Export
df.to_csv(OUT_CSV, index=False, encoding="utf-8")
pd.DataFrame(log).to_csv(REPORTS / "cleaning_log.csv", index=False)
json.dump({"before": profile_before, "after": profile_after},
          open(REPORTS / "before_after_summary.json", "w"), indent=2)

with pd.ExcelWriter(OUT_XLSX, engine="openpyxl", datetime_format="yyyy-mm-dd hh:mm:ss",
                    date_format="yyyy-mm-dd") as xw:
    df.to_excel(xw, sheet_name="Cleaned_Data", index=False)
    pd.DataFrame(log).to_excel(xw, sheet_name="Cleaning_Log", index=False)
    from openpyxl.styles import Font, PatternFill
    from openpyxl.utils import get_column_letter
    for ws in xw.book.worksheets:
        for cell in ws[1]:
            cell.font = Font(name="Arial", bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="1F3864")
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for i, col in enumerate(ws.iter_cols(min_row=1, max_row=200), 1):
            w = max(len(str(c.value)) if c.value is not None else 0 for c in col)
            ws.column_dimensions[get_column_letter(i)].width = min(max(w + 2, 11), 60)

print("\nBEFORE", profile_before, "\nAFTER ", profile_after)
