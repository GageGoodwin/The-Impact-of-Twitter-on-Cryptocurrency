import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


folder_path = "dogecoin_history_rates_apr21-jul21-SNL.csv"
dfDogeSNL = pd.read_csv(folder_path)

dfDogeSNL["date"] = [d.split('T')[0] for d in dfDogeSNL["time_period_start"]]

dfDogeSNL.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)
print(dfDogeSNL.head(100))
print(dfDogeSNL.columns)

fig, axs = plt.subplots()

show_every = 6

sparse_xticks = [None] * dfDogeSNL["date"].shape[0]
sparse_xticks[::show_every] = dfDogeSNL["date"][::show_every]

axs.set_title("DOGECOIN HIGH VALUES FROM (April - July)", fontsize = 15)
axs.tick_params(axis = 'x', labelsize = 10)
axs.set_xlabel('Date', size = 14)
axs.tick_params(axis = 'y', labelsize =10)
axs.set_ylabel('Price in $', size = 14)
axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=45)
plt.plot( dfDogeSNL["date"], dfDogeSNL["rate_open"])


plt.show()