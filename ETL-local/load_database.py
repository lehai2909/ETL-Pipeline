import mysql.connector
from datetime import date, datetime, timedelta
from transform import process_log


DB_NAME = 'pipeline'
df = process_log()

def establish_connection():
	cnx = mysql.connector.connect(user='lehai', password='iambawmim',
                              host='localhost')

	cursor = cnx.cursor()

	#create database if you don't have one already
	#cursor.execute("create database {} default character set 'utf8'".format(DB_NAME)
	cursor.execute("use {}".format(DB_NAME))
	return cnx, cursor

def create_table(cursor):
	#define command to create table `logs` in chosen database
	CREATE_TABLE = """
		create table `logs` (
		insertId varchar(50) not null,
		timestamp timestamp not null,
		message varchar(200) not null,
		primary key (`insertId`)) 
		"""
	cursor.execute(CREATE_TABLE)

def update_data(cursor,dataframe):
	#Add new entries to table
	for i in range(len(dataframe)):
		DATA = (df.loc[i,'Id'],df.loc[i,'parsed_time'],df.loc[i,'message'])
		ADD_ENTRY =  """
			insert into logs
			(insertId, timestamp, message)
			values (%s,%s,%s)
			"""
		cursor.execute(ADD_ENTRY, DATA)
	cnx.commit()

if __name__ == "__main__":
	cnx, cursor = establish_connection()
	create_table(cursor)
	update_data(cursor,df)
	cnx.close()
