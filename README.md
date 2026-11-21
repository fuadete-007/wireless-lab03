# Cellular Frequency Reuse and Co-Channel Interference Analysis

A Python-based simulation of **frequency reuse in cellular communication systems**. The project compares cluster sizes, calculates co-channel reuse distance and channels per cell, checks a minimum reuse-distance requirement, and estimates the signal-to-interference ratio (SIR).

## Objectives

- Calculate the frequency reuse ratio and co-channel reuse distance.
- Calculate the average number of channels assigned per cell.
- Identify the smallest tested cluster size that meets a minimum reuse-distance requirement.
- Estimate how SIR changes with cluster size.
- Visualize the results using Matplotlib.

## Tools and Libraries

- Python 3
- NumPy
- Matplotlib
- Python `math` and `os` standard-library modules

## Repository Structure

```text
Frequency-Reuse-Analysis/
├── frequency_reuse.py
├── sir_analysis.py
├── figures/
│   ├── reuse_distance.png
│   ├── channels_per_cell.png
│   └── sir_vs_cluster_size.png
├── requirements.txt
└── README.md
```

## Simulation Parameters

| Parameter | Value |
|---|---:|
| Total available channels | 420 |
| Cell radius, R | 1 km |
| Minimum reuse distance | 4 km |
| Cluster sizes, N | 3, 4, 7, 9, 12 |
| Path-loss exponent, n | 4 |
| First-tier co-channel interferers, K | 6 |

## Theory

### 1. Frequency reuse ratio

\[
Q = \frac{D}{R} = \sqrt{3N}
\]

### 2. Co-channel reuse distance

\[
D = R\sqrt{3N}
\]

Here, \(D\) is the distance between co-channel cells, \(R\) is the cell radius, and \(N\) is the cluster size.

### 3. Channels per cell

\[
C_{\text{cell}} = \frac{C}{N}
\]

Here, \(C\) is the total number of available channels. The result can be fractional when the total is not evenly divisible by the cluster size; it represents an average.

### 4. Approximate SIR

Using the simplified equal-distance, first-tier interference model:

\[
SIR \approx \frac{(D/R)^n}{K}
\]

In decibels:

\[
SIR_{dB} = 10\log_{10}\left(\frac{(\sqrt{3N})^n}{K}\right)
\]

The model assumes that all \(K\) first-tier interferers are at approximately the same distance from the mobile receiver. It is an idealized estimate, not a full propagation or network simulation.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Frequency-Reuse-Analysis.git
cd Frequency-Reuse-Analysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the simulations

```bash
python frequency_reuse.py
```

```bash
python sir_analysis.py
```

The scripts print their numerical results and save the plots in the `figures/` directory. Run the commands from the project root directory so the figures are saved in the expected location.

## Results

With the parameters above, the calculations give:

| Cluster size (N) | Reuse distance (km) | Average channels per cell | Approx. SIR (dB) |
|---:|---:|---:|---:|
| 3 | 3.000 | 140.00 | 11.30 |
| 4 | 3.464 | 105.00 | 13.80 |
| 7 | 4.583 | 60.00 | 18.66 |
| 9 | 5.196 | 46.67 | 20.85 |
| 12 | 6.000 | 35.00 | 23.34 |

**Smallest tested feasible cluster size: \(N = 7\)**

For \(N=7\):

- Reuse distance: **4.58 km**
- Frequency reuse ratio: **4.58**
- Average channels per cell: **60**
- Approximate SIR: **18.66 dB**

## Generated Figures

### Reuse Distance vs. Cluster Size

![Reuse Distance vs. Cluster Size](figures/reuse_distance.png)

### Channels per Cell vs. Cluster Size

![Channels per Cell vs. Cluster Size](figures/channels_per_cell.png)

### Approximate SIR vs. Cluster Size

![SIR vs. Cluster Size](figures/sir_vs_cluster_size.png)

## Key Observations

1. Reuse distance increases as cluster size increases.
2. A larger reuse distance generally reduces co-channel interference.
3. The average number of channels per cell decreases as cluster size increases.
4. The simplified SIR estimate increases with cluster size.
5. For the specified 4 km minimum reuse distance, \(N=7\) is the smallest feasible value among the tested cluster sizes.

## Conclusion

The simulation demonstrates the trade-off between frequency reuse, channel capacity, and co-channel interference. A larger cluster size increases the separation between co-channel cells and improves the estimated SIR, but reduces the average number of channels available per cell.

For the selected system parameters, **a cluster size of 7** is the smallest tested configuration that satisfies the 4 km minimum reuse-distance requirement.

---

**Topic:** Cellular Frequency Reuse and Co-Channel Interference Analysis  
**Programming Language:** Python  
**Application Area:** Mobile and Wireless Communication
