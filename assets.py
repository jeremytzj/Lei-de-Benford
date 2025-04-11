# Coleta dados dos 50 ativos mais negociados no Brasil (IBrX 50)


import yfinance as yf
import pandas as pd

# Lê a composiçção do IBrX 50 
df = pd.read_csv("data/compos.csv", encoding='ISO-8859-1')
tickers = [str(i)+".SA" for i in df['code']]

data = yf.download(tickers, start="2021-03-01", end="2025-01-01", interval="1mo")

# joga esses dados para uma planilha em excel
data.to_excel("data/data.xlsx")