def swap_bits(number):
    # Swaps bits from least to most significant and vice versa in an 8-bit number
    return int('{:08b}'.format(number)[::-1], 2)

def calculate_deviation(current, target):
    # Calculates the deviation based on bit differences
    deviation = sum((current >> i) & 1 != (target >> i) & 1 for i in range(8)) / 8.0
    print(deviation)
    return sum((current >> i) & 1 != (target >> i) & 1 for i in range(8)) / 8.0

# Example
base_number = 0b11010110  # Example base number (null state)
fully_swapped = swap_bits(base_number)  # Calculate fully swapped state once

# Simulate process and calculate deviation
current_state = base_number
deviation = calculate_deviation(current_state, fully_swapped)
while current_state != fully_swapped:
    current_state = swap_bits(current_state)  # Apply swapping process
    print(current_state, deviation)  # Print current state and deviation
    deviation = calculate_deviation(current_state, fully_swapped)  # Update deviation
    
