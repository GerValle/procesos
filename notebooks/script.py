def saludo():
    print("Hola mundo")

if __name__ == "__main__":
    saludo()

#%%
    
import numpy as np
import yfinance as yf
import pyperclip

symbol = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META']


ticker = yf.Tickers(symbol)

data = ticker.history(period='501d').Close

rendimientos = np.log(data).diff().dropna()

df_str = rendimientos.to_csv(index=False, sep='\t')

# Copy string to clipboard
pyperclip.copy(df_str)

#rendimientos.to_clipboard()




# %%
