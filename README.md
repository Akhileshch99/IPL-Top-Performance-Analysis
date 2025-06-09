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



## IPL Top Performance Analysis : Visualization
This project presents insightful visualizations of top performances in the Indian Premier League (IPL). The visualizations are designed to uncover trends, top players, and standout statistics using clean and aesthetic charts with optional interactivity.
🎯 Objective
The goal of this project is to:
•	Identify and showcase top performances across various IPL metrics.
•	Use appropriate visualizations to tell a meaningful story behind the data.
•	Present clear, well-structured, and interactive charts where applicable.
________________________________________
📊 Visualizations Included
1.	Top Run Scorers (Bar Chart)
Displays the highest run scorers in the league using a horizontal bar chart for easy comparison.
2.	Top Wicket Takers (Bar Chart)
Highlights bowlers with the most wickets using vertical bars.
3.	Strike Rate vs Average (Scatter Plot)
Shows batting performance with strike rate on the x-axis and average on the y-axis, helping identify explosive and consistent batters.
4.	Matches Played vs Total Runs (Bubble Plot)
Visualizes correlation between experience and run accumulation, with bubble size indicating total sixes.
5.	Most Sixes by a Batter (Bar Chart)
Highlights the power hitters of the tournament.
6.	Dismissal Types (Pie Chart)
Breaks down the various ways players have been dismissed.
________________________________________
🎨 Aesthetics & Clarity
•	Used Seaborn and Matplotlib for consistent styling and better readability.
•	Labels, titles, and legends are added to all plots.
•	Color palettes were selected for clarity and to reduce visual fatigue.
________________________________________
🧩 Interactivity (Optional)
•	Interactive versions of visualizations using Plotly (if available).
•	Tooltips enabled on interactive plots to display player-specific stats.
•	Filters (e.g., by year, team) can be optionally implemented for better exploration.
________________________________________
📁 Project Structure
plaintext
CopyEdit
📁 IPL-Top-Performance-Analysis/
├── data/
│   └── IPL Dataset.csv
├── visuals/
│   ├── top_run_scorers.png
│   ├── top_wicket_takers.png
│   └── ... (other plots)
├── interactive/
│   └── (plotly versions if any)
├── src/
│   └── ipl_visualizations.py
└── README.md
________________________________________
🧠 Interpretation & Insights
•	Virat Kohli emerges as the top run scorer, consistently contributing across seasons.
•	Lasith Malinga dominates in wickets, especially in death overs.
•	The strike rate vs average scatter highlights players like AB de Villiers who are both aggressive and reliable.
•	The dismissal types pie chart shows that the majority of players are out caught, reflecting modern T20 strategies.
________________________________________
🚀 How to Run
1.	Clone the repository:
bash
git clone https://github.com/Akhileshch99/IPL-Top-Performance-Analysis.git
cd IPL-Top-Performance-Analysis
2.	Install required Python libraries:
bash
pip install pandas matplotlib seaborn
3.	Run the visualization script:
bash
python src/ipl_visualizations.py
________________________________________
✅ Validation
•	Cross-checked player stats with ESPNcricinfo IPL data.
•	Ensured proper axis scaling, label correctness, and chart integrity.




