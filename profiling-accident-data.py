'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename:
    
Description:
    
'''
# pip install pandas_profiling
import pandas as pd
from pandas_profiling import ProfileReport as pr

# read your csv file
file = pd.read_excel("US_accidents_data_subset_MA.xlsx")

# run the report
profile = pr(file, title = "profile")

# output the profile in a file elsewhere
profile.to_file("profile_report.html")
