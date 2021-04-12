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


df = load_data(type_='groupfitdata')
st.title("GroupFit Dashboard")
	
df2 = df.drop(df.columns[[4,5]], axis=1)
st.write(df2)
totalpushups= df2['How many pushups did you do?'].sum()
st.write("Pushups goal: 300")
st.write("Total Pushups Completed: " + str(totalpushups))
totalpushups= df2['How many miles did you run?'].sum()
st.write("Miles goal: 300")
st.write("Total Miles Completed: " + str(totalpushups))
df3 = df2.copy()
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/11/2021'],'3')
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/10/2021'],'2')
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/9/2021'],'1')
df3.set_index('What day are you logging for?')
st.line_chart(df3)
