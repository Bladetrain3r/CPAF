import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Read the CSV files
shuffles_df = pd.read_csv('./shuffles.csv')
pyshuffles_df = pd.read_csv('./pyshuffles.csv')

# Creating the plot
fig = go.Figure()

# Adding traces for the custom shuffle algorithm
fig.add_trace(go.Scatter(x=shuffles_df['Shuffles'], y=shuffles_df['Avg'],
                         mode='lines+markers', name='Custom Shuffle Avg Deviation',
                         line=dict(color='blue')))
fig.add_trace(go.Scatter(x=shuffles_df['Shuffles'], y=shuffles_df['Final'],
                         mode='lines+markers', name='Custom Shuffle Final Deviation',
                         line=dict(color='navy')))

# Adding traces for the Python shuffle algorithm
fig.add_trace(go.Scatter(x=pyshuffles_df['Shuffles'], y=pyshuffles_df['Avg'],
                         mode='lines+markers', name='Python Shuffle Avg Deviation',
                         line=dict(color='red')))
fig.add_trace(go.Scatter(x=pyshuffles_df['Shuffles'], y=pyshuffles_df['Final'],
                         mode='lines+markers', name='Python Shuffle Final Deviation',
                         line=dict(color='darkred')))

# Updating the layout of the plot
fig.update_layout(title='Comparison of Custom and Python Shuffle Algorithms',
                  xaxis_title='Number of Shuffles',
                  yaxis_title='Deviation',
                  legend_title='Legend')

# Saving the figure as an HTML file
html_file = './shuffle_comparison_3.html'
pio.write_html(fig, file=html_file)
