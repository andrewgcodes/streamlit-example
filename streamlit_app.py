from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import datetime 
import pandas as pd
import requests
import matplotlib


			
def load_data(type_):
	df = pd.read_csv('fitnessdata.csv')

	return df


df = load_data(type_='groupfitdata')
st.title("FTC Team 14235 GroupFit Dashboard")
st.image("shine.png")
df2 = df.drop(df.columns[[4,5]], axis=1)
st.write(df2)
totalpushups= df2['How many pushups did you do?'].sum()
st.write("Group Pushup goal: 300")
st.write("Total Pushups Completed: " + str(totalpushups))
totalpushups= df2['How many miles did you run?'].sum()
st.write("Group Mile goal: 50")
st.write("Total Miles Completed: " + str(totalpushups))
df3 = df2.copy()
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/11/2021'],'3')
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/10/2021'],'2')
df3['What day are you logging for?'] = df3['What day are you logging for?'].replace(['4/9/2021'],'1')
#df3= df3.set_index('What day are you logging for?')
#plt.plot('What day are you logging for?'
#st.line_chart(df3)
try:
	user_input = st.multiselect('Search stats by username',df.iloc[:, 0])
	miletotal = 0
	mask = df2['What\'s your username?'].values == user_input

	df4 = df2[mask]
	miletotal = df4['How many miles did you run?'].sum()
	pushuptotal = df4['How many pushups did you do?'].sum()
	st.write(str(user_input) + " has done " + str(pushuptotal) + " pushups!")

	st.write(str(user_input) + " has run " + str(miletotal) + " miles!")
except:
	pass
