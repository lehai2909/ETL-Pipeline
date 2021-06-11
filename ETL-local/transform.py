import pandas as pd


def process_log(): 
	df = pd.read_csv("log/log-20210506.csv")
	df['parsed_time'] = pd.to_datetime(df.timestamp)
	df_new = df[['insertId','parsed_time','jsonPayload.message']]
	df_new = df_new.rename(columns={"insertId": "Id", "jsonPayload.message": "message"})
	return df_new





	

	
