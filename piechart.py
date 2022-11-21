import os
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import warnings
warnings.filterwarnings('ignore')


user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASS')

connection = mysql.connector.connect(host='localhost', user = user, passwd = password, db = 'mydb')

df = pd.read_sql_query('SELECT * FROM Cities', connection)

# customizing the plot...
fig = px.pie(df, values='residents', names='name',
            title='Number of Martin\'s Friends Living in Each City',
            hover_data=['residents'], labels={'residents': 'friends living in this city'})
fig.update_traces(textposition='inside', textinfo = 'value+label')


# then, plot
fig.show()