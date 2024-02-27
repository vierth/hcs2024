import pandas as pd
import matplotlib.pyplot as plt

# lets import our data
df = pd.read_csv('weather.csv', sep=',')

# df["TMAX"].notnull()
# print(df["TMAX"].notnull().value_counts())
df = df[df["TMAX"].notnull()]
df = df[df["TMIN"].notnull()]
df["TAVG"] = df[['TMAX', "TMIN"]].mean(1)

hot = df[df["TMAX"]> 28]
rot = df[df["NAME"]=="ROTTERDAM, NL"]
rot["DATE"] = pd.to_datetime(rot["DATE"])
rot = rot.set_index("DATE")
rot["TMAX"].plot()
plt.show()
