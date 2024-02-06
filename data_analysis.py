print("data analysis--------------")
from data_loading import data_loading
import pandas as pd
import seaborn as sns
import matplotlib as plt

def data_analysis():
    data = data_loading()
    data.info()
    data.describe()
    data.isnull().sum()
    data.columns
    data.shape
    for col in data.columns:
        print(col, data[col].nunique())

    data.duplicated().sum()

    return data

data_analysis()