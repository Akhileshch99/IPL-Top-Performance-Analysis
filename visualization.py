import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("IPL Dataset.csv")

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# 1. Top Run Scorers – Horizontal Bar Chart
top_batters = df.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
plt.figure()
sns.barplot(x=top_batters.values, y=top_batters.index, palette="Blues_d")
plt.title("Top 10 Run Scorers in IPL")
plt.xlabel("Total Runs")
plt.ylabel("Batter")
plt.tight_layout()
plt.show()


# 2. Most Wickets Taken – Vertical Bar Chart
wickets_df = df[(df["is_wicket"] == 1) & (~df["dismissal_kind"].isin(["run out", "retired hurt", "obstructing the field"]))]
top_bowlers = wickets_df["bowler"].value_counts().head(10)
plt.figure()
sns.barplot(x=top_bowlers.index, y=top_bowlers.values, palette="Set2")
plt.title("Top 10 Wicket Takers in IPL")
plt.xlabel("Bowler")
plt.ylabel("Wickets Taken")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. Player Performance Over Seasons – Line Chart
# Simulate 'season' info from match_id if not available
df['season'] = df['match_id'].astype(str).str[:4]  # adjust this based on real season data
season_runs = df.groupby(['season', 'batter'])['batsman_runs'].sum().reset_index()
top_3_batters = season_runs.groupby('batter')['batsman_runs'].sum().nlargest(3).index
plt.figure()
for batter in top_3_batters:
    data = season_runs[season_runs['batter'] == batter]
    plt.plot(data['season'], data['batsman_runs'], label=batter, marker='o')
plt.title("Top Player Performance Over Seasons")
plt.xlabel("Season")
plt.ylabel("Runs Scored")
plt.legend()
plt.tight_layout()
plt.show()


# 4. Strike Rate vs Average – Scatter Plot
balls_faced = df.groupby('batter').size()
runs_scored = df.groupby('batter')['batsman_runs'].sum()
dismissals = df[df['player_dismissed'].notna()]['player_dismissed'].value_counts()

batters_df = pd.DataFrame({
    'Runs': runs_scored,
    'Balls': balls_faced,
    'Dismissals': dismissals
}).dropna()

batters_df['Strike Rate'] = (batters_df['Runs'] / batters_df['Balls']) * 100
batters_df['Average'] = batters_df['Runs'] / batters_df['Dismissals']

plt.figure()
sns.scatterplot(data=batters_df, x='Average', y='Strike Rate', size='Runs', legend=False, alpha=0.6)
plt.title("Strike Rate vs Batting Average")
plt.xlabel("Batting Average")
plt.ylabel("Strike Rate")
plt.tight_layout()
plt.show()


# 5. Matches Played Per Team Per Year – Stacked Bar Chart
matches = df[['match_id', 'batting_team']]
matches = matches.drop_duplicates()
matches['season'] = matches['match_id'].astype(str).str[:4]
match_counts = matches.groupby(['season', 'batting_team']).size().unstack().fillna(0)

match_counts.plot(kind='bar', stacked=True, colormap='tab20', figsize=(14, 7))
plt.title("Matches Played Per Team Per Year")
plt.xlabel("Season")
plt.ylabel("Matches")
plt.tight_layout()
plt.show()


# 6. Win Percentages of Teams – Pie Chart
# This data requires a match-winner column which may not be present in your dataset
# If it exists:
# win_df = pd.read_csv("matches.csv")  # load match-level dataset if available
# win_counts = win_df["winner"].value_counts()
# pie = win_counts.plot.pie(autopct='%1.1f%%', figsize=(8, 8), title="Win Percentages of Teams")

# Temporary placeholder if 'winner' column not available:
print("⚠️ Pie chart for team win percentages requires match-level data with 'winner' column.")


# 7. Venues With Highest Total Scores – Column Chart
venue_scores = df.groupby(['match_id', 'venue'])['total_runs'].sum().reset_index()
top_venues = venue_scores.groupby('venue')['total_runs'].mean().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_venues.index, y=top_venues.values, palette="coolwarm")
plt.title("Top 10 Highest Scoring Venues")
plt.xlabel("Venue")
plt.ylabel("Average Match Total")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
