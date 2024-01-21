from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from watcher import *

# load environment variables
load_dotenv()


# ###### set api key on openai  client ############
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)


# ####### Read data set with pandas ###########
data_frame = pd.read_csv("sales_data_sample.csv")
print(data_frame)
# print(data_frame.groupby('QTR_ID').sum()['SALES'])

# ######### Create TEMP DB in RAM #################
temp_db = create_engine('sqlite:///:memory:', echo=True)


# ####### PUSH Pandas Data Frame --> TEMP DB #########
# name= db table name;  
data = data_frame.to_sql(name='Sales', con=temp_db)
# print(data)

# Perform SQL queries on TEMP DB with Pandas DF
# with temp_db.connect() as conn:
    # makes the connection
    # runs code block
    # result = conn.execute(text("SELECT * from Sales"))
    # result = conn.execute(text("select * from Sales"))
    ## auto close connection
    # for row in result:
    #     print(row)
    #result.all()
    
# function: return a table definition
# here we can add multiple db tables, not just Sales
def create_table_definition(df):
    prompt = """### sqlite SQL table, with it properties
    #
    # Sales({})
    #
    """.format(",".join(str(col) for col in df.columns))
    
    return prompt

# takes in prompt from user
def prompt_input():
    nlp_text = input("Enter the info you want: ")
    return nlp_text


# combine the data frame and the user prompt
def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_string = f"### A query to answer: {query_prompt}\nSELECT"
    return definition+query_string


# gets user prompt
nlp_text = prompt_input()
# combine data frame with user prompt
result = combine_prompts(data_frame, nlp_text)
print(result)

# OpenAI API Call with Prompt
completion = client.chat.completions.create(
   messages=[
       {
           "role": "user",
           "content": combine_prompts(data_frame, nlp_text)
       }
   ],
   model="gpt-3.5-turbo",
   temperature=0,
   max_tokens=150,
   top_p=1.0,
   frequency_penalty=0,
   presence_penalty=0,
   stop=['#', ';']
)
print(completion.choices[0].message.content)
# print(completion.choices[0].message.content)
# p[0].message.contentrint(chat_completion[0]['text'])

# Creates query with API completion response 
def handle_completion(completion):
    query = completion.choices[0].message.content 
    # if query.startswith(" "):
    query = 'SELECT '+query 
    return query

with temp_db.connect() as conn:
    print('QUERY: ' + handle_completion(completion))
    result = conn.execute(text(handle_completion(completion)))
    for row in result:
        print(row)
    # result.all()