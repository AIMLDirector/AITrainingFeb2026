from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
# openapikey  = os.getenv("OPENAI_API_KEY")
# print(openapikey)

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

