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
yf.pdr_override()

"""
# Stock Viewer
"""
current = datetime.date.today();

st.header("Stock Viewer")
symbol = st.text_input("Stock Symbol", "GME")
myTicker = yf.Ticker(symbol)
data = myTicker.history(period='1d',start='2020-1-1',end = '2021-2-25')
st.dataframe(data)
st.write("Closing Price")
st.line_chart(data.Close)
st.write("High Price")
st.line_chart(data.High)
st.write("Low Price")
st.line_chart(data.Low)
st.write("Volume")
st.line_chart(data.Volume)
