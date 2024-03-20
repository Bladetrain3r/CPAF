import random
import plotly.graph_objects as go
from plotly.offline import plot

# Function to calculate the average deviation per step
def calculate_average_deviation(deviations):
    return sum(deviations) / len(deviations)

def bubble_sort_with_deviation(arr):
    n = len(arr)
    deviations = []  # To store deviation after each pass
    
    # Function to calculate deviation
    def calculate_deviation(sorted_arr, current_arr):
        correct_positions = sum(1 for x, y in zip(sorted_arr, current_arr) if x == y)
        return correct_positions / n
    
    # Generate the sorted array for deviation comparison
    sorted_arr = sorted(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        deviation = calculate_deviation(sorted_arr, arr)
        deviations.append(deviation)
        print(f"Iterations:  Deviation: {deviation:.8f}")
        if not swapped:  # If no two elements were swapped by inner loop, then break
            break
    
    # Calculate and print the average deviation per step
    average_deviation = calculate_average_deviation(deviations)
    print(f"\nAverage deviation per step: {average_deviation:.4f}\n")
    print(f"Number of iterations: {len(deviations)}")
    
    return deviations

# Generate 10 random numbers within a larger range for more variability
random_numbers = [random.randint(1, 100000) for _ in range(10000)]
print("Initial array:", random_numbers)

# Sort the array and print deviation at each step
deviations = bubble_sort_with_deviation(random_numbers)

# Plot the deviations over iterations
fig = go.Figure()
fig.add_trace(go.Scatter(y=deviations, mode='lines+markers', name='Deviation'))
fig.update_layout(title='Deviation Over Iterations in Bubble Sort',
                  xaxis_title='Iteration',
                  yaxis_title='Deviation',
                  yaxis=dict(range=[0, 1]))

plot(fig, filename='bubble_sort_deviation.html', auto_open=False)
