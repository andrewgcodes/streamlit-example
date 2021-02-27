from collections import namedtuple
import altair as alt
import math
import pandas as pd
import yfinance as yf
import streamlit as st
import datetime 
import ta
import pandas as pd
import requests
import matplotlib
yf.pdr_override()

"""
# Stock Viewer
"""
current = datetime.date.today();

darkmode = """
<style>
body {
  background-color: black;
  color: white;
}
</style>
"""
buffer = st.checkbox('Dark Mode')
if buffer:
    st.markdown(darkmode,unsafe_allow_html=True)
st.write("First stock symbol")
symbol = st.text_input("", "GME")
myTicker = yf.Ticker(symbol)
data = myTicker.history(period='1d',start='2020-1-1',end = '2021-2-25')
st.write("Second stock symbol")
symbol2 = st.text_input("", "TSLA")
myTicker2 = yf.Ticker(symbol2)
data2 = myTicker2.history(period='1d',start='2020-1-1',end = '2021-2-25')


data3 = [data["Close"], data2["Close"]]

headers = [symbol, symbol2]

df3 = pd.concat(data3, axis=1, keys=headers)
st.write("Closing Price")
st.line_chart(df3)

