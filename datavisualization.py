print("data visulization-------")
from data_cleaning import data_cleaning
from feature_engineering import feature_eng
import pandas as pd
import plotly.express as px
from IPython.display import Image
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import plotly.io as pio
import plotly.graph_objects as go
import io
from PIL import Image
a =[]
def data_visualization():
    dataset = feature_eng()
    column = list(dataset.columns)
    print("sdfghjk--------------------",column)

    columns_to_remove_outliers = ["type","amount", "newbalanceDest", "amount", "oldbalanceOrg", "newbalanceOrig", "oldbalanceDest", "isFraud"]

    for col in columns_to_remove_outliers:
        q1 = dataset[col].quantile(0.25)
        q3 = dataset[col].quantile(0.75)
        iqr = q3 - q1
        upper_limit = q3 + (1.5 * iqr)
        lower_limit = q1 - (1.5 * iqr)

        # Apply the filtering conditions to the original DataFrame
        dataset = dataset.loc[(dataset[col] < upper_limit) & (dataset[col] > lower_limit)]

    for i in column:
        fig = px.histogram(dataset, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        fig.write_image(f"{i}_hist.jpg")

    #colum_box = ['type', 'amount', 'oldbalanceOrg', 'isFraud']

    
    for i in column:
        fig = px.box(dataset, y=i)
        fig.update_layout(template='plotly_dark')
        fig.update_xaxes(showgrid=False,zeroline=False)
        fig.update_yaxes(showgrid=False,zeroline=False)
        fig.write_image(f"{i}_box.jpg")
        

    
    df=dataset.drop("isFraud",axis=1)
    y=df.corr().columns.tolist()
    z=df.corr().values.tolist()
    z_text = np.around(z, decimals=4) # Only show rounded value (full value on hover)
    fig = ff.create_annotated_heatmap(z,x=y,y=y,annotation_text=z_text,colorscale=px.colors.sequential.Cividis_r,showscale=True)
    fig.update_layout(template='plotly_dark')
    # fig.show()
    fig.write_image("heat_map.jpg")
    # a.append(fig)
    
    return dataset

data_visualization()
