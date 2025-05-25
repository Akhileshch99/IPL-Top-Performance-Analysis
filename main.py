# 📦 Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 🔧 Settings
sns.set(style='darkgrid')
%matplotlib inline


# Load the deliveries dataset
df = pd.read_csv("deliveries.csv")
# Display basic info
print("Shape of dataset:", df.shape)
df.head()


# Check for missing values
print(df.isnull().sum())
# Drop rows with missing values (if any)
df.dropna(inplace=True)


# Add a new column for boundary type
df['boundary_type'] = df['batsman_runs'].apply(lambda x: 'Four' if x == 4 else ('Six' if x == 6 else 'Other'))
# Total runs per batsman
top_batsmen = df.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
# Total wickets per bowler
df['is_wicket'] = df['dismissal_kind'].notnull()
top_bowlers = df[df['is_wicket']].groupby('bowler')['is_wicket'].count().sort_values(ascending=False).head(10)


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


print("Total Unique Matches:", df['match_id'].nunique())
print("Total Unique Batsmen:", df['batsman'].nunique())
print("Total Unique Bowlers:", df['bowler'].nunique())
# Average runs per ball
avg_run_per_ball = df['total_runs'].mean()
print("Average runs per ball:", round(avg_run_per_ball, 2))


# Check outliers in runs per delivery
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['total_runs'])
plt.title("Distribution of Total Runs per Delivery")
plt.show()

