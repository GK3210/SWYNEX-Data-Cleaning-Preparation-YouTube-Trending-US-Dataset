# SWYNEX – Data Cleaning & Preparation (Task 1)

Cleaning of a public dataset – **YouTube Trending Videos (US)**, Kaggle *Trending YouTube Video Statistics* – using **Python (pandas)** for the SWYNEX Technologies Data Analytics internship.

## Repository structure
```
data/raw/youtube_trending_us_raw.csv        original file (unchanged)
data/cleaned/youtube_trending_us_cleaned.csv  cleaned dataset
data/cleaned/youtube_trending_us_cleaned.xlsx cleaned dataset + Cleaning_Log sheet (Excel)
reports/cleaning_log.csv                    every change with row counts
reports/removed_duplicates.csv              the 50 rows that were deleted
reports/before_after_summary.json           before / after profile
src/clean_data.py                           reproducible cleaning script
```
Run it with `python src/clean_data.py` (needs `pandas`, `numpy`, `openpyxl`).

## Dataset summary
| | Before | After |
|---|---|---|
| Rows | 40,949 | 40,899 |
| Columns | 23 | 25 (2 flag columns added) |
| Exact duplicate rows | 48 | 0 |
| Missing cells | 0 (hidden as fake zeros) | 1,478 (true missing, now explicit) |

Each row is one video on one trending day, so a `video_id` appearing on many dates is **expected** and was kept.

## Issues found and what was changed
| # | Issue | Action | Records |
|---|---|---|---|
| 1 | Exact duplicate rows | Removed (first kept) | 48 |
| 2 | Same video + same trending date, slightly different counters | Kept the row with highest views | 2 |
| 3 | Wrong data types: `publish_time` and `trending_date` were text; flags / small ints used wide types | Converted to datetime (UTC), date, boolean, compact ints | all rows |
| 4 | Repeated / extra spaces in titles | Collapsed to single spaces; `title_length` and `title_caps_ratio` recalculated | 588 |
| 5 | Inconsistent channel names (`marshmello` vs `Marshmello`, `QUARTZ` vs `Quartz`, `chris lee`, Pokémon channel) | Standardised to the most frequent spelling | 31 |
| 6 | `ratings_disabled = True` but `likes`, `dislikes`, `like_ratio`, `dislike_ratio`, `like_dislike_ratio` held fake `0` / `1.0` | Set to missing | 169 |
| 7 | `comments_disabled = True` but `comment_count = 0` | Set to missing | 632 |
| 8 | `like_dislike_ratio = 1.0` with 0 likes and 0 dislikes | Set to missing | 1 |
| 9 | Videos trending > 365 days after upload (max 4,214 days) | **Kept**, flagged in `days_to_trend_outlier` | 237 |
| 10 | `video_id` shared by different channels / upload times | **Kept**, flagged in `video_id_conflict` | 97 |

## Checks run after cleaning
- No exact duplicates and no duplicate (`video_id`, `trending_date`) pairs
- Likes never exceed views; `title_length` matches the title text
- Each `category_id` maps to exactly one `category_name` (16 categories)
- `publish_hour` / `publish_day` agree with `publish_time`; `days_to_trend` is never negative

## Notes and assumptions
- `publish_time` is in **UTC**. `trending_date` has no time part, so for 120 videos published later on the trending day, `days_to_trend` is 0 (kept as in the source).
- Large view counts (max 225M) are real viral videos, so no outliers were removed.
- Constant column `country` (= US) was kept for traceability.
- Missing values in items 6–8 should be excluded, not treated as 0, when averaging likes, comments or ratios.
