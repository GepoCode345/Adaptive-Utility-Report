# Adaptive Utility Report (AUR)

The **Adaptive Utility Report (AUR)** is a Python framework for evaluating the magnitude and consistency of performance differences between adaptive and fixed models across repeated experimental runs.

AUR is currently under active development.

---

## Current Version

The current implementation provides:

- Paired comparison of adaptive and fixed model results
- Adaptive gain-magnitude calculation
- User-defined percentile selection
- Percentile Upside
- Percentile Spread
- Automatic generation of a terminal-based AUR report

Further components are planned for future versions.

---

## Methodology

For each paired adaptive and fixed result, AUR calculates the magnitude of the relative difference:

$$
m_s = 100 \frac{|M_{A,s} - M_{F,s}|}{|M_{F,s}|}
$$

where:

- $M_{A,s}$ is the adaptive result for seed $s$
- $M_{F,s}$ is the corresponding fixed result
- $m_s$ is the percentage gain magnitude

Because the numerator uses an absolute value, this quantity measures the **magnitude of the difference** between the adaptive and fixed results.

---

## Percentile Selection

The user specifies a percentile $p$.

The number of observations selected is:

$$
k_p = \left\lceil \frac{p}{100} n \right\rceil
$$

where:

- $p$ is the requested percentile
- $n$ is the total number of experimental runs
- $k_p$ is the number of selected runs
- $\lceil \cdot \rceil$ denotes rounding upward to the nearest integer

The gain magnitudes are ranked from highest to lowest, and the first $k_p$ observations are selected.

Because $k_p$ must be an integer, the effective percentile may differ slightly from the requested percentile.

The effective percentile is:

$$
p_{\mathrm{eff}} = 100\frac{k_p}{n}
$$

---

## Percentile Upside

The **Percentile Upside** is the mean gain magnitude within the selected percentile.

If the selected magnitudes are ordered as

$$
m_{(1)} \geq m_{(2)} \geq \dots \geq m_{(k_p)}
$$

then:

$$
U_p = \frac{1}{k_p}\sum_{i=1}^{k_p}m_{(i)}
$$

A larger Percentile Upside indicates a larger average adaptive-to-fixed difference within the selected highest-magnitude runs.

---

## Percentile Spread

The **Percentile Spread** measures the range of gain magnitudes within the selected percentile:

$$
S_p = \max_{i \leq k_p}(m_{(i)}) - \min_{i \leq k_p}(m_{(i)})
$$

Equivalently, because the selected observations are already ordered:

$$
S_p = m_{(1)} - m_{(k_p)}
$$

A smaller spread indicates that the selected gain magnitudes are more tightly grouped.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/GepoCode345/Adaptive-Utility-Report.git
cd Adaptive-Utility-Report
```

Install the package locally:

```bash
pip install -e .
```

The intended public package installation method will eventually be:

```bash
pip install adaptive-utility-report
```

after the package is published to PyPI.

---

## Input Format

The current version accepts a CSV file with the following structure:

```csv
Seed,Adaptive_DA,Fixed_DA
15,58.3,50.0
16,55.6,52.4
17,61.1,51.2
18,52.8,48.8
```

Each row represents one paired experimental run.

- `Seed` identifies the experimental run
- `Adaptive_DA` contains the adaptive-model result
- `Fixed_DA` contains the corresponding fixed-model result

The adaptive and fixed observations must be correctly paired.


For a requested percentile of `30`, AUR selects approximately the top 30% of observations ranked by gain magnitude.

For example, with 10 runs:

$$
k_{30} = \left\lceil \frac{30}{100}(10) \right\rceil = 3
$$

so three observations are selected.

---

## Package Structure

```text
Adaptive-Utility-Report/
│
├── LICENSE
├── NOTICE
├── README.md
├── pyproject.toml
│
├── src/
│   └── aur/
│       ├── __init__.py
│       ├── read_data.py
│       ├── gains.py
│       ├── percentile.py
│       ├── spread.py
│       └── report.py
│
├── tests/
│
└── examples/
    └── weird.csv
```

---

## Project Status

AUR is currently an **early-stage research software project**.

The present version implements the first percentile-based components of the Adaptive Utility Report methodology.

Additional analytical, historical, reporting, and validation components are planned as the framework develops.

The API, input format, and methodology may therefore change between early versions.

---

## License

Adaptive Utility Report is licensed under the **Apache License, Version 2.0**.

See `LICENSE` and `NOTICE` for further information.

Copyright 2026 Gabriel Duque Díaz.