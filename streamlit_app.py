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


def main():


	df = load_data(type_='groupfitdata')

	st.title("{} GroupFit Dashboard".format(page))
	

	st.markdown("> Chart in this page shows the comparison of number of respondents who is tested and not tested")
	st.write(df)
	

