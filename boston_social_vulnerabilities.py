'''

MISM3405 Spring 2023
Benjamin Teixeira
    
Filename: boston_social_vulnerabilities.py
    
Description: wrangling and visualizing boston social vulnerability risk data
    
'''
def main():
    
    # importing libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # official data sources + pandas documentation used
    # https://data.boston.gov/dataset/climate-ready-boston-social-vulnerability
    # https://pandas.pydata.org/docs/reference/groupby.html
    
    # reading Boston_Social_Vulnerabilities.csv file, grouping columns by name
    bsv = pd.read_csv("Boston_Social_Vulnerabilities.csv")
    bsv.groupby(by="Name")
    
    # creating neighborhood variable, remove index's from output
    neighborhood = bsv.groupby(by="Name",as_index=False)
    
    # grouping neighborhood mean averages together; use 'OlderAdult' means
    # disclaimer: different variables provide different visuals & insights
    neighborhood_population_averages = neighborhood["OlderAdult"].mean()
    print(neighborhood_population_averages)
    
    # distinguishing between neighborhood names and their population averages
    names = neighborhood_population_averages["Name"]
    averages = neighborhood_population_averages["OlderAdult"]
    
    # creating graph to visualize neighborhood averages of OlderAdult pop.
    plt.figure(figsize = (8,6), dpi = 400)
    plt.title("Boston Population at Risk of Climate Vulnerabilities")
    plt.xlabel("Boston Neighborhood")
    plt.ylabel("Average Population of Older Adults per Neighborhood")
    
    # visualize the data, clean x-axis
    plt.bar(names,averages, color = "darkgreen")
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,
                14,15,16,17,18,19,20,21,22],["Alst.","BBay","BVlg","Bri.",
                "ChTwn","Dor","E.Bos","Fen","Harb.","Hyde","JP","LthDis","LMA",
                "MttPn","M.Hll","N.End","Ros.","Rox.","S.Bos","S.Wtr","S.End",
                "W.End","W.Rox"], size = 6)                                     
    plt.savefig("OlderAdults.png")
    
main()