import random

# This is a simple example of a system exemplified by a deck of cards, with interactions in the form of shuffling
# It does not account for all local and global interactions, but it does demonstrate the concept of a system.

# Function to shuffle the deck
def shuffle_deck(deck):
    shuffled_deck = list(deck)
    random.shuffle(shuffled_deck)
    return tuple(shuffled_deck)

# Function to calculate deviation
def calculate_deviation(deck, null_state):
    deviation = sum(1 for original, shuffled in zip(null_state, deck) if original != shuffled) / len(deck)
    return deviation

# Function to shuffle the deck less efficiently
def custom_shuffle_deck(deck):
    shuffled_deck = list(deck)
    num_pairs = random.randint(1, 20)  # Select between 1-20 pairs to transpose
    
    for _ in range(num_pairs):
        # Randomly select two positions in the deck to swap
        pos1, pos2 = random.sample(range(len(deck)), 2)
        shuffled_deck[pos1], shuffled_deck[pos2] = shuffled_deck[pos2], shuffled_deck[pos1]
    
    return tuple(shuffled_deck)

# Initialize variables for demonstration
null_state = tuple(range(1, 53))  # A tuple representing a deck of cards numbered 1 to 52
n_shuffles = random.randint(1, 6)  # Number of shuffles to perform, randomly chosen between 1 and 6
deck = null_state
deviations = []

# Perform the custom shuffle n times and calculate deviation after each shuffle
for i in range(n_shuffles):
    deck = custom_shuffle_deck(deck)
    deviation = calculate_deviation(deck, null_state)
    deviations.append(deviation)
    print(f"Shuffle {i+1}: Deck order: {deck}")
    print(f"Deviation after shuffle {i+1}: {deviation:.4f}")

# Calculate and print the average deviation
average_deviation = sum(deviations) / len(deviations)
print(f"Average deviation after {n_shuffles} shuffles: {average_deviation:.4f}")
