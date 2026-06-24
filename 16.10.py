import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

N = 1_000_000
gamma = 0.5

# Initialize 4 nodes in a cycle: 1→2, 2→3, 3→4, 4→1
targets = [0] * (N + 1)
targets[1] = 2
targets[2] = 3
targets[3] = 4
targets[4] = 1

in_degree = [0] * (N + 1)
for i in range(1, 5):
    in_degree[targets[i]] += 1

current_n = 4

for m in range(5, N + 1):
    if random.random() < gamma:
        # Uniform random attachment
        target = random.randint(1, current_n)
    else:
        # Copy model / preferential attachment: pick random existing page and copy its out-link
        u = random.randint(1, current_n)
        target = targets[u]

    targets[m] = target
    in_degree[target] += 1
    current_n += 1

# Degree distribution analysis
deg_count = Counter(in_degree[1:N+1])
max_deg = max(in_degree[1:N+1])

# Plot degree distribution (log-log)
degrees = list(range(1, max_deg + 1))
counts = [deg_count.get(d, 0) for d in degrees]

plt.figure(figsize=(10, 6))
plt.loglog(degrees, counts, 'b.', markersize=2)
plt.xlabel('Degree k')
plt.ylabel('Number of vertices with degree k')
plt.title('Degree Distribution (Preferential Attachment with γ=0.5)')
plt.grid(True, which="both", ls="--")
plt.savefig('degree_dist.png')
plt.show()

# Complementary Cumulative Distribution Function (CCDF)
cum = 0
ccdf = []
ks = list(range(1, max_deg + 1))
for k in range(max_deg, 0, -1):
    cum += deg_count.get(k, 0)
    ccdf.append(cum)
ccdf = ccdf[::-1]  # reverse to match k=1..max

plt.figure(figsize=(10, 6))
plt.loglog(ks, ccdf, 'r.', markersize=2)
plt.xlabel('Degree k')
plt.ylabel('Number of vertices with degree ≥ k')
plt.title('Complementary Cumulative Degree Distribution (CCDF)')
plt.grid(True, which="both", ls="--")
plt.savefig('ccdf.png')
plt.show()

# Summary statistics
print(f"Max degree: {max_deg}")
print(f"Nodes with degree 1: {deg_count[1]}")
print(f"Fraction with degree 1: {deg_count[1]/N:.4f}")
print(f"Nodes with degree >= 10: {sum(deg_count[d] for d in range(10, max_deg+1))}")
