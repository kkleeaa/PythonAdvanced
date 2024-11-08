import plotly.express as px
import pandas as pd
import matplotlib

df=pd.read_csv('avgIQpercountry.csv')
df["Population-2023"]=df["Population-2023"].str.replace(',','').astype(float)

print(df.info())

fig=px.scatter_geo(df,locations="Country",locationmode='country names',hover_name="Country", size="Average IQ",color="Continent", projections="natural earth", title="Average IQ per country",sizemax=20,template="plotly dark")
fig.show()

