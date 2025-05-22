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

# ✅ CODE
## 📦 Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

## 🔧 Settings
sns.set(style='darkgrid')
%matplotlib inline

📥 Step 1: Load the Dataset
# Load the deliveries dataset
df = pd.read_csv("deliveries.csv")

# Display basic info
print("Shape of dataset:", df.shape)
df.head()

🧹 Step 2: Data Cleaning
# Check for missing values
print(df.isnull().sum())

# Drop rows with missing values (if any)
df.dropna(inplace=True)

🔎 Step 3: Feature Engineering
# Add a new column for boundary type
df['boundary_type'] = df['batsman_runs'].apply(lambda x: 'Four' if x == 4 else ('Six' if x == 6 else 'Other'))

# Total runs per batsman
top_batsmen = df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

# Total wickets per bowler
df['is_wicket'] = df['dismissal_kind'].notnull()
top_bowlers = df[df['is_wicket']].groupby('bowler')['is_wicket'].count().sort_values(ascending=False).head(10)

📊 Step 4: Static Visualizations with Matplotlib & Seaborn
# Top 10 Batsmen
plt.figure(figsize=(10, 6))
sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette='rocket')
plt.title("Top 10 Batsmen by Runs")
plt.xlabel("Runs")
plt.ylabel("Batsman")
plt.show()

# Top 10 Bowlers
plt.figure(figsize=(10, 6))
sns.barplot(x=top_bowlers.values, y=top_bowlers.index, palette='mako')
plt.title("Top 10 Bowlers by Wickets")
plt.xlabel("Wickets")
plt.ylabel("Bowler")
plt.show()

📈 Step 5: Interactive Visuals with Plotly
# Interactive plot for top batsmen
fig = px.bar(
    x=top_batsmen.values, 
    y=top_batsmen.index, 
    orientation='h', 
    labels={'x': 'Runs', 'y': 'Batsman'},
    title='Top 10 Batsmen (Interactive)'
)
fig.update_layout(yaxis={'categoryorder':'total ascending'})
fig.show()

🧠 Step 6: Summary Statistics
print("Total Unique Matches:", df['match_id'].nunique())
print("Total Unique Batsmen:", df['batsman'].nunique())
print("Total Unique Bowlers:", df['bowler'].nunique())

# Average runs per ball
avg_run_per_ball = df['total_runs'].mean()
print("Average runs per ball:", round(avg_run_per_ball, 2))

🧼 Step 7: Handling Outliers
# Check outliers in runs per delivery
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['total_runs'])
plt.title("Distribution of Total Runs per Delivery")
plt.show()


