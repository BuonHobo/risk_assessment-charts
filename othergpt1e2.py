import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dest-avg.csv')

def visualize_data(df):
    # Create a FacetGrid to visualize multiple graphs in a grid
    g = sns.FacetGrid(df, col="strategy", row="expertise", margin_titles=True)

    # Plot makespan vs risk in a scatter plot
    g.map_dataframe(sns.scatterplot, x="makespan", y="risk", hue="shared", palette="deep", alpha=0.8)

    # Customize the axes labels
    g.set_axis_labels("Makespan", "Risk (log)")

    # Set the y-axis to logarithmic scale
    g.set(yscale="log")

    # Add a legend
    g.add_legend()

    # Show the plot
    plt.savefig('test1-avg')

def visualize_time(df):
    # Create a box plot for time taken by each strategy, grouped by expertise
    sns.boxplot(x="strategy", y="time", hue="expertise", data=df)

    # Customize the axes labels
    plt.xlabel("Strategy")
    plt.ylabel("Time (ms)")

    # Add a legend
    plt.legend(title="Expertise")

    # Show the plot
    plt.savefig('test2-avg')

visualize_data(df)
#visualize_time(df)