import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def simulate_typing(n_chars=1_000_000, seed=42):
    np.random.seed(seed)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    space_prob = 0.2

    # Scenario 1: Uniform probabilities
    letter_probs1 = np.full(8, 0.1)
    probs1 = np.append(letter_probs1, space_prob)
    chars1 = np.random.choice(letters + [' '], size=n_chars, p=probs1)

    # Scenario 2: Random letter probabilities summing to 0.8
    letter_probs2 = np.random.dirichlet(np.ones(8)) * 0.8
    probs2 = np.append(letter_probs2, space_prob)
    chars2 = np.random.choice(letters + [' '], size=n_chars, p=probs2)

    return chars1, chars2

def extract_words(chars):
    """Extract words, treating consecutive spaces as empty words"""
    words = []
    current = ''
    for c in chars:
        if c == ' ':
            words.append(current)
            current = ''
        else:
            current += c
    words.append(current)  # last word
    return words

# Run simulation
chars1, chars2 = simulate_typing()

words1 = extract_words(chars1)
words2 = extract_words(chars2)

freq1 = Counter(words1)
freq2 = Counter(words2)

# Prepare data for plotting
def get_rank_freq(freq_counter):
    sorted_freq = sorted(freq_counter.values(), reverse=True)
    ranks = np.arange(1, len(sorted_freq) + 1)
    return ranks, sorted_freq

ranks1, freqs1 = get_rank_freq(freq1)
ranks2, freqs2 = get_rank_freq(freq2)

# Plotting
plt.figure(figsize=(10, 6))
plt.loglog(ranks1, freqs1, 'b-', alpha=0.8, label='Scenario 1 (Uniform)')
plt.loglog(ranks2, freqs2, 'r-', alpha=0.8, label='Scenario 2 (Random Probs)')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.title('Word Frequency Distribution (Log-Log Plot)')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# Print summary
print(f"Scenario 1: {len(words1):,} words, {len(freq1):,} distinct")
print(f"Scenario 2: {len(words2):,} words, {len(freq2):,} distinct")
print("Top 5 words Scenario 1:", freq1.most_common(5))
print("Top 5 words Scenario 2:", freq2.most_common(5))
