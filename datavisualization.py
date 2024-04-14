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
    dataset = data_cleaning()

    data = feature_eng()
    print("dfghjk--------------------------", data)


    car_df = dataset['type'].value_counts().rename_axis('type').reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=car_df['type'],
        y=car_df['count']
    ))
    fig.update_layout(template="plotly_dark", title="Distribution - Required Payment Type")
    fig.write_image("payment_type.jpg")

    #------------------------------------------------------------------------------


    car = data['isFraud'].value_counts().rename_axis('isFraud').reset_index(name='count')
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=car['isFraud'],
        y=car['count']
    ))
    fig.update_layout(template="plotly_dark", title="Distribution - Is Fraud")
    fig.write_image("Is_Fraud.jpg")

    #---------------------------------------------------------------------------------------

    top_products = dataset['type'].value_counts().head(10).index.tolist()
    filtered_df = dataset[dataset['type'].isin(top_products)]

    product_counts = filtered_df['type'].value_counts()

    fig = go.Figure(data=[go.Pie(labels=product_counts.index, values=product_counts.values)])
    
    fig.update_layout(
        template='plotly_dark',
        title='Payment Types'
    )

    fig.write_image("pie_chart.jpg")  
        
    #---------------------------------------------------------------------------------------
    
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
