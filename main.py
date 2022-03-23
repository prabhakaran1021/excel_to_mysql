import os

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from config import DATABASE

def load_files():
    from os import listdir
    from os.path import isfile, join
    mypath='input_files'
    onlyfiles = [mypath+'/'+f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
files=load_files()
engine = create_engine('mysql+mysqlconnector://'+DATABASE.USER+':'+DATABASE.PASSWORD+'@'+DATABASE.HOST+':'+DATABASE.PORT+'/'+DATABASE.NAME+'', echo=False)
for file in files:
    file_type=file.split('.')[-1]
    df=pd.DataFrame()
    if file_type=='csv':
        df=pd.read_csv(file)
    elif file_type=='xlsx':
        df=pd.read_excel(file,engine='openpyxl')
    df.to_sql(name=file, con=engine, if_exists = 'append', index=False)
