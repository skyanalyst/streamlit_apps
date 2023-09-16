import streamlit as st
import yfinance as yf
import pandas as pd

st.write("""
# Simple Stock Price App
         """)
tickersymbol = '^NSEI'
tickerdata = yf.ticker(tickersymbol)
tickerdf = tickerdata.history(period ='1m', start = )