import pandas as pd

dataframe = pd.read_csv('../Resources/cities.csv')
dataframe.to_html('data.html', index=False)
table = dataframe.to_html()