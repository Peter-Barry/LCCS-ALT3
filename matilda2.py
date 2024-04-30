# Event: ALT2
# Author: PBarry 
# Using pandasand Statistics - recommended for larger files
import statistics
import pandas

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('shopping2.csv')
#df['Age99'] = df['Age99'].fillna('')
#df = df.dropna(subset=['Age99'])
#df.to_csv('shopping.csv', index=False)

# Filter out the columns
Age99  = df['Age99']

print (Age99)

# Compute and display the mean
mean_value_age99 = round(statistics.mean(Age99),2)
mean_value_age99 = round(statistics.mean(Age99),2)

print("Mean Value age99:",type(mean_value_age99), mean_value_age99)