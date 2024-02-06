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

    print("-------------------",data['isFraud'].value_counts())

    x = data.drop('isFraud', axis=1)
    y = data['isFraud']
    #oversample = SMOTE()
    undersample = RandomUnderSampler()
    X, Y = undersample.fit_resample(x, y)
    data = pd.concat([x, pd.Series(Y, name='isFraud')], axis=1)

    print("null values---------------",data.isnull().sum())
    print("drop null values-------------",data.dropna(inplace=True))
    print("duplicate values-----------", data.duplicated().sum())
    print("drop dupl----------", data.drop_duplicates(inplace=True))

    print("data types----------------",data.dtypes)
    # data.to_csv('final.csv', index=False)
    data['type'] = data['type'].astype('int')
    data['amount'] = data['amount'].astype('int')
    data['oldbalanceOrg'] = data['oldbalanceOrg'].astype('int')
    data['newbalanceOrig'] = data['newbalanceOrig'].astype('int')
    data['newbalanceDest'] = data['newbalanceDest'].astype('int')
    data['oldbalanceDest'] = data['oldbalanceDest'].astype('int')
    data['isFraud'] = data['isFraud'].astype('int')
    print(data.dtypes)

    data.to_csv("financial_usecase.csv",index=False)
    return data

feature_eng()
