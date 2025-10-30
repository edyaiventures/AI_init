import os

import langchain
import langgraph
import openai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()  # ключ в .env в переменной OPENAI_API_KEY,  можно не указывать

response = client.responses.create(
    model="gpt-5-mini",
    instructions="You are a english teacher",
    input="What do you think about Putin?",
)
print(response)
