import streamlit as st
import google.generativeai as genai

# Configure Gemini API Key
API_KEY = "AIzaSyACsFezbMnKTgDd1j096QjFA3vLvoEON0M"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Function to interact with Gemini AI
def get_gemini_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text

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
        st.write("🤖 **Chatbot:**", response)

# College recommendation based on input
if st.sidebar.button("🔍 Find Best Colleges"):
    if not score or not field_of_study or not preferred_country:
        st.sidebar.warning("Please fill in all required fields.")
    else:
        query = f"Suggest top universities in {preferred_country} for {field_of_study} students with a score of {score}. Consider budget range: {budget if budget else 'Not specified'}."
        recommendations = get_gemini_response(query)
        st.sidebar.subheader("🏆 Recommended Universities")
        st.sidebar.write(recommendations)

# Footer
st.markdown("---")
st.markdown("💡 *This chatbot uses Google Gemini AI to provide study abroad advice. Always verify information from official sources.*")
