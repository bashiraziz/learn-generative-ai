from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
print(load_dotenv(find_dotenv())) # read local .env file

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")