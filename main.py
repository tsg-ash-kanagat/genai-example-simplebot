import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import certifi
import ssl

ssl_context = ssl.create_default_context(cafile=certifi.where())
messages = []
system_message = input("What type of chatbot you want me to be?")
messages.append({"role": "system", "content": system_message})

print("Alright! I am ready to be your friendly chatbot" + "\n" + "You can now type your messages.")
message = input("")
messages.append({"role": "user", "content": message})

response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=messages)

reply = response.choices[0].message.content
print(reply)
