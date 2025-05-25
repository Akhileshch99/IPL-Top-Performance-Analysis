# IPL Top Performance Analysis

## 📊 Project Overview

**IPL Top Performance Analysis** is a data analytics project aimed at identifying and visualizing the top-performing players and teams in the Indian Premier League (IPL). By analyzing historical data from past IPL seasons, this project uncovers insights into batting and bowling performances, team trends, and match-winning factors using Python-based data visualization tools.

---

## 🎯 Objectives

- Analyze batting and bowling statistics across all IPL seasons.
- Identify top players based on runs, wickets, strike rate, economy, etc.
- Evaluate team performance trends and win ratios.
- Visualize key patterns in performance using interactive charts.
- Provide a comprehensive view of individual and team contributions.

---

## 🗂️ Dataset

The analysis uses publicly available IPL datasets, which typically include:

- **`matches.csv`** – Match-level information like teams, venue, result, toss, etc.
- **`deliveries.csv`** – Ball-by-ball delivery data, including batsman, bowler, runs, and dismissals.

> Source: [IPL Dataset]()

---

## 🔧 Tools & Technologies

- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computations
- **Matplotlib / Seaborn** – Static visualizations
- **Plotly** – Interactive charts
- **Jupyter Notebook / VS Code** – Development environment

---

## 📌 Key Analyses

### 🔹 Batting Analysis
- Top run-scorers of all time and by season
- Highest strike rate and average (min innings)
- Most 50s/100s and match-winning knocks

### 🔹 Bowling Analysis
- Top wicket-takers overall and per season
- Best economy and strike rate (min overs bowled)
- Most 4-wicket and 5-wicket hauls

### 🔹 Team Performance
- Wins and losses over the seasons
- Toss decision impact
- Home vs. away performance

### 🔹 Trend Analysis
- Performance trajectory of players
- Emerging talents vs. consistent performers
- Season-wise statistical comparison

---

## 📈 Visualizations

The project includes various charts such as:
- Bar charts for top players
- Line plots for season trends
- Pie charts for dismissal types
- Heatmaps for team matchups

---

## 🧹 Data Preprocessing

Steps taken:
### 1. Cleaning
- Removed/filled missing values (e.g., umpire names, null results).
- Ensured correct data types (dates, integers, categories).

### 2. Feature Engineering
- **Batting**: Strike Rate, Average, Boundary %, Match Impact Score.
- **Bowling**: Economy Rate, Dot Ball %, Wicket Impact Index.
- **Team**: Win % by venue, toss-decision patterns.

### 3. Data Consistency
- Merged datasets on match IDs with verified row counts.
- Handled duplicate player/team name entries (e.g., "Delhi Daredevils" vs "Delhi Capitals").
---

## 📁 Project Structure

ipl-top-performance-analysis/
│
├── data/
│ ├── matches.csv
│ └── deliveries.csv
│
├── notebooks/
│ └── ipl_analysis.ipynb
│
├── images/
│ └── charts_and_graphs.png
│
├── README.md
└── requirements.txt


---

## ▶️ How to Run

1. Clone the repository  
   `git clone https://github.com/Akhileshch99/IPL-Top-Performance-Analysis.git`

2. Install dependencies  
   `pip install -r requirements.txt`

3. Run the Jupyter notebook  
   `jupyter notebook notebooks/ipl_analysis.ipynb`

---

## ✅ Future Improvements

- Add predictive modeling (e.g., player performance prediction)
- Build a web dashboard using Streamlit or Dash
- Incorporate more granular data (e.g., player injuries, venue stats)


