import os
import subprocess
import sys
import papermill as pm

# Install all required libraries
subprocess.check_call([
    sys.executable, "-m", "pip", "install",
    "jupyter", "papermill", "pandas", "matplotlib", "seaborn",
    "scipy", "statsmodels", "scikit-learn", "numpy",
    "yfinance", "fredapi"
])

print("Libraries Installed")

#create folder structure incase folders were accidently deleted or moved
os.makedirs("Data/Raw_data", exist_ok=True)
os.makedirs("Data/Cleaned_data", exist_ok=True)
os.makedirs("Outputs/Figures", exist_ok=True)
os.makedirs("Outputs/Tables", exist_ok=True)
os.makedirs("Executed_scripts", exist_ok=True)

# 1. Get raw data
pm.execute_notebook("Scripts/Get_raw_data.ipynb","Executed_scripts/Get_raw_data_output.ipynb",cwd="Scripts")
print("Retrieved raw data.")

# 2. Clean data
pm.execute_notebook("Scripts/Clean.ipynb","Executed_scripts/Clean_output.ipynb",cwd="Scripts")
print("Cleaned data.")

# 3. Run analysis
pm.execute_notebook("Scripts/Analysis.ipynb","Executed_scripts/Analysis_output.ipynb",cwd="Scripts")
print("Completed analysis.")

print("Project build complete.")