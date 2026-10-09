# SWYNEX Final Data Analytics Project
### What drives reach and engagement on YouTube's US Trending list?

**An end-to-end analytics case study: data cleaning → exploratory analysis → interactive dashboard → business insights.** Built with Python (pandas, matplotlib, seaborn) and an HTML/JavaScript dashboard during the Data Analytics internship at **SWYNEX Technologies**.

![Dashboard overview](screenshots/dashboard_overview.png)

*The interactive dashboard: 6 KPI cards, filters, annotated charts and a key-findings panel (open `dashboard/index.html` in any browser).*

---

## Project at a glance
| | |
|---|---|
| **Dataset** | YouTube Trending Videos (US), 14 Nov 2017 to 14 Jun 2018 |
| **Data size** | 40,949 raw rows → **40,899 clean rows** · 6,351 videos · 2,203 channels · 16 categories |
| **Data cleaning** | 10 issues found and fixed or flagged, including hidden fake zeros |
| **Analysis** | 11 report-ready charts · 7 insights · 3 types of anomalies |
| **Dashboard** | 6 KPI cards · 4 interactive filters · 3 annotated charts |
| **Business output** | 9 insights with recommended actions |
| **Tools** | Python (pandas, NumPy, matplotlib, seaborn) · openpyxl · HTML/CSS/JavaScript |
| **Author** | Gautam Kurpatwar · Data Analytics Intern, SWYNEX Technologies |

