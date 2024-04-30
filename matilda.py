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
OnLine = df['OnLine']
Age    = df['Age']
Age99  = df['Age99']
Age12  = df['Age12']
Age13  = df['Age13']
Age14  = df['Age14']
Product  = df['Product']
Spend    = df['Spend']
Makeup   = df['Makeup']
Food   = df['Food']
Toys   = df['Toys']
Hacked   = df['Hacked']
#Print the Age99 column data
print (Age99)

# Compute and display the mean
mean_value_age = round(statistics.mean(Age),2)
mean_value_age99 = round(statistics.mean(Age99),2)
mean_value_spend = round(statistics.mean(Spend),2)
print("Mean Value age:",type(mean_value_age), mean_value_age)
print("Mean Value age99:",type(mean_value_age99), mean_value_age99)
print("Mean Value spend:", type(mean_value_spend), mean_value_spend)

# Compute and display the median
median_value_spend = statistics.median(Spend)
median_value_age = statistics.median(Age)
#median_value_product = statistics.median(Product)
print("Median Value Spend:", median_value_spend)
print("Median Value Age:", median_value_age)
#print("Median Value Product:", median_value_product)

#print Mode
mode_value_spend = statistics.mode(Spend)
mode_value_age = statistics.mode(Age)
print("Mode Value Spend:", mode_value_spend)
print("Mode Value Age:", mode_value_age)

#Print some min and max
print("MinAge: €%f, MinSpend: €%f" %(min(Age),min(Spend)))
print("MaxAge: €%f, MaxSpend: €%f" %(max(Age),max(Spend)))

#Calculate and Print Sums
tot_makeup = sum((Makeup) == "Yes")
print("Total Makeup:", tot_makeup)
#No Makeup here??
tot_food = sum((Food) == "Yes")
print("Total Food:", tot_food)
#No Food Here??
tot_toys = sum((Toys) == "Yes")
print("Total Toys:", tot_toys)
#No Toys here??
tot_hacked_yes = sum((Hacked) == "Yes")
print("Total Yes Hacked:", tot_hacked_yes)
tot_hacked_no = sum((Hacked) == "No")
print("Total Not Hacked:", tot_hacked_no)



"""
# Compute and display the min and max values
print("Min: €%f, Max: €%f" %(min(player_values),max(player_values)))

# Second smallest unique value
s1 = list(set(sorted(player_values)))
s2 = sorted(s1)
print("Min:", s2[1])
print("Max:", s2[len(s2)-1])
"""
