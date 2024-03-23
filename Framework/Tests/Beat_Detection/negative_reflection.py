import pandas as pd
import numpy as np

def generate_noise(input_file='accumulated_beat_times.csv'):
    # Load the accumulated data
    df = pd.read_csv(input_file)
    
    # Determine the min and max of the beat times
    min_time = df['beat_time'].min()
    max_time = df['beat_time'].max()
    # Get the range of iterations
    min_iter = df['iteration'].min()
    max_iter = df['iteration'].max()
    
    # Generate random beat times and iterations within their respective ranges
    noise_count = np.random.randint(5, 15)  # Randomly decide how many noises to add
    noise_times = np.random.uniform(min_time, max_time, noise_count)
    noise_iterations = np.random.randint(min_iter, max_iter + 1, noise_count)
    
    # Create a DataFrame for the noise data
    noise_df = pd.DataFrame({
        'iteration': noise_iterations,
        'beat_time': noise_times
    })
    
    # Combine the original data with the noise data
    combined_df = pd.concat([df, noise_df])
    
    # Re-sort the DataFrame by beat_time to maintain chronological order
    combined_df.sort_values(by='beat_time', inplace=True)
    
    # Save the modified DataFrame back to a CSV
    combined_df.to_csv('noisy_accumulated_beat_times.csv', index=False)

# Example usage
generate_noise()
