import random
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

N = 1_000_000
gamma = 0.5
m = 3  # outlinks per new node

# Initialize 4 nodes: complete graph K4 (each points to the other 3)
targets = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for i in range(1, 5):
    for j in range(1, 5):
        if i != j:
            targets[i].append(j)
            in_degree[j] += 1

current_n = 4

for node in range(5, N + 1):
    for _ in range(m):
        if random.random() < gamma:
            # Uniform random attachment
            target = random.randint(1, current_n)
        else:
            # Copy existing link (preferential)
            u = random.randint(1, current_n)
            if targets[u]:
                target = random.choice(targets[u])
            else:
                target = random.randint(1, current_n)

        targets[node].append(target)
        in_degree[target] += 1
    current_n += 1

# Degree distribution analysis
deg_count = Counter(in_degree[1:N+1])
max_deg = max(in_degree[1:N+1])

print(f"Max in-degree: {max_deg}")
print(f"Nodes with in-degree 1: {deg_count.get(1, 0)} ({deg_count.get(1, 0)/N:.4%})")

# Degree distribution plot
degrees = sorted(deg_count.keys())
counts = [deg_count[d] for d in degrees]

plt.figure(figsize=(10, 6))
plt.loglog(degrees, counts, 'b.', markersize=1.5)
plt.xlabel('Degree k')
plt.ylabel('Number of vertices with degree k')
plt.title('Degree Distribution (m=3, γ=0.5)')
plt.grid(True, which="both", ls="--")
plt.savefig('degree_dist_m3.png', dpi=150)
plt.show()

# Complementary Cumulative Degree Distribution (CCDF)
max_k = max_deg
ccdf = np.cumsum([deg_count.get(k, 0) for k in range(max_k, 0, -1)])[::-1]

ks = list(range(1, max_k + 1))
plt.figure(figsize=(10, 6))
plt.loglog(ks, ccdf, 'r.', markersize=1.5)
plt.xlabel('Degree k')
plt.ylabel('Number of vertices with degree ≥ k')
plt.title('Complementary Cumulative Degree Distribution (m=3)')
plt.grid(True, which="both", ls="--")
plt.savefig('ccdf_m3.png', dpi=150)
plt.show()
