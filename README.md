# 🌍 Greenhouse Gas Emissions Analysis and Forecasting

## 📌 Project Overview

This project analyzes historical greenhouse gas emission trends and develops forecasting models to predict future CO₂ emissions.

The workflow covers the complete data science pipeline including data preprocessing, exploratory data analysis, feature engineering, machine learning regression models, and time-series forecasting.

The final objective is to compare different forecasting techniques and understand long-term emission trends across selected countries.


---

# 🎯 Problem Statement

Climate change analysis requires understanding historical emission patterns and estimating possible future trends.

This project aims to:

- Analyze historical CO₂ emission behavior
- Identify country-wise emission trends
- Engineer meaningful time-based features
- Build predictive machine learning models
- Apply time-series forecasting methods
- Compare different forecasting approaches


---

# 📊 Dataset

The dataset contains historical greenhouse gas emission information including:

- Country
- Year
- CO₂ emissions
- CO₂ emissions per capita
- Population indicators
- Greenhouse gas intensity indicators

The analysis focuses on selected countries representing different emission patterns and economic backgrounds.


---

# 🔄 Project Workflow

## 1. Data Acquisition and Exploration

Performed:

- Dataset loading
- Data Profiling
- Missing value analysis
- Global CO₂ Trend Analysis 
- Top Emitter Comparison
- Greenhouse Gas Composition Analysis



Notebook:

`WEEK_1_Data_aquisition_exploration_understanding.ipynb`


---

## 2. Feature Engineering

Performed:

- Time-Based Feature Creation
- Lag Features
- Per-Capita and Intensity Features
- Growth Rate Features
- Final Feature Dataset Creation


Notebook:

`WEEK_2_Feature_Engineering.ipynb`


---

## 3. Baseline ML Models – Regression

Performed:
- Problem Framing
- Time-Based Train-Test Split
- Naive Baseline Model
- Linear Regression Model
- Random Forest Regressor
- Model Performance Comparison

### Naive Baseline Model

Uses current year emissions as next-year prediction baseline.


### Linear Regression

Learns relationships between engineered features and future emissions.


### Random Forest Regression

Uses multiple decision trees to capture complex emission patterns.


Evaluation metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)


Notebook:

`WEEK_3_Baseline_ML_Model_Regression.ipynb`


---

## 4. Time-Series Forecasting with ETS(A,Ad,N) — Holt's Damped Trend

Performed:
- ETS Concept Introduction
- ETS Model Fitting
- Forecasting CO₂ Emissions to 2043
- Forecast Trend Interpretation
- Forecast Summary Table
- Final Model Validation


## ETS(A,Ad,N)

Components:

- Additive Error
- Additive Damped Trend
- No Seasonality


The ETS model forecasts emissions from:

2024 → 2043


Notebook:

`WEEK_4_Time_Series_Forecasting_with_ETS(A,Ad,N)_Holts_Damped_Trend.ipynb`


---

## 5. Scenario Analysis
Performed:

- Scenario Design
- Scenario Calculation
- Scenario Visualisations
- Impact Summary

Notebook:

`WEEK_5_Scenario_Analysis.ipynb`

---


# 📈 Model Evaluation

Models compared:

| Model |
|---|
| Naive Baseline |
| Linear Regression |
| Random Forest |
| ETS(A,Ad,N) |


Performance was evaluated country-wise using:

- MAE
- RMSE


The results showed that no single model performs best for every country. Model effectiveness depends on each country's emission trend.


---
# 🚀 How to Run the Project

Clone the repository:

```bash
git clone https://github.com/neeladrish/GHG-emission-analysis.git
```

Move into the project directory:

```bash
cd GHG-emission-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run notebooks in order:

```
├── WEEK_1_Data_aquisition_exploration_understanding
├── WEEK_2_Feature_Engineering
├── WEEK_3_Baseline_ML_Model_Regression
├── WEEK_4_Time_Series_Forecasting_with_ETS(A,Ad,N)_Holts_Damped_Trend
```



---

# 📊 Interactive Streamlit Dashboard

An interactive dashboard was developed using Streamlit to visualize emission trends, forecasts, and model results.

The dashboard includes:

- Project overview with key metrics
- Multi-country historical emission comparison
- Individual country emission profiles
- ETS(A,Ad,N) forecasts until 2043
- Machine learning vs time-series model comparison


## Running the Dashboard

Move into the project directory:

```bash
cd GHG-emission-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```
To Run:

```bash
streamlit run app.py
```

---

# 📁 Repository Structure
```
GHG-Emission-Analysis
│
├── data/
│   ├── ghg_features.csv
│   ├── model_data.csv
│   ├── comparison_table.csv
│   ├── ets_forecasts.csv
│   └── final_comparison.csv
│
├── WEEK_1_Data_aquisition_exploration_understanding
├── WEEK_2_Feature_Engineering
├── WEEK_3_Baseline_ML_Model_Regression
├── WEEK_4_Time_Series_Forecasting_with_ETS(A,Ad,N)_Holts_Damped_Trend
├── WEEK_5_Scenario_Analysis
|
├── app.py
├── requirements.txt
│
└── README.md

```



---

