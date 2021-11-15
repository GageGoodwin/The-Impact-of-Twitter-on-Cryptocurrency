import twint
import pandas as pd
import os
from os.path import exists

# Configure
c = twint.Config()
c.Username = "elonmusk"
c.Limit = 200
c.Until = '2021-11-15 12:00:00'
c.Lang = "en"
c.Filter_retweets = True
c.Store_csv = True
c.Output = "1.csv"
c.Hide_output = True
twint.run.Search(c)

if(exists('1.csv')):
    i = 2
    while i < 250:
        if not (exists('{num}.csv'.format(num = (i - 1)))):
            i = i -1
        else:
            df = pd.read_csv ('{num}.csv'.format(num = str(i - 1)))
            date = df['date'].iloc[-1] + " " + df['time'].iloc[-1]
            # Configure
            c = twint.Config()
            c.Username = "elonmusk"
            c.Limit = 200
            # c.Since = '2009-01-01 12:35:33'
            c.Until = str(date)
            c.Lang = "en"
            c.Filter_retweets = True
            c.Store_csv = True
            c.Output = str((i)) + ".csv"
            c.Hide_output = True
            twint.run.Search(c)
            i = i + 1

fout=open("elon_archive.csv","a",encoding="utf8")
# first file:
for line in open("1.csv",encoding="utf8"):
    fout.write(line)
# now the rest:
for num in range(2,250):
    f = open(str(num)+".csv","r",encoding="utf8")
    f.__next__() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()


for x in range(1,250):
    file = '{num}.csv'.format(num = (x))
    if (exists(file)):
        os.remove(file)