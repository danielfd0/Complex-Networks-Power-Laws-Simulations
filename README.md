# Complex-Networks-Power-Laws-Simulations
# Chapter 16: Complex Networks & Power Laws Simulations

This repository contains Python simulations exploring **power-law distributions**, **Zipf's law**, and **preferential attachment** models — common in complex networks and natural language.

These scripts were developed as part of exercises from **Chapter 16** (likely *Networks, Crowds, and Markets* or similar textbook).

---

## 📋 Scripts Overview

### `16.8.py` — Monkey Typing & Zipf's Law (Theoretical)
- Generates words using a simplified monkey typing model with probabilities `q` (for 'a') and `r` (space).
- Words correspond to Fibonacci numbers by pseudo-rank.
- Demonstrates **power-law rank-frequency distribution**.
- Plots theoretical distribution + power-law fit on log-log scale.
- Compares fitted exponent with theoretical value involving golden ratio φ.

### `16.9.py` — Monkey Typing Simulation (Empirical)
- Simulates random typing with 8 letters + space.
- Two scenarios:
  1. Uniform letter probabilities.
  2. Random (Dirichlet) letter probabilities.
- Extracts words and plots **rank-frequency** on log-log scale.
- Shows emergence of heavy-tailed word frequency distributions.

### `16.10.py` — Preferential Attachment (Copy Model)
- Simple directed network growth model with one out-link per node.
- Mixture of uniform random attachment (`γ = 0.5`) and preferential attachment via copying.
- Generates degree distribution and **CCDF** (Complementary Cumulative Distribution Function).
- Classic model that produces power-law tails.

### `16.11.py` — Preferential Attachment with Multiple Out-links
- More realistic variant: each new node adds `m = 3` out-links.
- Combines uniform attachment and link copying.
- Produces richer degree distributions.
- Includes both standard degree plot and CCDF on log-log scales.

---

## 🛠 Requirements

```bash
pip install numpy matplotlib.
