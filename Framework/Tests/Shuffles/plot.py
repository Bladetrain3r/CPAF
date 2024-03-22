import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

# Read the CSV files
shuffles = pd.read_csv('./shuffles.csv')
pyshuffles = pd.read_csv('./pyshuffles.csv')

# Creating the plot
fig = go.Figure()

fig.add_trace(go.Scatter(x=shuffles['Shuffles'], y=shuffles['Avg'],
                         mode='lines+markers', name='Custom Shuffle'))

fig.add_trace(go.Scatter(x=pyshuffles['Shuffles'], y=pyshuffles['Avg'],
                         mode='lines+markers', name='Python Shuffle'))

fig.update_layout(title='Comparison of Shuffle Algorithms Over Time',
                  xaxis_title='Number of Shuffles',
                  yaxis_title='Average Deviation',
                  legend_title='Algorithm')

# Save the figure to an HTML file
html_file_path = './shuffle_comparison_plot.html'
pio.write_html(fig, file=html_file_path)