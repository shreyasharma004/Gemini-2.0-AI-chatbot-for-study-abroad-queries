import streamlit as st
import google.generativeai as genai
from google.api_core import exceptions
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API Key
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("""
    ⚠️ **API Key Not Found**
    
    Please make sure you have:
    1. Created a `.env` file in your project root
    2. Added your API key to the `.env` file:
       ```
       GOOGLE_API_KEY=your-api-key-here
       ```
    3. Installed python-dotenv:
       ```
       pip install python-dotenv
       ```
    """)
    st.stop()

genai.configure(api_key=API_KEY)

# Function to interact with Gemini AI
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)
        return response.text
    except exceptions.NotFound as e:
        st.error(f"Error: The model was not found. Please check your API key and model name. Error: {str(e)}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit UI
st.set_page_config(page_title="Study Abroad Chatbot", page_icon="🎓", layout="wide")

# Header
st.title("🎓 Study Abroad Chatbot - Powered by Gemini AI")
st.write("Get personalized guidance on study abroad opportunities and college recommendations.")

# User input fields
st.sidebar.header("📌 Your Preferences")
score = st.sidebar.number_input("Enter Your Score (GPA/Percentage/SAT/IELTS/TOEFL)", min_value=0.0, step=0.1)
field_of_study = st.sidebar.text_input("Enter Your Preferred Field of Study", placeholder="Example: Computer Science")
preferred_country = st.sidebar.text_input("Enter Preferred Country", placeholder="Example: USA, Canada, UK")
budget = st.sidebar.text_input("Enter Budget Range (Optional)", placeholder="Example: $30,000 - $50,000 per year")

# Chat interface
st.subheader("💬 Chat with the AI")
user_input = st.text_input("Ask about study abroad, scholarships, or universities!")

# Generate response
if st.button("Get Advice"):
    if user_input.strip() == "":
        st.warning("Please enter a question to proceed.")
    else:
        response = get_gemini_response(user_input)
        if response:
            st.write("🤖 **Chatbot:**", response)

# College recommendation based on input
if st.sidebar.button("🔍 Find Best Colleges"):
    if not score or not field_of_study or not preferred_country:
        st.sidebar.warning("Please fill in all required fields.")
    else:
        query = f"Suggest top universities in {preferred_country} for {field_of_study} students with a score of {score}. Consider budget range: {budget if budget else 'Not specified'}."
        recommendations = get_gemini_response(query)
        if recommendations:
            st.sidebar.subheader("🏆 Recommended Universities")
            st.sidebar.write(recommendations)

# Footer
st.markdown("---")
st.markdown("💡 *This chatbot uses Google Gemini AI to provide study abroad advice. Always verify information from official sources.*")
