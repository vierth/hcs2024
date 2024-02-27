import pandas as pd

# lets import our data
df = pd.read_csv('weather.csv', sep=',')
print(df.index)
print(df.columns)
print(df.head(10))
print(df.describe())

# drop missing information

# df = df.dropna()
# df = df.fillna(0)
# df.dropna(axis=1)

print(df.max(), df.min(), df.mean())