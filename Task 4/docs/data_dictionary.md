# Data Dictionary – `youtube_trending_us_cleaned.csv`

Source: Kaggle "Trending YouTube Video Statistics" (US file), cleaned in SWYNEX Task 1. One row = one video on one trending day.

| Column | Type | Description |
|---|---|---|
| video_id | text | YouTube video identifier (11 characters) |
| title | text | Video title (extra spaces removed in Task 1) |
| channel_title | text | Channel name (capitalisation standardised) |
| category_id | integer | YouTube category code |
| category_name | text | Category label (16 categories) |
| country | text | Always `US` |
| publish_time | datetime (UTC) | When the video was published |
| trending_date | date | Day the video appeared on the trending list |
| publish_hour | integer | Hour of `publish_time` (0–23, UTC) |
| publish_day | text | Weekday of `publish_time` |
| days_to_trend | decimal | Days from publishing to the trending date (0 when published later on the trending date) |
| views | integer | Cumulative views on the trending date |
| likes | integer | Cumulative likes (blank when ratings are disabled) |
| dislikes | integer | Cumulative dislikes (blank when ratings are disabled) |
| comment_count | integer | Number of comments (blank when comments are disabled) |
| like_ratio | decimal | likes ÷ views |
| dislike_ratio | decimal | dislikes ÷ views |
| like_dislike_ratio | decimal | likes ÷ (likes + dislikes) |
| title_length | integer | Number of characters in the title |
| title_caps_ratio | decimal | Uppercase letters ÷ letters in the title |
| tag_count | integer | Number of tags (0 = no tags) |
| comments_disabled | boolean | True if comments are turned off |
| ratings_disabled | boolean | True if likes/dislikes are hidden |
| days_to_trend_outlier | boolean | Flag added in Task 1: trended more than 365 days after upload |
| video_id_conflict | boolean | Flag added in Task 1: the same video_id appears with different channels or upload times |
