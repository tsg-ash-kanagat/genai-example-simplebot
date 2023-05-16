import os
import openai

# openai.organization = "org-Edw9Vvm6IxAT4DmEXFl12qii"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