## Table of contents
1. [Problem statement](#1-problem-statement)
2. [Dataset information](#2-dataset-information)
3. [Project workflow](#3-project-workflow)
4. [Data cleaning process](#4-data-cleaning-process)
5. [Exploratory data analysis](#5-exploratory-data-analysis)
6. [Interactive dashboard](#6-interactive-dashboard)
7. [Key business insights and recommendations](#7-key-business-insights-and-recommendations)
8. [Limitations](#8-limitations)
9. [Conclusion](#9-conclusion)
10. [Repository structure](#10-repository-structure)
11. [How to reproduce](#11-how-to-reproduce)
12. [Skills demonstrated](#12-skills-demonstrated)
13. [Author](#author)

## Quick links
| What | Where |
|---|---|
| Cleaned dataset | `data/youtube_trending_us_cleaned.csv` |
| Cleaning script and log | [`src/clean_data.py`](src/clean_data.py) · `reports/cleaning/cleaning_log.csv` |
| Analysis script | [`src/eda.py`](src/eda.py) |
| Written report (16 pages) | [`docs/SWYNEX_EDA_Report.pdf`](docs/SWYNEX_EDA_Report.pdf) |
| All charts in one PDF | [`reports/EDA_Figures_Report.pdf`](reports/EDA_Figures_Report.pdf) |
| Summary tables (Excel) | `reports/EDA_summary_tables.xlsx` |
| Interactive dashboard | [`dashboard/index.html`](dashboard/index.html) |
| Data dictionary | [`docs/data_dictionary.md`](docs/data_dictionary.md) |

---

## 1. Problem statement
**Business scenario:** a content or marketing team wants to place videos on YouTube. They need to know **what a typical trending video looks like, which categories and publishing times perform best, and whether the trending list itself behaves consistently over time**. Without clean data and clear evidence, they risk benchmarking against misleading averages and planning content for the wrong categories or times.

**Questions this project answers**
1. What does a typical trending video look like, and how variable is it?
2. Which categories, channels and publishing times are associated with more reach and engagement?
3. How has the trending list changed over time?
4. Which records are unusual, and why do they matter?

## 2. Dataset information
| Item | Detail |
|---|---|
| **Source** | US file of the Kaggle dataset *Trending YouTube Video Statistics* (please check its licence on Kaggle before reusing) |
| **Granularity** | One row = one video on one trending day. A video appears once for each day it stayed on the list (about 200 videos per day) |
| **Period** | 14 Nov 2017 to 14 Jun 2018 (205 trending days) |
| **Raw file** | `data/raw/youtube_trending_us_raw.csv` · 40,949 rows · 23 columns |
| **Cleaned file** | `data/youtube_trending_us_cleaned.csv` · 40,899 rows · 25 columns (+ Excel copy) |
| **Key columns** | views, likes, dislikes, comment_count, category_name, channel_title, publish_time, trending_date, days_to_trend, tag_count, title_length |

Full column descriptions are in the [data dictionary](docs/data_dictionary.md).

## 3. Project workflow
```
 Raw data ──► 1. Cleaning ──► Clean data ──► 2. Analysis ──► 3. Dashboard ──► 4. Business insights
 (40,949)     clean_data.py    (40,899)       eda.py          index.html       recommendations
                                              11 charts       6 KPIs + filters
```

## 4. Data cleaning process
The raw file looked tidy, but it hid real problems. Every change is logged in `reports/cleaning/cleaning_log.csv`.

| # | Issue found | Action | Records |
|---|---|---|---|
| 1 | Exact duplicate rows | Removed (first kept) | 48 |
| 2 | Same video on the same date with different counters | Kept the row with the most views | 2 |
| 3 | Dates stored as text; wide data types | Converted to datetime, date, boolean and compact integer types | all |
| 4 | Extra spaces inside titles | Collapsed; `title_length` and `title_caps_ratio` recalculated | 588 |
| 5 | Same channel with different capitalisation (e.g. `marshmello` / `Marshmello`) | Standardised to the most common spelling | 31 |
| 6 | **Hidden missing values:** likes, dislikes and ratios stored as fake `0` / `1.0` when ratings are disabled | Set to missing | 169 |
| 7 | **Hidden missing values:** comment count `0` when comments are disabled | Set to missing | 632 |
| 8 | Like/dislike ratio `1.0` with 0 likes and 0 dislikes | Set to missing | 1 |
| 9 | Videos that trended more than 365 days after upload | Kept, flagged (`days_to_trend_outlier`) | 237 |
| 10 | `video_id` shared by different channels or upload times | Kept, flagged (`video_id_conflict`) | 97 |

| Before vs after | Raw | Clean |
|---|---|---|
| Rows | 40,949 | **40,899** |
| Columns | 23 | 25 (2 flag columns added) |
| Exact duplicate rows | 48 | **0** |
| Missing cells | 0 (hidden as fake zeros) | 1,478 (true missing, now explicit) |

The 50 removed rows are saved in `reports/cleaning/removed_duplicates.csv`.

## 5. Exploratory data analysis
**Typical values (medians, because the data is heavily skewed):** 680,977 views · 18,247 likes · 1,912 comments · 4.8 days from upload to trending · 19 tags.

| Metric | Median | Mean | Maximum |
|---|---|---|---|
| Views | 680,977 | 2,360,649 | 225,211,923 |
| Likes | 18,247 | 74,579 | 5,613,827 |
| Comments | 1,912 | 8,581 | 1,361,580 |
| Days from upload to trending | 4.8 | 16.2 | 4,214.6 |

### Insight 1: Views are extremely skewed, so use medians
The mean (2.36M) is **3.5× the median (681K)**, and 4,498 rows (11%) are statistical outliers. The top video, *Childish Gambino – This Is America*, has 225M views.
![Figure 1](charts/01_views_distribution.png)

### Insight 2: Entertainment has the volume, but Music, Gaming and Film earn the reach
Entertainment is 24.3% of rows, but Gaming (1.49M), Music (1.43M) and Film & Animation (1.27M) have about **2× its median views** (734K).
![Figure 2](charts/02_category_volume_vs_views.png)

### Insight 3: News and Sports get fewer likes and a shorter life on the list
Median like ratio: **0.85%** for News & Politics and **1.08%** for Sports, against 4.31% for Howto & Style. They also stay on the list the shortest (about 4.9 and 4.8 days vs 8.1 for Music).
![Figure 3](charts/03_category_engagement_and_lifespan.png)

### Insight 4: Publishing time matters, and weekend uploads earn more
32.7% of videos were published between 14:00 and 17:00 UTC (about 9am to 12pm US Eastern), with the busiest cells on Tuesday to Thursday. Weekends are only **17.7%** of rows (28.6% if evenly spread) yet have a higher median view count (**752K vs 662K**).
![Figure 4](charts/04_publish_time_heatmap.png)
![Figure 5](charts/05_weekday_volume_vs_views.png)

### Insight 5: The trending list changed around March 2018
Median days from upload to trending rose from **3.3 to 10.9**, median views rose from about 320K to 2.0M, and new videos entering the list fell from about **44 to 12 per day**. A change in how YouTube builds the list is plausible, but the data cannot prove it (June covers 14 days).
![Figure 6](charts/06_monthly_trend_shift.png)

### Insight 6: Engagement metrics rise together; tags and title length barely matter
Views correlate with likes (0.87) and comments (0.83), but only 0.08 with tag count and −0.07 with title length. Shorter titles do show a higher like ratio (3.73% for up to 30 characters vs 1.80% for 71 to 100), and videos with 21 to 30 tags have a higher median than untagged ones (850K vs 494K). These are associations, not proof of cause.
![Figure 7](charts/07_correlation_heatmap.png)
![Figure 8](charts/08_title_and_tag_effects.png)

### Insight 7: Views roughly double while a video stays on the list
For the 3,981 videos that stayed five or more days, the median video had **2.0×** its first-day views on its last day. The median stay is 6 days, 1,209 videos lasted 10+ days, and the longest lasted 29.
![Figure 11](charts/11_views_growth_during_trending.png)

### Top channels
The most frequent channels are late-night shows, sports and media brands (ESPN: 202 video-days across 84 videos). The top 10 channels account for only **4.6%** of rows, so the list is spread across 2,203 channels.
![Figure 9](charts/09_top_channels.png)

### Anomalies
- **237** videos trended more than a year after upload (one after about 11.5 years, a Budweiser ad).
- **67** videos with 100K+ views have more dislikes than likes, often political. *YouTube Rewind 2017* reached 1.64M dislikes.
- Comments are disabled most often in News & Politics and Nonprofits & Activism (about 7% of video-days).

![Figure 10](charts/10_anomalies.png)

*The full written report with every chart explained is in [`docs/SWYNEX_EDA_Report.pdf`](docs/SWYNEX_EDA_Report.pdf).*

## 6. Interactive dashboard
[`dashboard/index.html`](dashboard/index.html) is a single self-contained page (no installation, works offline). Download the repository and open it in any browser.

| Feature | Details |
|---|---|
| **6 KPI cards** | Video-days · total views · average views · overall like ratio · average comments · % trending within 3 days |
| **Filters** | Category · From month · To month · bar-chart metric · click-a-bar drill-down · Reset |
| **Charts** | Category comparison · monthly trend with the March 2018 shift annotated · median views by publish day |
| **Key findings panel** | Five headline findings plus a definitions footer |

**1. Filter by category and period:** Music, March to June 2018. All KPIs and the trend update instantly.
![Music, Mar to Jun 2018](screenshots/dashboard_filtered_music_mar-jun.png)

**2. Change the bar-chart metric:** overall like ratio by category.
![Like ratio by category](screenshots/dashboard_like_ratio_by_category.png)

**3. Click a bar to drill into one category:** News & Politics, all months.
![News & Politics](screenshots/dashboard_news_politics.png)

> **Note on like ratio:** the dashboard shows the *overall* like ratio (total likes ÷ total views); the insights above use the *median per-video* ratio. The two rank categories differently. By median per video, News & Politics (0.85%) and Sports (1.08%) are lowest; by overall ratio, Autos & Vehicles (0.82%) and News & Politics (1.23%) are lowest.

## 7. Key business insights and recommendations
| # | Insight | What it means | Recommended action |
|---|---|---|---|
| 1 | Typical views (681K) are far below the average (2.36M) | Averages are inflated by a few viral hits | Set targets and benchmarks with **medians**, not averages |
| 2 | Gaming, Music and Film & Animation have about 2× Entertainment's median views, while Entertainment is the most crowded category | Reach and crowding are different things | Prioritise high-reach categories in planning; Gaming has only 816 rows, so test before committing |
| 3 | News & Politics and Sports have the lowest median like ratios and the shortest stay on the list | Attention is real but short-lived | Plan these as **rapid-response** content, not evergreen |
| 4 | Weekend uploads are 17.7% of trending rows but have higher median views | Less competition may help (association, not proof) | **A/B test weekend publishing** against the weekday peak window |
| 5 | After March 2018 videos took 10.9 days to trend instead of 3.3, and fewer new videos entered daily | The list became harder to enter and favoured slower-building videos | Analyse **before and after March 2018 separately** |
| 6 | Tags and title length barely relate to views; shorter titles have a higher like ratio | Metadata tricks do not drive reach | Focus on content quality; keep titles concise |
| 7 | Views about double during a video's stay | The trending list sustains exposure | Prepare follow-up content and calls to action for the trending window |
| 8 | 67 videos have more dislikes than likes | Controversy can reach the list too | Monitor the like/dislike balance as a **brand-risk signal** |
| 9 | Disabled ratings and comments were stored as zeros | Averages were biased downwards | Treat disabled metrics as **missing**, not zero, in all reporting |

## 8. Limitations
- Only videos that **reached the trending list** are included, so results do not describe YouTube overall.
- Views, likes and comments are **cumulative snapshots** on each trending day, not daily values.
- US data only, Nov 2017 to Jun 2018; June is a partial month. The data is historical, so recommendations should be re-tested on current data.
- Correlations and group differences are **associations, not proof of cause**.
- Small groups (for example Shows: 4 videos; Nonprofits & Activism: 14 videos) should be read with caution.

## 9. Conclusion
Trending performance is a long tail of moderate videos plus a few viral hits, so decisions should be based on medians. Category, publishing day and the period of the list all matter, and the list itself changed in March 2018. Cleaning the data first, by exposing hidden zeros and removing duplicates, was essential to getting trustworthy numbers.

## 10. Repository structure
```
README.md                         this case study
requirements.txt                  Python packages
data/
  raw/youtube_trending_us_raw.csv                original dataset
  youtube_trending_us_cleaned.csv                cleaned dataset (and .xlsx copy)
src/
  clean_data.py                   Step 1: cleaning
  eda.py                          Step 2: exploratory analysis and charts
charts/                           11 report-ready figures (PNG)
reports/
  cleaning/                       cleaning log, removed duplicates, before/after summary
  *.csv, EDA_summary_tables.xlsx, EDA_Figures_Report.pdf    analysis tables
dashboard/
  index.html                      interactive dashboard
screenshots/                      4 dashboard screenshots (used in this README)
  (see top-level screenshots/ folder)
docs/
  SWYNEX_EDA_Report.pdf / .docx   16-page written report
  data_dictionary.md              column descriptions
```

## 11. How to reproduce
```bash
git clone https://github.com/GK3210/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
python src/clean_data.py    # raw data     -> cleaned data + cleaning log
python src/eda.py           # cleaned data -> charts and summary tables
# then open dashboard/index.html in a browser
```
Both scripts were run from scratch on the raw file and reproduce the cleaned dataset and all analysis numbers.

## 12. Skills demonstrated
`Data cleaning and validation` · `Exploratory data analysis` · `Statistical thinking (medians, Spearman correlation, IQR outliers)` · `Data visualisation` · `Dashboard design` · `Business storytelling` · `Documentation and reproducible workflows`

## Author
**Gautam Kurpatwar**
GitHub: [GK3210](https://github.com/GK3210) · LinkedIn: [Gautam Kurpatwar](https://www.linkedin.com/in/gautam-kurpatwar-98268138a)

Completed as part of the Data Analytics internship at **SWYNEX Technologies** (Tasks 1 to 4: Data Cleaning · Exploratory Analysis · Interactive Dashboard · Final Project).

`#SWYNEX` `#Internship` `#DataAnalytics` `#CaseStudy` `#Python` `#Dashboard`
