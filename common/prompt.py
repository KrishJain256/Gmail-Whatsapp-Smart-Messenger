import openai
import os
openai.api_key = os.environ.get("OPENAI_API_TOKEN", "")

def prompt(user_query):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_query}]
    )

    # Get the assistant's reply from the API response
    return response['choices'][0]['message']['content']

