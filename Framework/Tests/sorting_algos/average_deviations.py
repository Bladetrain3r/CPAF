from bubble_sort import bubble_sort_with_deviation
import random

def run_sorting_simulations(num_simulations, list_size):
    all_averages = []
    for _ in range(num_simulations):
        random_numbers = [random.randint(1, 100) for _ in range(list_size)]
        deviations = bubble_sort_with_deviation(random_numbers)
        average_deviation = sum(deviations) / len(deviations)
        all_averages.append(average_deviation)
    
    refined_average = sum(all_averages) / num_simulations
    return refined_average

# Run the sorting simulation 100 times with a list size of 10
refined_average_deviation = run_sorting_simulations(1000, 100)
print(f"Refined average deviation over 100 simulations: {refined_average_deviation}")
