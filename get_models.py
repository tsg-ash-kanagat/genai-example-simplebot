import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# openai.organization = "org-Edw9Vvm6IxAT4DmEXFl12qii"
print(client.models.list())
