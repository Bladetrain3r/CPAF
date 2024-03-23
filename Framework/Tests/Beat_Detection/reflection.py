import pandas as pd

def refine_beat_detection(output_file='accumulated_beat_times.csv'):
    # Load the accumulated data
    df = pd.read_csv(output_file)
    
    # Round off the timeseries data to 10ms
    df['rounded_beat_time'] = df['beat_time'].round(decimals=3)
    
    # Identify unique timestamps across all runswc -l ref
    unique_timestamps = df['rounded_beat_time'].value_counts()
    outliers = unique_timestamps[unique_timestamps == 1].index
    
    # Filter out outliers
    refined_df = df[~df['rounded_beat_time'].isin(outliers)]
    
    # Save the refined data to a new CSV file
    refined_df.to_csv('refined_beat_times.csv', index=False)
    
    # Call the function to calculate deviation values for each run
    calculate_deviation_per_run(df)

def calculate_deviation_per_run(df):
    # Assuming a simple measure of deviation as the standard deviation of beat counts per iteration
    iteration_counts = df.groupby('iteration')['beat_time'].count()
    deviation = iteration_counts.std()

    mean_beats = df.groupby('iteration')['beat_time'].count().mean()

    # Compute absolute deviation from mean for each iteration
    df['deviation'] = df.groupby('iteration')['beat_time'].transform(lambda x: abs(x.count() - mean_beats))
    
    # Normalize deviations by the max possible deviation for visibility
    df['normalized_deviation'] = df['deviation'] / df['deviation'].max()
    
    # Here, we use the mean of normalized deviations as an example
    cpaf_deviation = df['normalized_deviation'].mean()

    print(f"CPAF Deviation Value: {cpaf_deviation}")
    print(f"Standard Deviation across runs: {deviation}")
    
    # Optionally, save or further process the deviation information

# Example usage
refine_beat_detection()
