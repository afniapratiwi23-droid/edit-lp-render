import google.generativeai as genai
import os

API_KEY = "AIzaSyAWBb5d05FYoK7Y6cz0l1r9_OYg9LJyytU"
genai.configure(api_key=API_KEY)

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error listing models: {e}")
