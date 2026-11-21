import os
import numpy as np
import matplotlib.pyplot as plt

TOTAL_CHANNELS = 420
CELL_RADIUS = 1.0
MIN_REUSE_DISTANCE = 4.0
CLUSTER_SIZES = np.array([3, 4, 7, 9, 12])

reuse_ratio = np.sqrt(3 * CLUSTER_SIZES)
reuse_distance = CELL_RADIUS * reuse_ratio
channels_per_cell = TOTAL_CHANNELS / CLUSTER_SIZES

print(" N | D/R  | D (km) | Channels/Cell")
print("-" * 39)

for n, ratio, distance, channels in zip(
    CLUSTER_SIZES, reuse_ratio, reuse_distance, channels_per_cell
):
    print(f"{n:2d} | {ratio:4.2f} | {distance:6.2f} | {channels:12.2f}")

valid_indices = np.where(reuse_distance >= MIN_REUSE_DISTANCE)[0]

if len(valid_indices) > 0:
    best_index = valid_indices[0]
    best_n = CLUSTER_SIZES[best_index]

    print(f"\nMinimum required reuse distance = {MIN_REUSE_DISTANCE:.2f} km")
    print(f"Smallest feasible cluster size = {best_n}")
    print(f"Reuse distance = {reuse_distance[best_index]:.2f} km")
    print(f"Reuse ratio = {reuse_ratio[best_index]:.2f}")
    print(f"Channels per cell = {channels_per_cell[best_index]:.2f}")
else:
    best_index = None
    print("\nNo tested cluster size satisfies the minimum reuse distance.")

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(8, 5))
plt.plot(CLUSTER_SIZES, reuse_distance, "o-", label="Reuse distance")
plt.axhline(
    MIN_REUSE_DISTANCE,
    linestyle="--",
    color="red",
    label=f"Minimum distance ({MIN_REUSE_DISTANCE} km)"
)
if best_index is not None:
    plt.plot(
        CLUSTER_SIZES[best_index],
        reuse_distance[best_index],
        "s",
        color="green",
        markersize=8,
        label=f"Selected N = {CLUSTER_SIZES[best_index]}"
    )
plt.xlabel("Cluster Size (N)")
plt.ylabel("Reuse Distance (km)")
plt.title("Reuse Distance vs. Cluster Size")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/reuse_distance.png", dpi=300, bbox_inches="tight")
plt.show()

plt.figure(figsize=(8, 5))
plt.plot(CLUSTER_SIZES, channels_per_cell, "o-", color="orange")
if best_index is not None:
    plt.plot(
        CLUSTER_SIZES[best_index],
        channels_per_cell[best_index],
        "s",
        color="green",
        markersize=8,
        label=f"Selected N = {CLUSTER_SIZES[best_index]}"
    )
plt.xlabel("Cluster Size (N)")
plt.ylabel("Channels per Cell")
plt.title("Channels per Cell vs. Cluster Size")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/channels_per_cell.png", dpi=300, bbox_inches="tight")
plt.show()
