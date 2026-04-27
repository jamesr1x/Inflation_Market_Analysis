# How Do Inflation Metrics Influence S&P500 Returns and Volatility?

This is my 2nd year Data Science project at the University of Exeter for the module BEE2041_A_2_202526. The project involves collecting, analysing and reporting findings, to answer the following research question: **How Do Inflation Metrics Influence S&P500 Returns and Volatility?** I use 3 seperate inflation metrics: Inflation, inflation volatility and inflation surprise.

The analysis uses 300 monthly observations from 01/01/2001-12/31/2025 and collects 3 sets of raw data from 2 websites:

- **FRED** (CPIAUCSL)
- **FRED** (MICH)
- **Yahoo Finance** (^GSPC)

**To view the rendered final report please follow the link:** https://jamesr1x.github.io/Inflation_Stock_Returns_Analysis/Report.html

## Repository structure:
```
Inflation_Stock_Returns_Analysis/
│
├── Data/
│   ├── Cleaned_data/
│   └── Raw_data/
│
├── Make_scripts/
│   ├── Make_API_key.py
│   └── Make_no_API_key.py
│
├── Outputs/
│   ├── Figures/
│   └── Tables/
│
├── Scripts/
│   ├── Get_raw_data.ipynb
│   ├── Clean.ipynb
│   └── Analysis.ipynb
│
├── Formatting.css
├── FRED_API_key.txt # in .gitignore
├── LICENSE
├── README.md
├── Report.html
└── Report.qmd
```

## Explanation of Directory:

### Scripts/:

**The project contains 3 scripts:**

- "Get_raw_data.ipynb" collects raw data from the FED and Yfinance and converts this raw data into 3 csvs which are stored in "Data/Raw_data/".
- "Clean.ipynb" carries out data processing on the raw data csvs, combinding them into a single csv file called Clean.csv which is stored in "Data/Raw_data/".
- "Analysis.ipynb" carries out analysis on the cleaned data (Clean.csv). It produces graphs which are stored in "Outputs/Figures/" and regression tables which are stored in "Outputs/Tables/".

### FRED_API_key.txt

This text file is ignored by git. It contains my API key required to fetch data from the FRED. **PLEASE NOTE** If you are planning on cloning this project, create a blank txt file called FRED_API_key.txt and position it in the repository as shown above. Copy and paste your API key inside it. You can retrieve your personal API key from the FRED by creating an account here: https://fredhelp.stlouisfed.org/fred/account/fred-account-features/register/

### Make_scripts/

**The project has 2 Make scripts:**

- "Make_API_key.py"
- "Make_no_API_key.py"

An explanation for how to use these scripts is provided under [Instructions For Setup](#instructions-for-setup)

### Report.html

This is the final rendered report.

## Library and Version requirements:

Before running the scripts please install the following libraries:

- Python: 3.12.0
- Jupyter: v2025.9.1
- Papermill: 2.7.0
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

## Instructions For Setup

### 1) Clone the repository:

- Create a folder on your device you wish to contain the repository
- Open Git Bash and type the following commands:
```
CD "FOLDER_PATH" #where FOLDER_PATH is the path to your folder

git clone "https://github.com/jamesr1x/Inflation_Stock_Returns_Analysis.git"
```
### 2) Install papermill 
- In the terminal type:
```
pip install papermill
```

### 3) Run either of the following 2 make scripts:

**Make_no_API_key**: 
- Runs only "Clean.ipynb" and "Analysis.ipynb" script - If pulling raw data is not required this is easier, it does not require the user to create an API key.

**Make_API_key**: 
- Runs all 3 scripts, including gathering and cleaning raw data.
- **NOTE:** Within "Get_raw_data.ipynb" cell 3, a txt file is past in containing my API key, this file is in .gitignore so will NOT automatically download when you clone the repository. As mentioned earlier under [Explanation of Directory](#explanation-of-directory), create a txt file called "FRED_API_key.txt" and paste in your API key.

### 4) View Report
- Veiw report.qmd (any updates to graphs and regression models will automatically be included).

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




