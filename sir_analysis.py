import math
import os
import matplotlib.pyplot as plt

TOTAL_CHANNELS = 420
CELL_RADIUS = 1.0
MIN_REUSE_DISTANCE = 4.0
CLUSTER_SIZES = [3, 4, 7, 9, 12]
PATH_LOSS_EXPONENT = 4
FIRST_TIER_INTERFERERS = 6


def reuse_distance(cluster_size):
    return CELL_RADIUS * math.sqrt(3 * cluster_size)


def sir_db(cluster_size):
    reuse_ratio = math.sqrt(3 * cluster_size)
    sir_linear = (reuse_ratio ** PATH_LOSS_EXPONENT) / FIRST_TIER_INTERFERERS
    return 10 * math.log10(sir_linear)


print(
    f"{'N':>3} {'D (km)':>9} {'Feasible':>10} "
    f"{'Ch/cell':>10} {'SIR (dB)':>10}"
)
print("-" * 48)

feasible_sizes = []
sir_values = []

for n in CLUSTER_SIZES:
    distance = reuse_distance(n)
    feasible = distance >= MIN_REUSE_DISTANCE
    channels = TOTAL_CHANNELS / n
    sir = sir_db(n)
    sir_values.append(sir)

    if feasible:
        feasible_sizes.append(n)

    print(
        f"{n:>3} {distance:>9.3f} {str(feasible):>10} "
        f"{channels:>10.2f} {sir:>10.2f}"
    )

if feasible_sizes:
    best_n = min(feasible_sizes)
    print(f"\nSmallest feasible cluster size = {best_n}")
    print(f"Channels per cell = {TOTAL_CHANNELS / best_n:.2f}")
    print(f"Reuse distance = {reuse_distance(best_n):.3f} km")
    print(f"Approximate SIR = {sir_db(best_n):.2f} dB")
else:
    print("\nNo tested cluster size satisfies the minimum reuse distance.")

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(CLUSTER_SIZES, sir_values, "o-", color="purple")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Approximate SIR (dB)")
plt.title("SIR vs. Cluster Size")
plt.grid(True)
plt.tight_layout()
plt.savefig("figures/sir_vs_cluster_size.png", dpi=300, bbox_inches="tight")
plt.show()
