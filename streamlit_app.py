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

st.header("Stock Viewer")
symbol = st.text_input("Second Stock Symbol", "GME")
myTicker = yf.Ticker(symbol)
data = myTicker.history(period='1d',start='2020-1-1',end = '2021-2-25')
data['Stock'] = symbol
symbol2 = st.text_input("Second Stock Symbol", "TSLA")
myTicker2 = yf.Ticker(symbol2)
data2 = myTicker2.history(period='1d',start='2020-1-1',end = '2021-2-25')
data2['Stock'] = symbol2
ax = data.Close.plot()
data2.Close.plot(ax=ax)
st.pyplot(ax)
st.dataframe(data)
st.write("Closing Price")
st.line_chart(data.Close)
st.write("High Price")
st.line_chart(data.High)
st.write("Low Price")
st.line_chart(data.Low)
st.write("Volume")
st.line_chart(data.Volume)
