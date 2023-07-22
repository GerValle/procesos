#%%

import yfinance as yf

symbols = ['AAPL','F', 'C']

tickers = yf.Tickers(symbols)

dias = 500

h = tickers.history(period=f"{dias}d")['Close']

#%%
rendimientos = h.pct_change().dropna()

#%%

import sqlite3 as lite

from pathlib import Path

mi_base = Path.cwd() / 'mi_base.sqlite'

conn = lite.connect(mi_base)



conn.close()






# %%
