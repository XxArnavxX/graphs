import pandas as pd
import plotly.express as px

ref = pd.read_csv("data.csv")
fig = px.bar(ref, x = "Country", y = "InternetUsers")
fig.show()