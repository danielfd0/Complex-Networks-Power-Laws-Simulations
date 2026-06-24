import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# ========================= PARAMETERS =========================
q = 0.4                     # Probability of 'a' (0 < q < (√5-1)/2 ≈ 0.618)
r = 1 - q - q**2            # Probability of space
print(f"q = {q:.4f}, r = {r:.4f}\n")

# ====================== FIBONACCI NUMBERS ======================
def generate_fibonacci(n):
    """Generate first n+1 Fibonacci numbers with F0=0, F1=1"""
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return fib

max_j = 50
fib = generate_fibonacci(max_j + 3)

# ====================== VERIFICATION PART (b) ======================
print("Verification: Number of words with pseudo-rank j")
print("j".center(5), "W(j)".center(8), "Probability".center(15))
print("-" * 35)

for j in range(15):  # Show first 15 for clarity
    prob = q**j * r
    print(f"{j:5d} {fib[j+1]:8d} {prob:.2e}")

# ====================== RANK-FREQUENCY ANALYSIS ======================
# Cumulative number of words up to pseudo-rank j
cumulative = np.cumsum([fib[j + 1] for j in range(max_j + 1)])

ranks = []
probs = []

for j in range(max_j + 1):
    num_words = fib[j + 1]
    start_rank = cumulative[j - 1] if j > 0 else 0
    p = r * (q ** j)
    
    ranks.extend(range(start_rank + 1, start_rank + num_words + 1))
    probs.extend([p] * num_words)

ranks = np.array(ranks)
probs = np.array(probs)

# ========================= PLOTTING =========================
plt.figure(figsize=(11, 7))

plt.loglog(ranks, probs, 'b.', markersize=4, label='Theoretical')

# Power-law fit in the tail (avoid very low ranks)
valid = ranks > 50
log_ranks = np.log(ranks[valid])
log_probs = np.log(probs[valid])

coeff = np.polyfit(log_ranks, log_probs, 1)
alpha = -coeff[0]
fitted = np.exp(coeff[1]) * ranks**coeff[0]

plt.loglog(ranks, fitted, 'r--', linewidth=2, 
           label=f'Power-law fit: $k^{{-{alpha:.3f}}}$')

plt.xlabel('Rank k (log scale)')
plt.ylabel('Probability p(k) (log scale)')
plt.title(f'Monkey Typing Power Law\n(q = {q:.3f}, α ≈ {alpha:.3f})')
plt.legend()
plt.grid(True, which='both', linestyle='--', alpha=0.7)

plt.show()

# ========================= SUMMARY =========================
print(f"\nFitted power-law exponent α ≈ {alpha:.4f}")
print(f"Theoretical α = -ln(q) / ln(φ) ≈ {-np.log(q)/np.log((1+np.sqrt(5))/2):.4f}")
