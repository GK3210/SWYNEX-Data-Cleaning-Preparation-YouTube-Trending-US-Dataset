SWYNEX Technologies – Data Analytics Internship Projects

A portfolio of the tasks I completed during my Data Analytics internship at SWYNEX Technologies. The tasks build on each other: clean a raw dataset, explore it for insights, then present the results. All work uses one public dataset, YouTube Trending Videos (US) (Kaggle, "Trending YouTube Video Statistics").

Author: Gautam Kurpatwar | GitHub: GK3210 | LinkedIn: (https://www.linkedin.com/in/gautam-kurpatwar-98268138a/)

Task overview
#	Task	Tools	Status	Folder
1	Data Cleaning & Preparation	Python (pandas)	✅ Completed	Task-1-Data-Cleaning
2	Exploratory Data Analysis	Python (pandas, matplotlib, seaborn)	✅ Completed	Task-2-EDA
3	Interactive Dashboard	to be decided	⏳ Upcoming	–
4	Final Data Analytics Project	to be decided	⏳ Upcoming	–

Each task folder has its own README with full details, code and outputs.

Task 1 – Data Cleaning & Preparation

Goal: identify missing values, duplicates, wrong data types and inconsistent values, and produce a clean dataset.

	Before	After
Rows	40,949	40,899
Columns	23	25 (2 flag columns added)
Exact duplicate rows	48	0

Main fixes

Removed 50 duplicate records (48 exact, 2 same-video snapshots).
Converted publish_time and trending_date from text to proper date types.
Collapsed extra spaces in 588 titles and standardised 31 inconsistent channel names.
Found hidden missing values: likes, dislikes and ratios held fake 0/1.0 for 169 rows with ratings disabled, and comment counts held 0 for 632 rows with comments disabled. These were set to true missing values so averages are not distorted.
Flagged, but kept, 237 old-video outliers and 97 video-ID conflicts.

Deliverables: cleaned CSV and Excel file, reproducible script, change log and a removed-records file.

Task 2 – Exploratory Data Analysis

Goal: calculate key statistics, find trends, patterns and anomalies, and explain at least five insights with charts.

Key insights

Views are extremely skewed. Mean 2.36M vs median 681K; 11% of rows are outliers.
Entertainment has the most volume (24.3%), but Music, Gaming and Film & Animation earn about twice its median views.
News & Sports get the lowest like ratios (0.85% and 1.1%) and the shortest time on the trending list.
Weekend uploads are only 17.7% of rows yet have higher median views (752K vs 662K).
The trending list changed around March 2018: median days to trend rose from 3.3 to 10.9, and new videos per day fell from about 44 to 12.
Views, likes and comments rise together (correlation 0.83 to 0.87); tags and title length barely matter.
Views roughly double while a video stays on the list.

Anomalies: 237 old videos revived (one after about 11.5 years) and 67 controversial videos with more dislikes than likes.

Deliverables: 11 report-ready charts, summary tables, a 16-page written report (PDF and Word), data dictionary and analysis script.

Repository structure
SWYNEX-Data-Analytics-Internship/
├── README.md                         this file
├── Task-1-Data-Cleaning/
│   ├── README.md
│   ├── src/clean_data.py
│   ├── data/raw/                     original dataset
│   ├── data/cleaned/                 cleaned CSV and Excel
│   └── reports/                      cleaning log, removed duplicates, before/after summary
└── Task-2-EDA/
    ├── README.md
    ├── requirements.txt
    ├── src/eda.py
    ├── data/                         cleaned dataset from Task 1
    ├── charts/                       11 figures (PNG)
    ├── reports/                      summary tables, Excel workbook, combined figures PDF
    └── docs/                         written report (PDF, DOCX) and data dictionary
Tech stack
Area	Tools
Language	Python 3
Data handling	pandas, NumPy
Visualisation	matplotlib, seaborn
Excel output	openpyxl
Documentation	Markdown, Word/PDF report
How to run
bash
git clone https://github.com/GK3210/<repo-name>.git
cd <repo-name>
pip install -r Task-2-EDA/requirements.txt

# Task 1: cleaning
cd Task-1-Data-Cleaning && python src/clean_data.py && cd ..

# Task 2: exploratory analysis
cd Task-2-EDA && python src/eda.py

Both scripts read their input from the data/ folder and write results to data/cleaned/, charts/ and reports/. Task 2 includes the cleaned data, so it can run on its own.

Skills demonstrated
Data cleaning: duplicates, data types, text standardisation and hidden missing values
Exploratory analysis: descriptive statistics, grouping, time trends, correlation and outlier detection
Data visualisation: clear, labelled and reproducible charts
Documentation: READMEs, data dictionary, change logs and a written analytical report
Reproducible work: every result can be regenerated from the scripts
Limitations
Only videos that reached the trending list are included, so results do not describe YouTube overall.
Views and likes are cumulative snapshots on each trending day.
Data covers the US from 14 Nov 2017 to 14 Jun 2018 (June is partial).
Group differences and correlations are associations, not proof of cause.
Data source

Kaggle: Trending YouTube Video Statistics (US file). Please check the dataset's licence on Kaggle before reusing it.

Acknowledgements

Thanks to SWYNEX Technologies for the internship tasks and guidance.

#SWYNEX #Internship #DataAnalytics #Python #EDA #DataCleaning
