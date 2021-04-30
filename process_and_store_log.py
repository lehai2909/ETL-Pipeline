import pandas as pd

with open('log/log1.json','r') as file:
	events = json.load(file)

for event in events:
	print(event['insertId'])
	print(event['timestamp'])
	print(event['logName'])
