import pandas as pd;
import plotly.express as px;

data = pd.read_csv('final_stars.csv');

fig1 = px.scatter(data, x = data['mass'], y = data['radius'], color=data['name'], size='mass');
fig2 = px.scatter(data, x = data['distance'], y = data['gravity'], color=data['name'], size='mass')
fig1.show();
fig2.show();