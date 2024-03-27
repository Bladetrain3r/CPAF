import random

def simulate_flips_advanced(num_flips, initial_bias, guess):
    good_fortune, bad_fortune = 0, 0
    current_bias = initial_bias

    for _ in range(num_flips):
        # Calculate the net influence of good and bad fortune
        net_good_influence = good_fortune - 0.5 * bad_fortune
        net_bad_influence = bad_fortune - 0.5 * good_fortune
        
        # Adjust bias based on net influences
        bias_adjustment = (net_good_influence - net_bad_influence) * 0.01
        current_bias = min(max(initial_bias + bias_adjustment, 0), 1)
        
        # Flip the coin with adjusted bias
        flip_result = "heads" if random.random() < current_bias else "tails"
        
        # Update fortunes based on outcome
        if flip_result == guess:
            good_fortune += 1  # Increment good fortune for correct guess
        else:
            bad_fortune += 1  # Increment bad fortune for incorrect guess

    return good_fortune, bad_fortune, current_bias

# Example usage
num_flips = 100
initial_biases = {"Flipper 1": 0.5, "Flipper 2": 0.55, "Flipper 3": 0.45}
guess = "heads"

for flipper, bias in initial_biases.items():
    good_fortune, bad_fortune, final_bias = simulate_flips_advanced(num_flips, bias, guess)
    print(f"{flipper}: Good Fortune: {good_fortune}, Bad Fortune: {bad_fortune}, Final Bias: {final_bias}")
