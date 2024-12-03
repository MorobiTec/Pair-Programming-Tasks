## 4. Converting a csv file to a DataFrame
#import pandas as pd
#import matplotlib.pyplot as plt
#titanic = pd.read_csv('titanic.csv', skiprows=2)
#print(type (titanic))
#print(titanic.head(5))

#print(titanic.info())
#print(titanic.describe())

#titanic = pd.read_csv('titanic.csv', header=None, names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
#print(titanic.head(2))
#titanic = pd.read_csv('titanic.csv', index_col='Name')
#print(type (titanic))
#print(titanic.head(2))

#df = pd.read_excel('all_seasons.xlsx', sheet_name = 0, header = 0)
#print(df.head())


#df = pd.read_json('universities_ranking.json', orient='records')

#print(df.head())

# from pandas_datareader import wb

# all_indicators = pdr.wb.get_indicators()

# print(all_indicators.iloc[:5, :2])

import pandas as pd
from pandas_datareader import wb

# Download the data
result_data = wb.download(indicator="SP.DYN.LE00.IN", start='1975', end='1999', country='all')

# Optionally, convert specific columns to numeric
result_data['SP.DYN.LE00.IN'] = pd.to_numeric(result_data['SP.DYN.LE00.IN'], errors='coerce')

# Now handle the rest of the processing, like pivoting
aggregated_data = result_data.groupby(['country', 'year']).mean().reset_index()
pivot_result = aggregated_data.pivot(index='country', columns='year')

print(pivot_result)

