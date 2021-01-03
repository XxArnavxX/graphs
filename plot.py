import pandas as pd
import plotly.express as px

ref = pd.read_csv("line_chart.csv")
fig = px.line(ref, x = "Year", y = "Per capita income", color = "Country", title = "Per capita income")
fig.show()