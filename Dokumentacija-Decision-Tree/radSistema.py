import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import entropy

def makePairsForPlot(df: pd.DataFrame, state="NORMAL_STATE", dot_color='green'):
    wt_columns = [col for col in df.columns if col.startswith('WT')]

    for wt_col in wt_columns:
        wt_values = df[wt_col]
        normal_state_values = df[state]

        # Filter rows where 'NORMAL_STATE' is 1
        wt_values_normal_state_1 = wt_values[normal_state_values == 1]

        if not wt_values_normal_state_1.empty:
            # Scatter plot of 'WT' values when 'NORMAL_STATE' is 1
            plt.scatter(wt_values_normal_state_1.index, wt_values_normal_state_1, label=f'WT values in {state}',
                        marker='o', color=dot_color)

    # Adding labels and legend
    plt.xlabel('Discrete time values')
    plt.ylabel('Wather thermometer values')


    # Show the plot
    plt.show()

