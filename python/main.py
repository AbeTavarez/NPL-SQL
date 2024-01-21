from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from watcher import *

load_dotenv()
# watcher.watch()

# set api key on openai 

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# test
# chat_completion = client.chat.completions.create(
#    messages=[
#        {
#            "role": "user",
#            "content": "which technologies should i learn in 2024?"
#        }
#    ],
#    model="gpt-3.5-turbo"
# )
# print(chat_completion)
# print(chat_completion[0]['text'])



data_frame = pd.read_csv("sales_data_sample.csv")
print(data_frame)
print(data_frame.groupby('QTR_ID').sum()['SALES'])

# TEMP DB in RAM; can connect to other db instead later
temp_db = create_engine('sqlite:///:memory:', echo=True)


# PUSH Pandas Data Frame --> TEMP DB
# name= db table name;  
data = data_frame.to_sql(name='Sales', con=temp_db)
# print(data)

# Perform SQL queries on TEMP DB with Pandas DF
with temp_db.connect() as conn:
    # makes the connection
    # runs code block
    # result = conn.execute(text("SELECT * from Sales"))
    result = conn.execute(text("SELECT SUM(SALES) From Sales"))
    # auto close connection
    result.all()