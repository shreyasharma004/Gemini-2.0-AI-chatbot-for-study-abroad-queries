# Study Abroad Chatbot

A Streamlit application powered by Google's Gemini AI that provides personalized guidance for study abroad opportunities and college recommendations.

## Setup and Deployment

1. Make sure you have Python 3.8+ installed
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Google Cloud API key:
   - Get your API key from Google Cloud Console
   - Enable the Gemini API in your project
   - Replace the API key in `app.py`

## Running Locally

```bash
streamlit run app.py
```

## Deployment on Streamlit Cloud

1. Push your code to a GitHub repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub repository
4. Deploy the app

## Environment Variables

Make sure to set the following environment variables in your Streamlit Cloud deployment:
- `GOOGLE_API_KEY`: Your Google Cloud API key

## Features

- Personalized study abroad guidance
- University recommendations based on preferences
- Interactive chat interface
- Score-based filtering
- Budget consideration
- Country-specific recommendations

## Note

Always verify the information provided by the chatbot with official sources.

