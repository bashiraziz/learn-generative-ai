from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
#import os
load_dotenv(find_dotenv()) # read local .env file

import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path("./.env"))
print(os.getenv("OPENAI_API_KEY"))

# client = OpenAI()

# stream = client.chat.completions.create(
#     model="gpt-3.5-turbo-1106",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )
print(os.getenv("OPENAI_API_KEY"))
# for part in stream:
#     print(part.choices[0].delta.content or "")