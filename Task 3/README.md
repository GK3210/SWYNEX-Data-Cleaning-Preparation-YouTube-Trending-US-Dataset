# SWYNEX – Interactive Dashboard (Task 3)

An interactive dashboard that communicates the main findings from the **YouTube Trending Videos (US)** analysis completed in Tasks 1 and 2. It is a single, self-contained web page (HTML, CSS and JavaScript) that opens in any browser, works offline and needs no installation.

## Dashboard preview
![Dashboard overview](screenshots/dashboard_overview.png)
*Default view: all categories, Nov 2017 to Jun 2018.*

---

## Objective
Build a professional dashboard from the analysed dataset, with **KPIs, charts and useful filters**, that clearly communicates the main findings (Task 3 of the SWYNEX Data Analytics internship).

## Dashboard features

### Filters
| Filter | What it does |
|---|---|
| **Category** | Shows one of the 16 YouTube categories, or all |
| **From month / To month** | Limits the period (Nov 2017 to Jun 2018) |
| **Bar chart metric** | Switches the category chart between average views, video-days and like ratio |
| **Click a bar** | Clicking a category in the bar chart applies it as the Category filter |
| **Reset filters** | Returns to the full dataset |

### KPI cards
| KPI | Definition |
|---|---|
| Video-days | Number of rows: one video on one trending day |
| Total views | Sum of views across the selected rows (cumulative snapshots) |
| Avg views / video-day | Mean views per row (skewed by viral videos) |
| Overall like ratio | Total likes ÷ total views, for rows where ratings are enabled |
| Avg comments | Mean comment count per row, for rows where comments are enabled |
| Trending in 3 days | Share of rows published up to 3 days before trending |

### Charts
| Chart | Responds to filters? | Purpose |
|---|---|---|
| Category bar chart | Month range (and highlights the selected category) | Compare reach, volume and engagement by category |
| Monthly trend line | Yes | Shows the shift in average views, annotated at **March 2018** |
| Median views by publish day | No (full data) | Shows weekend uploads earn higher median views |
| Key findings panel | No (full data) | Five headline findings from the Task 2 analysis |

## Main findings communicated
1. **Views are heavily skewed:** the mean (2.36M) is 3.5 times the median (681K).
2. **Entertainment has the most volume (24.3%)**, but Gaming, Music and Film & Animation earn about twice its median views.
3. **News & Politics (0.85%) and Sports (1.1%)** have the lowest *median per-video* like ratios.
4. **Weekend uploads** are only 17.7% of trending rows but have higher median views (752K vs 662K).
5. **The trending list changed around March 2018:** median days to trend rose from 3.3 to 10.9, and new videos entering the list per day fell from about 44 to 12.

## Interactive views (screenshots)

**1. Filter by category and period:** Music, March to June 2018. All six KPI cards and the monthly trend update instantly.

![Music, Mar to Jun 2018](screenshots/dashboard_filtered_music_mar-jun.png)

**2. Change the bar chart metric:** overall like ratio by category, showing engagement instead of reach.

![Like ratio by category](screenshots/dashboard_like_ratio_by_category.png)

**3. Click a bar to drill into one category:** News & Politics, all months.

![News & Politics](screenshots/dashboard_news_politics.png)

> **Note on like ratio:** the dashboard KPI and bar chart show the *overall* like ratio (total likes ÷ total views). The finding quoted above uses the *median per-video* like ratio from the Task 2 analysis. The two measures rank categories differently: by median per video, News & Politics (0.85%) and Sports (1.08%) are lowest; by overall ratio, Autos & Vehicles (0.82%) and News & Politics (1.23%) are lowest, and Sports is 2.24%.

## How to use
1. Download or clone the repository and open `index.html` in a browser.
2. Pick a category and a month range, or click a bar in the category chart.
3. Read the KPI cards and charts, which update instantly.
4. Click **Reset filters** to go back to the full view.

## Repository structure
```
README.md
index.html                                          the dashboard
screenshots/                                        4 dashboard screenshots used in this README
data/youtube_trending_us_cleaned.csv                cleaned dataset from Task 1 (source data)
```

## Publish it with GitHub Pages (optional)
Repository **Settings → Pages →** deploy from the `main` branch, root folder. GitHub will give you a link to the live dashboard.

## How it was built
- **Source:** the cleaned dataset from Task 1 (40,899 rows, 6,351 videos, 16 categories, 14 Nov 2017 to 14 Jun 2018).
- **Preparation:** the data was aggregated by category and month (video-days, views, likes, comments and videos trending within 3 days) in Python (pandas) and embedded in `index.html`, so the page loads instantly and works offline.
- **Visuals:** hand-built SVG charts with JavaScript; no external libraries or internet connection are required.
- **Design:** bordered panels, labelled axes, data labels, definitions footer, and light and dark mode support.

## Validation
Dashboard figures were checked against the source CSV. For example, **Music from March to June 2018** shows 3,369 video-days, 32.18B total views and 9.55M average views per video-day, matching the dataset. The page was also tested in a headless browser with no errors.

## Notes and limitations
- Averages are means and are pulled up by viral videos; medians are in the Task 2 report.
- Likes and comments are blank when ratings or comments are disabled, so those rows are excluded from like ratio and average comments.
- Views are cumulative snapshots on each trending day, not daily views.
- Only videos that reached the trending list are included, so the results do not describe YouTube overall.
- US data only; June 2018 covers 14 days.
- Built as an HTML dashboard rather than in Power BI or Tableau, which the task allows ("another suitable BI tool").

## Related tasks
- Task 1: Data Cleaning and Preparation
- Task 2: Exploratory Data Analysis

## Author
**Gautam Kurpatwar** · GitHub: [GK3210](https://github.com/GK3210) · LinkedIn: [Gautam Kurpatwar](https://www.linkedin.com/in/gautam-kurpatwar-98268138a)

Completed as part of the Data Analytics internship at **SWYNEX Technologies**.

#SWYNEX #Internship #DataAnalytics #Dashboard #Python
