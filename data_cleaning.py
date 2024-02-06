print("data cleaning----------------")
from data_analysis import data_analysis
from imblearn.over_sampling import SMOTE
from collections import Counter
import pandas as pd


def data_cleaning():
    data = data_analysis()
    data.dropna(inplace=True)
    data.isnull().sum()
    data.drop_duplicates(inplace=True)
    data.duplicated().sum()
    data.drop('step', inplace=True, axis=1)
    data.drop('isFlaggedFraud', inplace=True, axis=1)
    data.drop('nameOrig', inplace=True, axis=1)
    data.drop('nameDest', inplace=True, axis=1)
    print(data.head())

    return data

data_cleaning()