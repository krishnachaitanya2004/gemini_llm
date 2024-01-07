import os
import google.generativeai as genai
import time

# Google API Key
os.environ["GOOGLE_API_KEY"] = "Your API Key"
api_key = os.environ.get('GOOGLE_API_KEY')
genai.configure()

# Creating the model
model = genai.GenerativeModel('gemini-pro')

# User input
print("-------------------------------Welcome to GenAI - Generative AI for Everyone---------------------------------")
while True:
    query = input("Enter your Query: ")
    print("Generating response...")
    response = model.generate_content(query)
    print(response.text)
    print('\n')
