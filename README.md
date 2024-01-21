# Natural Language to SQL Query

This program uses Pandas to convert a tabular source of data into a SQL database.
Then takes the user prompt and combines the prompt with the SQL data base info, and
sends the prompt to OpenAI API using a Completion model to generate the SQL query.

Note: The Text Completion model is also very good at completing actual code.

 - Text Completion:
    Optimized for completing with natural language.

 - Code Completion:
    Optimized for completing with actual executable code.

### OpenAI Model

At this time we're using the "gtp-3.5-turbo" model.

Link: <a>https://platform.openai.com/docs/model-index-for-reserchers</a>

Previous Models:
    - text-davinci-002
    - code-davinci-002
    - text-davinci-003

### Text Completion API Parameters

    - Model: The OpenAI Model
    - Prompt: 
    - Temperature:
    - Max Tokens:
    - Top P:
    - N:
    - Frequency Penalty:
    - Presence Penalty:

## Notes

### Steps
 1. Setup OpenAI API Key.
 2. Read CSV file.
 3. Create an in-memory SQL database and load the csv data.
 4. Work on the Prompt Engineering using the user prompt.
 5. Pass the created prompt to the OpenAI API and the configuration.
 6. Handle the response from OpenAI API, to just get the actual SQL query.
 7. Run the final SQL Query on the database