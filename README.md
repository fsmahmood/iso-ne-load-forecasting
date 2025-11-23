# ⚡️ ISO-NE Hourly Load Forecasting (2021–2025)

**ISO-NE (Independent System Operator of New England)** is the organization responsible for balancing the electric grid across the six New England states — ensuring that electricity supply meets demand every hour of the year. Since electricity has to match demand in real time, accurate demand forecasting is critical to keeping the power grid reliable and cost-efficient, especially during peak demand events.

This project builds an end-to-end **electricity demand forecasting pipeline** using publicly available ISO-NE hourly load data, spanning from **February 11, 2021 to June 23, 2025**. The goal is to produce **high-accuracy, operationally reliable forecasts** suitable for grid planning and energy market decision-making.

📌 For a quick overview, start with: [`03_final_results.ipynb`](iso-ne-load-forecasting/notebooks/03_final_results.ipynb)

---

## 🚀 Project Highlights
| Stage | Summary |
|-------|---------|
| **Data Ingestion** | Programmatically downloads ISO-NE hourly demand from the EIA site via `download.py` |
| **Data Cleaning** | Handles missing hours, duplicate timestamps, validation checks, and long seasonal gaps using rule-based imputation |
| **Modeling** | Evaluated naïve, seasonal-naïve, Holt-Winters, Ridge Regression models |
| **Feature Engineering** | Lag features (1/24/168), calendar features, and weather HDD/CDD feature for chosen Ridge Regression model |
| **Evaluation** | Train/test split (test data from July 2024 to June 2025), metrics computed **only on non-imputed hours** |
| **Result** | Ridge Regression with lag + calendar + HDD/CDD features achieved **3.41% MAPE** on the test period, with **2.73% MAPE** for the top 50 peak demand hours. |

📊 **A quick side-by-side model comparison appears in [`02_modeling.ipynb`](iso-ne-load-forecasting/notebooks/02_modeling.ipynb) — including naive, seasonal-naive, Holt-Winters, and the Ridge model.**


---

## 📂 Repository Structure
The project is built around three Jupyter notebooks that form the complete analysis pipeline:
1. **01_data_prep** — download + clean data  
2. **02_modeling** — train, evaluate, and compare the models
3. **03_final_results** — generate additional tables and visuals, followed by final analysis

🧪 To fully reproduce results: run `01_data_prep → 02_modeling → 03_final_results` in order.


```
.
├── notebooks ← 📌 core project files
│   ├── 01_data_prep.ipynb
│   ├── 02_modeling.ipynb
│   └── 03_final_results.ipynb
│
├── data
│   ├── download.py                # pulls raw data via links to CSV files from EIA.gov
│   ├── processed/                 # cleaned dataset used for modeling
│   └── raw/ (ignored)             # created automatically by running `download.py` in 01_data_prep
│
├── artifacts/                     # saved tables/metrics from 02_modeling used in 03_final_results
│
├── README.md
├── LICENSE
└── .gitignore
```
---

## 🔑 Guiding Principles of the Project
- **Transparency** — every hour is marked as original or imputed so nothing is hidden or assumed.
- **Evaluate forecasts only on real demand values** — synthetic data is never used to boost accuracy.
- **Keep the modeling practical** — fast, interpretable models that can realistically be used by grid operators (not just academic benchmarks).
- **Make everything reproducible** — running the notebooks in order should produce the same results starting from raw downloaded data.

---

## 📈 Final Results
- Ridge Regression (lags + calendar + HDD/CDD) delivered **≈ 3.41% MAPE**
- **Consistently outperformed** naïve, seasonal-naïve, and Holt-Winters models
- **Strong peak-hour performance**, including heat-wave periods

---

## 📌 Data Source
Hourly ISO-NE demand data is sourced from the U.S. Energy Information Administration (EIA) Wholesale Electricity Markets Archive (November 2025), through the `download.py` script that pulls CSV tables from the site.

No proprietary ISO-NE datasets are stored in this repository.

---

## 🙋 Why this project matters
This project demonstrates end-to-end ownership of a forecasting pipeline — from raw messy public data to a deployable model and clear interpretation. It is designed as a portfolio piece to show not just model accuracy, but **data transparency, reproducibility, and business relevance**.

---

## 📄 License

This project is released under the MIT License — free for research, learning, and portfolio use.

---
