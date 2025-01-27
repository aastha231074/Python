# # yfinance is a library used to interactwith Yahoo Finance to fetch financial data for stocks, indices, cryptocurrencies and other financial instruments 
import yfinance as yf 
import streamlit as st
import pandas as pd

# Written as a markdown language '#' represent Heading 1

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google
         """)

ticker = yf.Ticker('GOOGL')
tickerDf = ticker.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# streamlit run main.py