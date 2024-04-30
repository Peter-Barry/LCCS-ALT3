# Import all relevant libraries or functions
# Bearing in mind that the more you import the bigger your program and
# the more space it will take up in memory
# Also the import statements will only work if the relevant modules or plugins
# have been added to THONNY
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import sklearn
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# Access and open the datasource
df= pd.read_csv('drivingtest.csv')
# The following commands are used to interrogate the data but also to ensure you
# access and are processing the correct data print(df.head(5)) 
print("info",df.info())  # Print first 5 rows of data
print("shape",df.shape) # shows 12 rows and 7 columns
print(df.describe())    # calculates some count,mean,std,min etc
# Here we put our own logic for the model we are trying to build
# Can you write the python logic that will determine the outcome based on your
# own parameters?

# drivers = open("drivingtest.csv","r") # Open the file
MyPass = 0
MyFail = 0
GenderF = 0
GenderM = 0
    
with open('drivingtest.csv', 'r+') as file:  #r+ means read and write
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row in the CSV file
    print("Printing rows")

    for row in csv_reader:
        #Here you will create the logic for deciding whether or not
        #the result is a PASS or FAIL
        if row[6] == "Pass" and int(row[2]) > 18:
            MyPass += 1
            print(row[2],"MyPass")
        # if Occupation  is none and income  is 0 and age < 18 FAIL!    
        if row[4] == "None" and row[5] == 0 and int(row[2]) < 18:
            MyFail += 1
            print(row[2],"MyFail")
            
        """
        # Print the values of the cells in the row
        print(row[0], "   ",
              row[1], "   ",
              row[2], "   ",
              row[3], "   ",
              row[4], "   ",
              row[5], "   ",
              row[6])
        """
print("MyFail",MyFail,"MyPass",MyPass)
#Here you will put in the graph to illustrate your model


