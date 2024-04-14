print("feature engineering---------------")
from data_cleaning import data_cleaning
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler


label_encoder = LabelEncoder()
def feature_eng():
    data = data_cleaning()

    columns_to_encode = ['type']
    for col in columns_to_encode:
        data[col] = label_encoder.fit_transform(data[col])

    dataset = data.copy()

    x = dataset.drop('isFraud', axis=1)
    y = dataset['isFraud']
    oversample = SMOTE()
    #undersample = RandomUnderSampler()
    X, Y = oversample.fit_resample(x, y)
    dataset = pd.concat([X, pd.Series(Y, name='isFraud')], axis=1)

    print("null values---------------",dataset.isnull().sum())
    print("drop null values-------------",dataset.dropna(inplace=True))
    print("duplicate values-----------", dataset.duplicated().sum())
    print("drop dupl----------", dataset.drop_duplicates(inplace=True))

    # data.to_csv('final.csv', index=False)
    dataset['type'] = dataset['type'].astype('int')
    dataset['amount'] = dataset['amount'].astype('int')
    dataset['oldbalanceOrg'] = dataset['oldbalanceOrg'].astype('int')
    dataset['newbalanceOrig'] = dataset['newbalanceOrig'].astype('int')
    dataset['newbalanceDest'] = dataset['newbalanceDest'].astype('int')
    dataset['oldbalanceDest'] = dataset['oldbalanceDest'].astype('int')
    dataset['isFraud'] = dataset['isFraud'].astype('int')

    dataset.to_csv("financial_usecase.csv",index=False)
    return dataset

feature_eng()
