import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

def load_and_prepare_data(file_path):
    """
    Load and prepare the data for analysis.
    """
    # Load the data
    df = pd.read_csv(file_path)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'])

    # Set 'Date' as the index
    df.set_index('Date', inplace=True)

    return df

def interactive_graph(df):
    # Create an interactive plot using Plotly
    fig = go.Figure()

    # Add line for each column
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))

    fig.update_layout(title='Closing Prices of The Big 7',
                      xaxis_title='Date',
                      yaxis_title='Closing Price',
                      legend_title='Companies',
                      template='plotly_dark',
                      hovermode='x unified')

    fig.show()

def show_correlation_heatmap(df):
    # Create a correlation heatmap using Seaborn
    returns = df.pct_change().dropna()

    # Calculate the correlation matrix
    correlation_matrix = returns.corr()

    #Plot the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True, cbar_kws={"shrink": .8})
    plt.title('Correlation Heatmap of The Big 7')
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()

def main():
    file_path = 'mag7.csv'
    df = load_and_prepare_data(file_path)
    interactive_graph(df)
    show_correlation_heatmap(df)

if __name__ == "__main__":
    main()
