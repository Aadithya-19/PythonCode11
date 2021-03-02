import plotly.express as ps
import pandas as spb
import plotly.graph_objects as go

data = spb.read_csv("studentData.csv")

print(data.groupby("level")["attempt"].mean())

student_df = data.loc[data['student_id']=='TRL_abc']

print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(x = student_df.groupby("level")["attempt"].mean(), y = ["Level 1", "Level 2", "Level 3", "Level 4"], orientation = 'h'))

fig.show()