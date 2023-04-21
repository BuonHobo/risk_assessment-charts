import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a Pandas DataFrame
data = pd.read_csv('dest.csv')

data=data.drop('expertise',axis=1)

# Group the data by planning strategy and shared tasks
grouped_data = data.groupby(['strategy', 'shared']).mean()

# Plot the time to plan vs. shared tasks for each planning strategy
for strategy in grouped_data.index.get_level_values('strategy').unique():
    strategy_data = grouped_data.loc[strategy]
    plt.plot(strategy_data.index.get_level_values('shared'), strategy_data['time'], label=strategy)

plt.xlabel('Shared Tasks')
plt.ylabel('Time to Plan (ms)')
plt.legend()
plt.savefig('test4')

plt.cla()

# Plot the number of tasks assigned to the robot and human vs. shared tasks for each planning strategy
for strategy in grouped_data.index.get_level_values('strategy').unique():
    strategy_data = grouped_data.loc[strategy]
    plt.plot(strategy_data.index.get_level_values('shared'), strategy_data['rtask'], label='Robot - ' + strategy)

plt.xlabel('Shared Tasks')
plt.ylabel('Number of Tasks Assigned')
plt.legend()
plt.savefig('test5')
