from openai import OpenAI
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

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