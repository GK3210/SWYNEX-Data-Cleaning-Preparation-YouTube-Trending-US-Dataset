<div align="center">

# 📊 YouTube Trending Videos (US) — Data Cleaning, Preparation & Exploratory Analysis

**A data analytics portfolio project | SWYNEX Technologies — Data Analyst Internship, Task 1**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Project-Completed-success)](#)
[![Dataset](https://img.shields.io/badge/Dataset-US%20YouTube%20Trending-red?logo=youtube&logoColor=white)](https://www.kaggle.com/datasets/datasnaek/youtube-new)

**Goal:** Turn historical YouTube Trending data into a clean, analysis-ready dataset and communicate meaningful findings through visual analysis.

</div>

---

## 📌 Project Overview

This project explores the US YouTube Trending Videos dataset for the period **14 November 2017 to 14 June 2018**. It combines data preparation with exploratory data analysis (EDA) to examine video reach, category performance, audience engagement, publishing time, channel presence, and unusual records.

The analysis shown in this repository uses **40,899 video-day records representing 6,351 unique videos**. A video-day is one observation of a video on a particular trending-list day; it is not the same as a unique video.

The work is designed to demonstrate a practical analyst workflow:

1. Inspect and understand the raw data.
2. Clean and standardize fields for consistent analysis.
3. Validate dates, metrics, and derived fields.
4. Engineer useful measures such as title length, tag count, engagement ratios, and days from upload to trending.
5. Explore patterns and anomalies with Python visualizations.
6. Translate charts into findings and cautious, actionable recommendations.

> **Scope note:** The figures below describe historical data from 2017–2018. They should not be interpreted as current YouTube platform behaviour. Observed relationships are associations, not proof of causation.

## 🎯 Business Questions

- Which categories appear most frequently on the trending list?
- Which categories have the highest typical view counts per video-day?
- How do likes, dislikes, comments, and views move together?
- Does publishing day or hour appear related to trending-list presence?
- Did typical views, time-to-trend, or daily new entries change over the study period?
- Are title length and tag count strongly associated with video performance?
- Which records look unusual and may deserve a closer quality review?

## 🧰 Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data loading, cleaning, transformation, and aggregation |
| NumPy | Numerical operations and derived metrics |
| Matplotlib / Seaborn | Statistical charts and visual exploration |
| Jupyter Notebook / Python scripts | Reproducible analysis workflow |
| Git & GitHub | Version control and project documentation |

## 🗂️ Repository Structure

```text
SWYNEX-Data-Cleaning-Preparation-YouTube-Trending-US-Dataset/
├── Task 1/                         # Data cleaning and preparation deliverables
├── Task 2/                         # Additional task materials
├── Task 3/                         # Additional task materials
├── Task 4/                         # Additional task materials
├── assets/
│   └── figures/
│       ├── 01_views_distribution.png
│       ├── 02_category_volume_vs_views.png
│       ├── 03_category_engagement_and_lifespan.png
│       ├── 04_publish_time_heatmap.png
│       ├── 05_weekday_volume_vs_views.png
│       ├── 06_monthly_trend_shift.png
│       ├── 07_correlation_heatmap.png
│       ├── 08_title_and_tag_effects.png
│       ├── 09_top_channels.png
│       ├── 10_anomalies.png
│       └── 11_views_growth_during_trending.png
└── README.md
```

*The folder names above reflect the task-based organization of the repository. Keep or adjust them to match the actual files committed to your branch. The `assets/figures/` folder contains the visualizations embedded in this README.*

## 📊 Dataset

**Source:** [YouTube Trending Video Dataset — US (Kaggle)](https://www.kaggle.com/datasets/datasnaek/youtube-new)

The historical dataset includes video metadata, channel and category information, publication timestamps, trending dates, and available engagement metrics. The analysis uses the cleaned dataset and derived fields prepared for the project.

### Key fields used in the analysis

| Field / measure | Description |
|---|---|
| `video_id` | Identifier for a video |
| `title` | Video title |
| `channel_title` | Channel name |
| `category_name` | Human-readable video category |
| `publish_time` | Timestamp when the video was published |
| `trending_date` | Date of the trending-list observation |
| `views` | Recorded view count for that observation |
| `likes`, `dislikes`, `comment_count` | Available engagement counts |
| `publish_hour`, `publish_day` | Derived publication-time fields |
| `days_to_trend` | Elapsed time between publishing and trending |
| `title_length`, `title_caps_ratio`, `tag_count` | Derived title and tag characteristics |
| `like_ratio`, `dislike_ratio` | Engagement counts relative to views, where valid |
| `comments_disabled`, `ratings_disabled` | Indicators for unavailable interaction features |

**Important:** Engagement metrics can be unavailable or disabled for some records. Ratios should be calculated only when the denominator and source metric are valid; zero or missing values should not automatically be interpreted as genuine audience behaviour.

## 🧹 Data Preparation Workflow

The project workflow focuses on making the data consistent and suitable for analysis.

1. **Load and inspect** — review row and column counts, column names, data types, missing values, and summary statistics.
2. **Check data quality** — investigate missing or invalid values, duplicate observations, and unexpected metric values.
3. **Standardize fields** — normalize text and category labels where appropriate, and ensure column names and data types are consistent.
4. **Validate dates** — parse publication and trending dates and check the relationship between them.
5. **Create analytical features** — derive publication day/hour, elapsed time to trending, title length, capitalization ratio, tag count, and engagement ratios.
6. **Handle edge cases carefully** — preserve the distinction between a true zero, a missing value, and an interaction metric disabled by YouTube.
7. **Validate outputs** — review record counts, data types, duplicate keys, value ranges, and the consistency of calculated fields.
8. **Analyze and visualize** — aggregate records by category, day, month, channel, and engagement measures.

The exact cleaning decisions should be documented alongside the relevant notebook or script so that the transformation can be reproduced.

## 🔎 Exploratory Data Analysis & Key Findings

### 1. View counts are highly right-skewed

![Distribution of views and category-level view ranges]
- The mean views per video-day (**about 2.36 million**) is much higher than the median (**about 681 thousand**), showing that a relatively small number of very high-view records pull the mean upward.
- The chart flags approximately **11%** of records above the IQR-based upper outlier threshold.
- Category distributions also show a wide range of typical performance and extreme observations.

**Analyst takeaway:** Use medians and percentiles alongside averages when comparing video performance. A few viral videos can distort the mean.

### 2. Category volume and category reach are different

![Video-day volume compared with median views by category](assets/figures/02_category_volume_vs_views.png)

- **Entertainment** has the largest number of video-day records in this sample, followed by **Music** and **Howto & Style**.
- **Gaming**, **Music**, and **Film & Animation** have the highest median views per video-day in the displayed comparison.
- A category that appears often is not necessarily the category with the highest typical reach.

**Analyst takeaway:** Report both *volume* (how often a category appears) and *reach* (typical views). They answer different business questions.

### 3. Engagement and time on the trending list vary by category

![Category like ratios and average trending-list duration](assets/figures/03_category_engagement_and_lifespan.png)

- **Howto & Style** has the highest median like ratio in the chart, with **Music** and **Comedy** also relatively high.
- **News & Politics** and **Sports** show lower median like ratios in this sample.
- The **Shows** category has the longest average stay in the displayed chart, but the sample is very small, so that result should be treated cautiously.

**Analyst takeaway:** Views alone do not describe engagement. Compare interaction rates and time on the list, while checking sample sizes and disabled ratings/comments.

### 4. Weekday afternoons are a high-volume publishing window

![Trending video-days by publishing weekday and hour](assets/figures/04_publish_time_heatmap.png)

- Many trending-list observations are associated with videos published during weekday afternoon hours in **UTC**.
- The figure reports that **32.7%** of trending rows were published between **14:00 and 17:00 UTC**.
- The pattern is descriptive: it does not establish that publishing during those hours causes a video to trend.

**Analyst takeaway:** Treat this window as a hypothesis for controlled testing, not a universal upload-time rule. Convert UTC to the target audience's local time before applying it.

### 5. Weekend records are fewer, but median views are higher

![Trending-list volume and median views by publishing weekday](assets/figures/05_weekday_volume_vs_views.png)

- Saturday and Sunday account for fewer video-day observations than weekdays in this dataset.
- The displayed median views are higher for weekend-published videos overall, with Sunday highest in the chart.
- This is an observational comparison and may reflect differences in content, audience, or other factors.

**Analyst takeaway:** Consider weekday and weekend performance separately, and compare similar categories or channels before recommending a publishing schedule.

### 6. The monthly pattern changes noticeably around March 2018

![Monthly changes in views, time to trend, and new entries](assets/figures/06_monthly_trend_shift.png)

- Median views per video-day rise sharply from March 2018 onward in the displayed series.
- Median time from upload to trending also increases during the same period.
- The number of new videos entering the list per day falls substantially from the earlier months.
- June 2018 covers only part of the month, so it is not directly comparable with full months.

**Analyst takeaway:** The change is worth investigating, but the charts alone cannot prove that a change to YouTube's recommendation or trending algorithm caused it. Dataset coverage and other external factors may also contribute.

### 7. Engagement metrics are strongly related to one another

![Spearman rank correlation between numerical variables](assets/figures/07_correlation_heatmap.png)

- Views have strong positive rank correlations with likes (**0.87**), dislikes (**0.86**), and comments (**0.83**) in the chart.
- Likes and comments are also strongly correlated (**0.89**).
- Tag count (**0.08**) and title length (**−0.07**) have near-zero rank correlations with views in this analysis.
- Days to trend has a modest positive relationship with views (**0.33**).

**Analyst takeaway:** Higher-view videos also tend to have more interactions, but correlation does not establish which metric drives another. Some interactions are disabled or unavailable, which affects the usable sample.

### 8. Title length and tag count show limited relationships with views

![Title length and tag count comparisons](assets/figures/08_title_and_tag_effects.png)

- Shorter titles have a higher median like ratio in the displayed grouping.
- Videos with **21–30 tags** have the highest median views among the tag-count groups shown, but the overall rank correlation between tag count and views is very small.
- These group comparisons do not show that changing title length or adding tags will directly improve performance.

**Analyst takeaway:** Treat title and tag choices as testable content hypotheses. Evaluate them within comparable categories, channels, and publishing periods.

### 9. A small group of channels appears repeatedly

![Top channels by days on the trending list](assets/figures/09_top_channels.png)

- ESPN, *The Tonight Show Starring Jimmy Fallon*, Netflix, TheEllenShow, and Vox appear among the channels with the most video-days on the trending list.
- The top ten channels account for only a small share of all records, and the list is spread across many channels.

**Analyst takeaway:** Recurring presence can reflect an established audience, frequent publishing, or multiple videos trending over time. It should not be interpreted as a direct measure of subscriber count or channel quality.

### 10. Anomalies deserve investigation rather than automatic deletion

![Upload-to-trending delays, controversial videos, and disabled comments](assets/figures/10_anomalies.png)

- A small number of observations have very long delays between upload and trending; the chart marks a 365-day reference line.
- Some high-view videos have more dislikes than likes, which may indicate controversial or strongly negative audience reactions.
- Disabled comments are more common in some categories than others in the displayed data.

**Analyst takeaway:** Flag unusual records for review. Some are genuine edge cases—such as older videos that resurface—and should not be removed just because they are statistically extreme.

### 11. Videos that stay trending often gain more views over time

![Growth multiple for videos with five or more trending days](assets/figures/11_views_growth_during_trending.png)

- For videos with five or more trending days, the displayed median ratio of views on the last trending day to views on the first trending day is approximately **2.0×**.
- The analysis includes **3,981 videos** that remained on the list for at least five days.
- The chart caps the ratio at 8× for readability, so values at the cap should not be read as exactly 8×.

**Analyst takeaway:** Longer trending-list presence is associated with view growth in these cumulative snapshots. This does not establish that trending-list duration alone caused the growth.

## 💡 Recommendations

Based on the descriptive findings:

1. **Use robust performance measures.** Report median views, percentiles, and outlier counts alongside averages.
2. **Separate volume from reach.** Compare categories using both trending-list frequency and typical views.
3. **Track engagement quality.** Monitor like ratio and comment activity, while clearly accounting for disabled or missing metrics.
4. **Test publishing windows.** Run controlled comparisons by weekday and hour, using the audience's local time zone.
5. **Segment before drawing conclusions.** Compare videos within similar categories, channels, and time periods.
6. **Investigate structural changes.** Examine the March 2018 shift with additional checks before attributing it to an algorithm change.
7. **Review anomalies with context.** Keep legitimate viral, revived, or controversial videos unless there is a documented data-quality reason to exclude them.
8. **Avoid causal claims from correlations.** Validate content-strategy recommendations through experiments or stronger analytical designs.

## ▶️ How to Use This Repository

1. Clone or download the repository.
2. Open the relevant task folder and locate the notebook or Python script used for data preparation and analysis.
3. Install the dependencies used by that notebook/script.
4. Update file paths if the dataset is stored in a different directory.
5. Run the cleaning and validation steps before generating the analysis.
6. Review the figures and compare the reported statistics with the outputs from your current data.

Example environment setup:

```bash
python -m venv .venv
```

Activate the environment, then install the packages required by your notebook or script. A typical analysis environment may use:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

> The exact execution command depends on the filenames and notebook structure in the task folders. Check those files before running a command.

## 📁 Visualization Gallery

All figures are stored in `assets/figures/` and are embedded above:

| Figure | Topic |
|---|---|
| 01 | View distribution and category-level outliers |
| 02 | Category volume versus median reach |
| 03 | Category engagement and trending-list lifespan |
| 04 | Publishing weekday/hour heatmap |
| 05 | Weekday volume versus median views |
| 06 | Monthly change in views, time-to-trend, and new entries |
| 07 | Correlation heatmap |
| 08 | Title length and tag-count comparisons |
| 09 | Top channels by trending-list presence |
| 10 | Anomaly review |
| 11 | View growth during trending-list presence |

## ⚠️ Limitations

- The dataset covers a historical period and one country (US); findings may not generalize to other markets or today's platform.
- Each video can appear on multiple trending dates, so video-day observations are not independent unique videos.
- View counts are cumulative snapshots and should not be interpreted as daily views without calculating differences between observations.
- Category-level comparisons can be affected by different sample sizes and content mixes.
- Missing or disabled engagement metrics can bias comparisons if treated as zero.
- The analysis is descriptive; it does not prove causation or identify YouTube's internal ranking logic.
- June 2018 covers only part of the month in the displayed monthly analysis.

## 🚀 Possible Future Improvements

- Build an interactive Power BI, Tableau, or Streamlit dashboard.
- Add automated data-quality checks and a reproducible cleaning report.
- Compare categories and channels using confidence intervals or bootstrap estimates.
- Model view growth while accounting for repeated observations of the same video.
- Test publishing-time hypotheses with appropriate controls.
- Add a data dictionary and a formal before/after cleaning summary.
- Create a pipeline that regenerates all figures from the cleaned dataset.

## 👨‍💻 Author

**Gautam Kurpatwar**

Aspiring Data Analyst | Python • Pandas • Excel • SQL • Data Visualization

- **GitHub:** [GK3210](https://github.com/GK3210)
- **Project repository:** [SWYNEX — YouTube Trending US Dataset](https://github.com/GK3210/SWYNEX-Data-Cleaning-Preparation-YouTube-Trending-US-Dataset)

## 🙏 Acknowledgements

- [Kaggle — YouTube Trending Video Dataset (US)](https://www.kaggle.com/datasets/datasnaek/youtube-new)
- SWYNEX Technologies — internship task context
- Python, Pandas, NumPy, Matplotlib, and Seaborn communities

---

<div align="center">

**If you find this project useful, consider giving the repository a ⭐**

</div>
