import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def timetoplan_strategy(data, dest):
    # Create a box plot for time taken by each strategy, grouped by 'shared'
    sns.boxplot(x="strategy", y="time to plan", hue="shared", data=data)

    # Customize the axes labels
    plt.xlabel("Strategy")
    plt.ylabel("Time (ms)")

    plt.xticks(rotation=15)
    # Add a legend
    plt.legend(title="Shared")

    # Show the plot
    plt.savefig(dest)
    plt.close()


def risk_makespan_shared(data, dest):
    # Create a FacetGrid to visualize multiple graphs in a grid
    g = sns.FacetGrid(data, col="shared", row="expertise", margin_titles=True)

    # Plot makespan vs risk in a scatter plot
    g.map_dataframe(sns.scatterplot, x="best makespan", y="average risk", hue="strategy", style="strategy",
                    palette="deep", alpha=0.8)

    # Customize the axes labels
    g.set_axis_labels("Makespan", "Risk (log)")

    # Set the y-axis to logarithmic scale
    g.set(yscale="log")

    # Add a legend
    g.add_legend()

    # Show the plot
    plt.savefig(dest)
    plt.close()


def risk_makespan_strategy(data, dest):
    # Create a FacetGrid to visualize multiple graphs in a grid
    g = sns.FacetGrid(data, col="strategy", row="expertise", margin_titles=True)

    # Plot makespan vs risk in a scatter plot
    g.map_dataframe(sns.scatterplot, x="best makespan", y="average risk", hue="shared", style="shared", palette="deep",
                    alpha=0.8)

    # Customize the axes labels
    g.set_axis_labels("Makespan", "Risk (log)")

    # Set the y-axis to logarithmic scale
    g.set(yscale="log")

    # Add a legend
    g.add_legend()

    # Show the plot
    plt.savefig(dest)
    plt.close()


def task_strategy(data, dest):
    # Filter data for shared=6 and group by strategy
    df_grouped = data[data['shared'] == 6].groupby(['strategy']).sum()

    # Create new dataframe with columns for each kind of cube
    df_plot = pd.DataFrame({
        'Robot Foam': df_grouped['robot foam'],
        'Human Foam': df_grouped['human foam'],
        'Robot Wood': df_grouped['robot wood'],
        'Human Wood': df_grouped['human wood'],
        'Robot Metal': df_grouped['robot metal'],
        'Human Metal': df_grouped['human metal']
    })

    # Set width of bars and positions of x-tick labels
    width = 0.25
    pos = np.arange(len(df_plot.index))

    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot the stacked bar chart for each kind of cube
    ax.bar(pos, df_plot['Robot Foam'], width, label='Robot Foam', color='blue')
    ax.bar(pos, df_plot['Human Foam'], width, bottom=df_plot['Robot Foam'], label='Human Foam', color='grey')
    ax.bar(pos + width, df_plot['Robot Wood'], width, label='Robot Wood', color='orange')
    ax.bar(pos + width, df_plot['Human Wood'], width, bottom=df_plot['Robot Wood'], label='Human Wood', color='grey')
    ax.bar(pos + 2 * width, df_plot['Robot Metal'], width, label='Robot Metal', color='green')
    ax.bar(pos + 2 * width, df_plot['Human Metal'], width, bottom=df_plot['Robot Metal'], label='Human Metal',
           color='grey')

    # Set the x-tick labels and add legend
    ax.set_xticks(pos + width)
    ax.set_xticklabels(df_plot.index)
    ax.legend()

    # Set the axis labels and title
    ax.set_xlabel('Strategy')
    ax.set_ylabel('Number of Cubes')
    ax.set_title('Assignments of Cubes to Robot and Human')

    # Display the plot
    plt.savefig(dest)
    plt.close()


def collisions_strategy(data, dest):
    # Create a grouped bar chart showing the number of foam collisions, wood collisions, and metal collisions by actor
    collisions_data = data.groupby(['strategy']).sum()[['foam collisions', 'wood collisions', 'metal collisions']]
    ax = collisions_data.plot(kind='bar', rot=0, figsize=(8, 6))
    ax.set_xlabel('Strategy')
    ax.set_ylabel('Number of Collisions')
    ax.legend(['Foam', 'Wood', 'Metal'], loc='upper left')
    plt.savefig(dest)
    plt.close()


def collisionscore_makespan_shared(data, dest):
    # Create a FacetGrid to visualize multiple graphs in a grid
    g = sns.FacetGrid(data, col="shared", margin_titles=True)

    # Plot makespan vs risk in a scatter plot
    g.map_dataframe(sns.scatterplot, x="best makespan", y="collision score", hue="strategy", style="strategy",
                    palette="deep", alpha=0.8)

    # Customize the axes labels
    g.set_axis_labels("Makespan", "Collision score")

    # Add a legend
    g.add_legend()

    # Show the plot
    plt.savefig(dest)
    plt.close()


def collisionscore_makespan_strategy(data, dest):
    # Create a FacetGrid to visualize multiple graphs in a grid
    g = sns.FacetGrid(data, col="strategy", margin_titles=True)

    # Plot makespan vs risk in a scatter plot
    g.map_dataframe(sns.scatterplot, x="best makespan", y="collision score", hue="shared", style="shared",
                    palette="deep", alpha=0.8)

    # Customize the axes labels
    g.set_axis_labels("Makespan", "Collision score")

    # Add a legend
    g.add_legend()

    # Show the plot
    plt.savefig(dest)
    plt.close()
