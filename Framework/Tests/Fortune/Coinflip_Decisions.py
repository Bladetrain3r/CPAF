import random
import math

def simulate_flips_decision_making(num_flips, initial_bias, initial_guess):
    good_fortune, bad_fortune = 0, 0
    current_bias = initial_bias
    current_guess = initial_guess

    for _ in range(num_flips):
        # Calculate the chance of changing the guess based on the log of the sum of fortunes
        total_fortune = good_fortune + bad_fortune
        if total_fortune > 0:
            change_chance = math.log(total_fortune + 1) / math.log(num_flips + 1)
            if random.random() < change_chance:
                current_guess = "tails" if current_guess == "heads" else "heads"

        # Adjust bias based on net influences (previous implementation)
        # Flip the coin with adjusted bias
        flip_result = "heads" if random.random() < current_bias else "tails"
        
        # Update fortunes based on outcome
        if flip_result == current_guess:
            good_fortune += 1
        else:
            bad_fortune += 1

    return good_fortune, bad_fortune, current_bias, current_guess

# Example usage
num_flips = 1000
initial_biases = [0.5, 0.7, 0.3]  # Example biases for three flippers
initial_guess = "heads"

for bias in initial_biases:
    good_fortune, bad_fortune, final_bias, final_guess = simulate_flips_decision_making(num_flips, bias, initial_guess)
    print(f"Initial Bias: {bias}, Final Bias: {final_bias}, Good Fortune: {good_fortune}, Bad Fortune: {bad_fortune}, Final Guess: {final_guess}")
