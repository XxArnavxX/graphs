import pandas as pd
import plotly.express as px
 
ref = pd.read_csv("data.csv")
fig = px.scatter(ref, x = "Population", y = "Per capita", size = "Percentage", color = "Country")
fig.show()