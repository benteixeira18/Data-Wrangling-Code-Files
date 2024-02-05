'''

MISM3405 Spring 2023
Benjamin Teixeira
    
Filename: Bike_Location_Data_Grouping.py
    
Description:
    
'''
def main():
    
    # second dataset source + pandas documentation
    # https://data.boston.gov/dataset/blue-bike-stations/resource/d0121b02-ac37-4426-a42b-4a6d18d8676d
    # https://pandas.pydata.org/docs/reference/groupby.html
    
    # importing libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # reading csv file with bsv and blue bike data from "combined" spreadsheet
    bsv = pd.read_excel('combined.xlsx', sheet_name = 0)
    bikes = pd.read_excel('combined.xlsx', sheet_name = 1)
    
    # group bsv + bikes columns by desired metric
    bsv.groupby(by='Name')
    bikes.groupby(by='District')
    
    # remove index from output
    neighborhood = bsv.groupby(by='Name',as_index=False)
    bike_location = bikes.groupby('District',as_index=False)
    
    # grouping metric sums together
    pop100_re = neighborhood['POP100_RE'].sum()
    docks = bike_location['Total_docks'].sum()
    print(docks)
    
    # storing metric sums in variables based on column names
    pop = pop100_re['POP100_RE']
    district = docks['District']
    docks_count = docks['Total_docks']
    
    # sum of boston population and average amount of bos. pop per dock
    average = sum(pop)/docks_count
    print(district, round(average,2))
    
    # the above line dispalys the ratio of people to blue bike docks in boston.
    # ex: There are 617,603 people in Boston according to the BSV dataset, and
    # there are 3668 total docks in Boston. 617,603/3668 = ~168.38 people in
    # Boston per blue bike dock. Getting more people to utilize blue bikes 
    # will lead to a higher demand in blue bikes and docks, which will reduce 
    # our carbon footprint and keep socially vulnerable people protected.
    
    # creating the graph
    plt.figure(figsize = (13,11), dpi = 400)
    plt.title("Ratio of Boston Population to Greater Boston Blue Bike Docks")
    plt.xlabel("Greater Boston District")
    plt.ylabel("# of People in Boston per Dock")
    
    # # visualizing the data
    plt.scatter(district,average, edgecolors = "black")
    plt.savefig("bike_ratio.png")
    
    # the lower the number gets, the more access to cleaner alternatives 
    # to transportation there will be, leading to a healtheir world less
    # impacted by climate change and better lives for the socially vulnerable.
    
    
    

    
    
    
    
    
    
main()
