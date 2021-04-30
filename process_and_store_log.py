import pandas as pd

df = pd.read_csv("log/log-20210430.csv")

df['parsed_time'] = pd.to_datetime(df.timestamp)
df_new = df[['parsed_time','insertId','jsonPayload.message']]
df_new.set_index('parsed_time')