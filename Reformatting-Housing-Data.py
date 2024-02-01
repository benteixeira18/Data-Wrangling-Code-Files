'''

DS2000 Spring 2022
Benjamin Teixeira
    
Filename: Data_Formatting_Assignment_pt2.py
    
Description: Reformatting Data
    
'''
# importing libraries
import pandas as pd

# reading csv file into pandas dataframe
homes = pd.read_csv("Boston_Homes_Sales_2021_INPUT.csv")

# formatting column headers to match desired PDF output
property_type = homes['PROPERTY TYPE']
address = homes['ADDRESS']
year = homes['YEAR BUILT']
beds = homes['BEDS']
baths = homes['BATHS']
sq_ft = homes['SQUARE FEET']
price = homes['PRICE']
price_sq_ft = homes['$/SQUARE FEET']

# listing supplementary address values together
city = homes['CITY']
state = homes['STATE OR PROVINCE']
zip_code = homes['ZIP OR POSTAL CODE']

# merging address data together, converting zip code values to string
# official pandas documentation used for astype function
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html
homes['Address'] = (address+' '+city+' '+state+' '+'0' + zip_code.astype(str))
new_address = homes['Address']

# creating new dataframe from desired columns
formatted_homes = pd.DataFrame(list(zip(property_type,new_address,year,
beds,baths,sq_ft,price,price_sq_ft)),columns=['Property Type','Address',
'Year Built','Beds','Baths','Square Feet','Price','Price Per Sq. Feet'])
                                   
# sorting by Property Type and Price
sorted_homes = formatted_homes.sort_values(by=['Property Type','Price'])

# sorting price and price per sq. feet by currency
sorted_homes['Price'] = ('$'+price.astype(str))
sorted_homes['Price Per Sq. Feet'] = ('$'+price_sq_ft.astype(str))

# outputting file to csv
sorted_homes.to_csv("Boston_Homes_Sales_2021_OUTPUT.csv",index=False)



# Data Report

# sort by the following metrics:
# only condos
condos = sorted_homes[sorted_homes['Property Type']==['Condo/Co-op']]
print(condos)



