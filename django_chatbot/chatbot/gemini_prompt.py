import os
from dotenv import load_dotenv
from pathlib import Path

# dotenv_path = Path().cwd()/'..'/'..'
load_dotenv()


import google.generativeai as genai

GEMINI_API = os.getenv('GEMINI_API')
genai.configure(api_key=GEMINI_API)
model = genai.GenerativeModel('gemini-pro')

def prompt_gemini(input_prompt):
    respone = model.generate_content(input_prompt)
    return respone.text

# print(prompt_gemini('Explain code for submitting form with javascript'))