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
# Random Stock
"""
current = datetime.date.today();

st.header("Random Stock Generator")
stock = yf.Ticker("GME")
myTicker = yf.Ticker(stock)
data = myTicker.history(period='1d',start='2020-1-1',end = '2021-2-25')
st.dataframe(data)
st.write("Closing Price for: GME")
st.line_chart(data.Close)
st.write("Volume for: GME")
st.line_chart(data.Volume)
