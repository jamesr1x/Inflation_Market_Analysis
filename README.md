# How Do Inflation Metrics Influence S&P500 Returns and Volatility?

This is my 2nd year Data Science project at the University of Exeter for the module BEE2041_A_2_202526. The project involves collecting, analysing and reporting findings, to answer the following research question: **How Do Inflation Metrics Influence S&P500 Returns and Volatility?** I use 3 seperate inflation metrics: Inflation, inflation volatility and inflation surprise.

The analysis uses 300 monthly observations from 01/01/2001-12/31/2025 and collects 3 sets of raw data from 2 websites:

- **FRED** (CPIAUCSL)
- **FRED** (MICH)
- **Yahoo Finance** (^GSPC)
  
## Repository structure:
```
Inflation_Stock_Returns_Analysis/
│
├── Data/
│   ├── Cleaned_data/
│   └── Raw_data/
│
├── Outputs/
│   ├── Figures/
│   └── Tables/
│
├── Scripts/
│   ├── Get_raw_data.ipynb
│   ├── Clean.ipynb
│   ├── Analysis.ipynb
│   └── Make.py
│
├── FRED_API_key.txt # in .gitignore
├── LICENSE
├── README.md
└── Report.qmd
```

## Explanation of Directory:

### The project contains 4 scripts:

- "Get_raw_data.ipynb" collects raw data from the FED and Yfinance and converts this raw data into 3 csvs which are stored in "Data/Raw_data/"
- "Clean.ipynb" carries out data processing on the raw data csvs, combinding them into a single csv file called Clean.csv which is stored in "Data/Raw_data/"
- "Analysis.ipynb" carries out analysis on the cleaned data (Clean.csv). It produces graphs which are stored in "Outputs/Figures/" and regression tables which are stored in "Outputs/Tables/"
- "Make.py" sets up the folder structure for the directory and runs all 3 scripts in the correct order (Get_raw_data -> Clean -> Analysis)

### FRED_API_key.txt

- This text file is ignored by git. It contains my API key required to fetch data from the FRED. **PLEASE NOTE** If you are planning on cloning this project, create a blank txt file called FRED_API_key.txt and position it in the repository as shown above. Copy and paste your API key inside it. You can retrieve your personal API key from the FRED by creating an account here: https://fredhelp.stlouisfed.org/fred/account/fred-account-features/register/

### Report.qmd

- This is the final report

## Library and Version requirements:

Before running the scripts please install the following libraries:

- Python: 3.12.0
- Pandas: 3.0.1
- Matplotlib: 3.10.8
- Seaborn: 0.13.2
- Scipy: 1.17.1
- Statsmodels: 0.14.6
- Scikit-learn: 1.8.0
- Numpy: 2.4.4
- Yfinance: 1.2.0
- Fredapi: N/A

**NOTE:** If libraries are not functioning as expected please check versions match.

## Instructions

To replicate the analysis either:
- A) Pull the whole repository (Recommended)
- Run "make.py" to run all scripts
- Veiw Report.qmd (any updates to graphs and regression models will automatically be included)

OR
  
- B) Download the "Scripts" folder and "Report.qmd"
- Ensure the folder and files are in the following format:
```
├── Scripts/
│   ├── Get_raw_data.ipynb
│   ├── Clean.ipynb
│   ├── Analysis.ipynb
│   └── Make.py
│
└── Report.qmd
```
- Run "make.py" to run all scripts
- Veiw Report.qmd to view the final report (any updates to graphs and regression models will automatically be included)

**NOTE:** Within "Get_raw_data.ipynb" cell 3, a txt file is past in containing my API key, this file is in .gitignore so will not automatically appear. There are two options to deal with this:

A) As mentioned earlier under "Explanation of Directory", create a txt file called "FRED_API_key.txt" and paste in your API key (recommended).

B) Replace the contents of the brackets in the following code with your API key and remove the previous 2 rows of code:

```fred = Fred(api_key = fred_api_key)```

## Method

### 1. Data collection
- CPI and inflation expectations pulled via `fredapi`
- S&P500 data retrieved using `yfinance`

### 2. Data cleaning
- S&P500 data resampled to monthly, missing values filled, merged all 3 data sets
- Calculation of S&P500 returns, S&P500 volatility and inflation metrics

### 3. Analysis

**Graph Production:**
- Time‑series plots  
- Scatter plots with fitted lines  

**Regression Modelling:**
- S&P500 returns on inflation metrics  
- Lagged inflation metrics  
- S&P500 volatility on inflation metrics  
- Nonlinear models (squared terms)  
- Interaction model: inflation × inflation volatility  
- Volatility‑persistence model including lagged S&P500 volatility
-  **Note:** All regressions use **standardised coefficients** and **HC1 robust standard errors**.

## Summary

- Inflation metrics do not influence S&P500 returns or predict future returns.
- Initial Inflation volatility and inflation surprise correlate with S&P500 volatility.
- Once lagged S&P500 volatility is included in the model, all inflation metrics become insignificant.
- Past volatility is the strongest predictor of current volatility.
- To conclude inflation related uncertainty may trigger short‑term volatility spikes, but it is not a structural driver of ongoing market volatility.




