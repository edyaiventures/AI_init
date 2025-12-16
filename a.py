from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


response = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="cedar",
    input="Yaroslav is my friend, but i suspect he is gay. He used to dream of so-called 'Black handsome'",
    instructions="speak with  russian accent. Style- like Silvester Stallone",
)
print(response)

response.write_to_file("stallone.mp3")