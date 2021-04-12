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

df3 = df2.drop(df2.columns[[1]],axis=1)
st.line_chart(df3)
