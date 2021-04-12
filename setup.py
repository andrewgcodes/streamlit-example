import gspread
import oauth2client
import pandas
import time
import streamlit
import altair


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('groupfit-008ebd4002c3.json', scope) #Change to your downloaded JSON file name
client = gspread.authorize(creds)

spreadsheets = ['GroupFit']

def main(spreadsheets):

	df = pd.DataFrame()

	for spreadsheet in spreadsheets:
		#Open the Spreadsheet
		sh = client.open(spreadsheet)

		#Get all values in the first worksheet
		worksheet = sh.get_worksheet(0)
		data = worksheet.get_all_values()

		#Save the data inside the temporary pandas dataframe
		df_temp = pd.DataFrame(columns = [i for i in range(len(data[0]))])
		for i in range(1,len(data)):
			df_temp.loc[len(df_temp)] = data[i]
        _type = 'groupfitdata'
