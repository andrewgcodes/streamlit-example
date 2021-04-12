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


			
def load_data(type_):
	df = pd.read_csv('fitnessdata.csv')

	return df
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



df = load_data(type_='groupfitdata')
st.title("GroupFit Dashboard")
	
df2 = df.drop(df.columns[[0,4,5]], axis=1)
st.write(df2)
totalpushups= df2[[1]].sum(I)
st.write("Total Pushups Completed: " + totalpushups)
