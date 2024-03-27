import random
import math

def simulate_flips_with_influence(num_flips, initial_head_probability, guess):
    good_fortune, bad_fortune = 1, 1
    fortune_multiplier = 2
    head_probability = initial_head_probability

    for _ in range(num_flips):
        # Apply external influence
        if random.random() < 0.5:
            deviation = 0.01 if random.random() < 0.5 else -0.01
            head_probability = min(max(head_probability + deviation, 0), 1)  # Ensure it stays within 0 and 1

        # Simulate the flip
        flip_result = "heads" if random.random() < head_probability else "tails"
        
        # Check the guess and update fortunes
        if flip_result == guess:
            good_fortune *= fortune_multiplier
        else:
            bad_fortune *= fortune_multiplier

    return good_fortune, bad_fortune, head_probability

def normalize_counters(num_flips, good_fortune, bad_fortune):
    # Neutral expectation for good fortune is 50% of num_flips
    neutral_good_fortune = num_flips * 0.5
    
    # Calculate deviation from neutral for good fortune
    good_fortune_deviation = (good_fortune - neutral_good_fortune) / num_flips
    
    # Calculate deviation from neutral for bad fortune
    # Since bad fortune increases with incorrect guesses, and neutral luck would result in 50% incorrect guesses:
    neutral_bad_fortune = num_flips * 0.5
    bad_fortune_deviation = (bad_fortune - neutral_bad_fortune) / num_flips
    
    return good_fortune_deviation, bad_fortune_deviation

import math

def normalize_counters_log(num_flips, good_fortune, bad_fortune):
    # Calculate the expected "neutral" counters after num_flips
    # Assuming neutral fortune would not multiply or diminish the fortune,
    # the neutral counters would remain equal to their starting value (set to 1 for simplicity)
    neutral_good_fortune = 1
    neutral_bad_fortune = 1
    
    # Calculate logarithmic deviation from neutral for good fortune
    # Adding a check to ensure good_fortune is greater than 0 to avoid math domain error
    good_fortune_deviation = math.log(good_fortune / neutral_good_fortune, 2) / num_flips if good_fortune > 0 else 0
    
    # Calculate logarithmic deviation from neutral for bad fortune
    # Similarly ensuring bad_fortune is greater than 0
    bad_fortune_deviation = math.log(bad_fortune / neutral_bad_fortune, 2) / num_flips if bad_fortune > 0 else 0
    
    return good_fortune_deviation, bad_fortune_deviation





# Example usage
num_flips = 100
flipper_scenarios = [(0.5, "heads"), (0.7, "heads"), (0.3, "heads")]

for initial_head_probability, guess in flipper_scenarios:
    good_fortune, bad_fortune, final_head_probability = simulate_flips_with_influence(num_flips, initial_head_probability, guess)
    print(f"Initial Prob: {initial_head_probability}, Final Prob: {final_head_probability}, Good Fortune: {good_fortune}, Bad Fortune: {bad_fortune}")
    good_fortune_deviation, bad_fortune_deviation = normalize_counters_log(num_flips, good_fortune, bad_fortune)
    print(f"Good Fortune Deviation: {good_fortune_deviation}, Bad Fortune Deviation: {bad_fortune_deviation}")
