import pandas as pd
import statistics
import numpy as np
import matplotlib.pyplot as plt

dfBTC = pd.read_csv (r'C:\Users\patel\Desktop\sourcecode\Data-Science-Project\Data\crypto\bitcoinAll_1HR_Cleaned.csv')
dfTweets = pd.read_csv (r'C:\Users\patel\Desktop\sourcecode\Data-Science-Project\Data\tweets\elon_archive_cleaned.csv')


percentChangeList = []
dateList = []
df_filteredElon = dfTweets[dfTweets['crypto_related'] == True]

for date in df_filteredElon['date']:
    row = dfBTC.loc[dfBTC['Date'] == date]
    firstHour = row['rate_low'].iloc[0]
    lastHour = row['rate_high'].iloc[-1]
    difference = (abs(lastHour - firstHour) / firstHour) * 100.0
    if (difference > 3):
        percentChangeList.append(difference)
        dateList.append(date)

    

print("Average price fluctuation from Elon Musk's crpyto related tweets: " + str(sum(percentChangeList) / len(percentChangeList)))

plt.figure(figsize=(30,10))
plt.scatter(dateList,percentChangeList)
plt.xticks(rotation=90)
plt.show()