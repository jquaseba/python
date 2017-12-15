# Stock API
import pandas as pd  
import datetime

from pandas_datareader import data, wb

symbol = 'GBTC'  
d = data.DataReader(symbol, "yahoo", '2016-06-01')

print(d[:25]['Adj Close'])