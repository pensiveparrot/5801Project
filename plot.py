####################
# Import dependencies
####################
import yfinance as yf
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pytest
from datetime import datetime


START_DATE = '2000-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))

#STOCK = 'AMZN'
#STOCK2 = 'GOOGL'
STOCK = input("Enter Stock 1:")
STOCK2 = input("Enter Stock 2:")
# makes a basic plot that compares two stocks.


def create_plt(stock_data, ticker, stock_data2, ticker2):
    plt.style.use('dark_background')
    stats = get_stats(stock_data)
    stats2 = get_stats(stock_data2)
    plt.subplots(figsize=(12, 8))
    plt.plot(stock_data, label=ticker)
    plt.plot(stats['short_rolling'], label='20 day rolling mean')
    plt.plot(stats['long_rolling'], label='200 day rolling mean')
    plt.plot(stock_data2, label=ticker2)
    plt.plot(stats2['short_rolling'], label='20 day rolling mean')
    plt.plot(stats2['long_rolling'], label='200 day rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adj Close (p)')
    plt.legend()
    plt.title('Stock prices over time.')

    plt.show()


def get_stats(stock_data):
    return {
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling': stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }


# cleans up the data


def clean_data(stock_data, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = stock_data[col].reindex(weekdays)
    return clean_data.fillna(method='ffill')

# grabs the open,close,low,high,volume,and the adjusted close for the stock


def get_data(ticker, ticker2):
    try:
        stock_data = data.DataReader(ticker,
                                     'yahoo',
                                     START_DATE,
                                     END_DATE)
        stock_data2 = data.DataReader(ticker2,
                                      'yahoo',
                                      START_DATE,
                                      END_DATE)
        adj_close = clean_data(stock_data, 'Adj Close')
        adj_close2 = clean_data(stock_data2, 'Adj Close')
        create_plt(adj_close, ticker, adj_close2, ticker2)
    except RemoteDataError:
        print('No data found for {t}'.format(t=ticker))


# get_data(STOCK, STOCK2)
print(get_data(STOCK, STOCK2))
