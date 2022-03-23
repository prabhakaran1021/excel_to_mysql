import os
from urllib.parse import quote_plus

import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from config import DATABASE
import config
def load_files():
    from os import listdir
    from os.path import isfile, join
    mypath='input_files'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    out_files=[]
    for files in onlyfiles:
        if files[0]=='.':
            onlyfiles.remove(files)
        else:
            files=mypath+'/'+files
            out_files.append(files)
    return out_files
files=load_files()
engine = create_engine('mysql+mysqlconnector://'+DATABASE.USER+':'+quote_plus(DATABASE.PASSWORD)+'@'+DATABASE.HOST+':'+DATABASE.PORT+'/'+DATABASE.NAME+'', echo=False)
for file,table_name in files,config.table_names:
    file_type=file.split('.')[-1]
    df=pd.DataFrame()
    if file_type=='csv':
        df=pd.read_csv(file)
    elif file_type=='xlsx':
        df=pd.read_excel(file,engine='openpyxl')
    df.to_sql(name=table_name, con=engine, if_exists = 'append', index=False)
