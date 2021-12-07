import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dogecoinSNL_EDA():

    # put csv file into pandas dataframe
    folder_path = "dogecoin_history_rates_apr21-jul21-SNL.csv"
    df = pd.read_csv(folder_path)
    # seperate the date from the time
    df["date"] = [d.split('T')[0] for d in df["time_period_start"]]
    # drop useless columns
    df.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)

    _, axs = plt.subplots()

    show_every = 4

    # separate ticks so they are not cluttered
    sparse_xticks = [None] * df["date"].shape[0]
    sparse_xticks[::show_every] = df["date"][::show_every]
    # set plot parameters
    axs.set_title("DOGECOIN HIGH VALUES FROM (April - July)", fontsize = 15)
    axs.tick_params(axis = 'x', labelsize = 10)
    axs.set_xlabel('Date', size = 14)
    axs.tick_params(axis = 'y', labelsize =10)
    axs.set_ylabel('Price in $', size = 14)
    axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=90)
    plt.plot( df["date"], df["rate_open"])
    # plot and save figure
    figure = plt.gcf()
    figure.set_size_inches(15,11)
    plt.savefig("Dogecoin_SNL.png", dpi = 600)


    # plt.show()

def dogecoinLIONKING_EDA():

    # put csv file into pandas dataframe
    folder_path = "dogecoin_history_rates_feb21-LionKingMeme.csv"
    df = pd.read_csv(folder_path)
    # seperate the date from the time
    df["date"] = [d.split('T')[0] for d in df["time_period_start"]]
    # drop useless columns
    df.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)

    _, axs = plt.subplots()

    show_every = 4
    # sparse ticks so they are not cluttered
    sparse_xticks = [None] * df["date"].shape[0]
    sparse_xticks[::show_every] = df["date"][::show_every]
    # set plot parameters
    axs.set_title("DOGECOIN HIGH VALUES (February - April)", fontsize = 15)
    axs.tick_params(axis = 'x', labelsize = 10)
    axs.set_xlabel('Date', size = 14)
    axs.tick_params(axis = 'y', labelsize =10)
    axs.set_ylabel('Price in $', size = 14)
    axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=90)
    plt.plot( df["date"], df["rate_open"])
    # plot and save EDA
    figure = plt.gcf()
    figure.set_size_inches(15,11)
    plt.savefig("Dogecoin_LionKing.png", dpi = 600)


    # plt.show()

def dogecoinMay20():

    # put csv file into pandas dataframe
    folder_path = "dogecoin_history_rates.csv"
    df = pd.read_csv(folder_path)
    # split the date from the time
    df["date"] = [d.split('T')[0] for d in df["time_period_start"]]
    # drop useless columns
    df.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)

    _, axs = plt.subplots()

    show_every = 2
    # sparse ticks so they are not cluttered
    sparse_xticks = [None] * df["date"].shape[0]
    sparse_xticks[::show_every] = df["date"][::show_every]
    # set plot parameters
    axs.set_title("DOGECOIN HIGH VALUES (May)", fontsize = 15)
    axs.tick_params(axis = 'x', labelsize = 10)
    axs.set_xlabel('Date', size = 14)
    axs.tick_params(axis = 'y', labelsize =10)
    axs.set_ylabel('Price in $', size = 14)
    axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=45)
    plt.plot( df["date"], df["rate_open"])
    # plot and save EDA
    figure = plt.gcf()
    figure.set_size_inches(15,11)
    plt.savefig("Dogecoin_May2020.png", dpi = 600)


    # plt.show()

def bitcoinJan21():

    # put csv file into pandas dataframe
    folder_path = "bitcoin_history_rates_jan21-apr21.csv"
    df = pd.read_csv(folder_path)
    # separate date from time
    df["date"] = [d.split('T')[0] for d in df["time_period_start"]]
    # drop useless columns
    df.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)

    _, axs = plt.subplots()

    show_every = 4
    # sparse ticks so they are not cluttered
    sparse_xticks = [None] * df["date"].shape[0]
    sparse_xticks[::show_every] = df["date"][::show_every]
    # set plot parameters
    axs.set_title("BITCOIN HIGH VALUES (January - April)", fontsize = 15)
    axs.tick_params(axis = 'x', labelsize = 10)
    axs.set_xlabel('Date', size = 14)
    axs.tick_params(axis = 'y', labelsize =10)
    axs.set_ylabel('Price in $', size = 14)
    axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=90)
    plt.plot( df["date"], df["rate_open"])
    # plot and save EDA
    figure = plt.gcf()
    figure.set_size_inches(15,11)
    plt.savefig("Bitcoin_January-April2021.png", dpi = 600)


    # plt.show()

def bitcoinApr21():

    # put csv file into pandas dataframe
    folder_path = "bitcoin_history_rates_apr21-jul21.csv"
    df = pd.read_csv(folder_path)
    # seperate date from time
    df["date"] = [d.split('T')[0] for d in df["time_period_start"]]
    # drop useless columns
    df.drop(columns=["time_period_start", "time_period_end", "time_open", "time_close"], inplace=True)

    _, axs = plt.subplots()

    show_every = 4
    # sparse ticks so they are not cluttered
    sparse_xticks = [None] * df["date"].shape[0]
    sparse_xticks[::show_every] = df["date"][::show_every]
    # set plot parameters
    axs.set_title("BITCOIN HIGH VALUES (April - July)", fontsize = 15)
    axs.tick_params(axis = 'x', labelsize = 10)
    axs.set_xlabel('Date', size = 14)
    axs.tick_params(axis = 'y', labelsize =10)
    axs.set_ylabel('Price in $', size = 14)
    axs.set_xticklabels(sparse_xticks, fontsize=10 ,rotation=90)
    plt.plot( df["date"], df["rate_open"])
    # plot and save EDA
    figure = plt.gcf()
    figure.set_size_inches(15,11)
    plt.savefig("Bitcoin_April-July2021.png", dpi = 600)

    # plt.show()

# run eda generation
def main():
    dogecoinMay20()
    dogecoinLIONKING_EDA()
    dogecoinSNL_EDA()
    bitcoinJan21()
    bitcoinApr21()

main()