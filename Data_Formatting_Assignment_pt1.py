'''

MISM304 Spring 2023
Benjamin Teixeira
    
Filename: Data_Formatting_Assignment_pt1.py
    
Description: Data Structure Practice
    
'''
# import libraries
import pandas as pd

# creating DataFrame
company = ['Microsoft','Apple','Alphabet','Amazon']
stock = ['MSFT','AAPL','GOOGL','AMZN']
price = [243.16,143.06,97.00,100.41]
date = ['1/30/23 3:30pm','1/30/23 3:30pm','1/30/23 3:30pm','1/30/23 3:30pm']

stock_dataframe = pd.DataFrame(list(zip(company,stock,price,date)),
                               columns=['Company','Stock','Stock Price ($)',
                               'Date'])

# printing original frame
print(stock_dataframe)

# creating a list to add to the dataframe
high_price = [price[0]>100,price[1]>100,price[2]>100,price[3]>100]
stock_dataframe['Price Greater than 100'] = high_price

# printing edited dataframe
print()
print(stock_dataframe)

# adding stock data from 2 additional companies, creating DataFrame
# twitter and snapchat
# https://finance.yahoo.com/quote/TWTR/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANLHQFPuP9l8yaF2lxaWWO9G5wz6RwJrbeLQuxOiaCyaAsYIE-GlfLHYbxt9pD7EZXHwKCknpkNxA53-t59OQEia8UhXXYrn6xah_bLN9sUAxW3jWYk4ZrQ7O6uehVCted0-em_TE90zbZg61uhAkyqzIM9M9-zuWj791JzAv17h
# https://finance.yahoo.com/quote/SNAP?p=SNAP&ncid=yahooproperties_stockrecom_g40boan2td8

# create list variables
added_companies = ['Twitter','Snapchat']
added_stock = ['TWTR','SNAP']
added_price = [53.70,11.00]
added_date = ['2/03/23 4::02pm','2/03/23 4::02pm']
added_high_price = [added_price[0]>100,added_price[1]>100]

# create dataframe from lists
added_dataframe = pd.DataFrame(list(zip(added_companies,added_stock,
added_price,added_date, added_high_price)),columns=['Company','Stock',
                        'Stock Price ($)','Date','Price Greater than 100'])
                                                  
print()
print(added_dataframe)

# append dataframe from added stock data to original stock data
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.append.html
combined_data_frame = stock_dataframe.append(added_dataframe)
print()
print(combined_data_frame)

# creating subset of low stocks
low_stocks = combined_data_frame[combined_data_frame['Stock Price ($)']<100]
print()
print(low_stocks)

# creating subset of low stock prices from low stocks
low_prices = low_stocks.iloc[0:,2]
print()
print("Sum of Low Stock Prices: $",sum(low_prices))








    