import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


wdown = pd.read_csv(".\data\WDO$N_M1.csv", sep="\t")
winwn = pd.read_csv(".\data\WIN$N_M1.csv", sep="\t")


# fig, ax = plt.subplots(2, 2)


date_time = [
    datetime.strptime(f'{data["<DATE>"]} {data["<TIME>"]}',  '%Y.%m.%d %H:%M:%S') for index, data in wdown.iterrows()]

wdown["<DATETIME>"] = date_time
wdown.set_index("<DATETIME>", inplace=True)

wdown = wdown.drop(columns=['<DATE>', '<TIME>'])


# wdown["<DATETIME>"] = date_time
# wdown.set_index(['<DATE>', '<TIME>'], inplace=True)

# wdown.plot()


monthly = wdown.resample('BM').mean()


daily = wdown.resample('D').mean()

daily.plot()
plt.show()
