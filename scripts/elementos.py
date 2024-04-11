#%%

import yfinance as yf
import sqlite3 as lite
from pathlib import Path
import numpy as np


symbols = ['AAPL','F', 'C']

tickers = yf.Tickers(symbols)

dias = 500

h = tickers.history(period=f"{dias}d").Close

rendimientos = np.log(h).diff().dropna()


mi_base = Path('/home/ger/Documents/unam/procesos/scripts/mi_base.sqlite')

conn = lite.connect(mi_base)

h.to_sql('historico', conn, if_exists='replace')
rendimientos.to_sql('rendimientos', conn, if_exists='replace')

conn.close()






# %%
