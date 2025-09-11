import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df= pd.read_csv('kerala.csv')
print(df.head(5))
print("info",df.info())
print("shape",df.shape)
print(df.describe())

