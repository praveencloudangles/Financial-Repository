import boto3
import pandas as pd


def data_loading():
    path = "risk_dataset.csv"

    df = pd.read_csv(path)
    print(df.head())
    return df
data_loading()
