import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df :pd.DataFrame= pd.read_csv("dest-avg.csv")

# Filter the DataFrame to only include rows where expertise is 'unexp'
df = df[df['expertise'] == ' exp']

# Select only rows with the same 'shared' value (e.g. 0 or 1)
shared_value = 6 # replace with the desired shared value
df = df[df['shared'] == shared_value]

# Create a scatter plot with makespan on the x-axis and risk on the y-axis
fig, ax = plt.subplots()

# Assign a color to each point based on the strategy column
strategy_colors = {
    " Planner": "blue",
    " RiskAssessmentPlanner": "green",
    " MakespanPlanner": "red",
    " RiskPlanner": "yellow",
}
colors = [strategy_colors[strategy] for strategy in df["strategy"]]

# Encode the size of each point based on the time column
sizes = df["time"] / 1000  # convert milliseconds to seconds
ax.scatter(df["makespan"], df["risk"], c=colors, s=sizes)

# Add a log scale to the y-axis
ax.set_yscale('log')


# Add a legend to the plot
handles = [
    plt.plot([], [], marker="o", ls="", color=color, label=strategy)[0]
    for strategy, color in strategy_colors.items()
]
ax.legend(handles=handles, title="Strategy")

# Label the axes and add a title
ax.set_xlabel("Makespan")
ax.set_ylabel("Risk")
ax.set_title("Tradeoff Between Risk and Makespan by Strategy")

plt.savefig("test-avg")  # display the plot
