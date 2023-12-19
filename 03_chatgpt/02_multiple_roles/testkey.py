import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path("./.env"))
print(os.getenv("OPENAI_API_KEY"))