import langchain
import langgraph
import openai


import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)
print(client)