# Build a Recommender Systems...
import streamlit as st
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Import the Local Environment
from dotenv import load_dotenv
import os
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# Design the Page... streamlit run app.py
#headers = {"authorization":st.secrets["GOOGLE-API-KEY"],
           #"content-type":"application/json"}

st.title("🆒Movie Recommender Systems...")
user_input = st.text_input("Enter the Movie title, genre or keyword")

# Prompt Template
demo_template = '''Based on {user_input} provide Movie Recommendations"'''
template = PromptTemplate(input_variables=["user_input"], 
                          template=demo_template)

# Google Gemini Model..
llm = ChatGoogleGenerativeAI(model = "gemini-pro", 
                             api_key=os.getenv("GOOGLE-API-KEY"))

if user_input:
    prompt = template.format(user_input = user_input)
    recommendations = llm.predict(text=prompt)
    st.write(f"Recommendations for you:\n {recommendations}")
else:
    st.write(" ")


