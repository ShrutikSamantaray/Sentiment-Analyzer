import streamlit as st
import google.generativeai as genai
from textblob import TextBlob

# Configure the GenAI API key
GOOGLE_API_KEY = "AIzaSyDU9viU1R3P1sDXO-xYznFMgPlEt7bp53Q"
genai.configure(api_key=GOOGLE_API_KEY)

# Create a GenerativeModel instance
model = genai.GenerativeModel('gemini-pro')

def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Function to display the response with improved styling
def display_response(response):
    st.markdown(f"**Sentiment:** {senti}",unsafe_allow_html=True)
    st.markdown(f" {response}",unsafe_allow_html=True)
    #st.info(f"### {response}")

# Streamlit app

st.set_page_config(page_title="Product Classification", page_icon="https://i2.wp.com/e7.pngegg.com/pngimages/357/433/png-clipart-computer-icons-website-web-design-logo.png")





page_bg_img = """
<style>



[data-testid="stAppViewContainer"] {
background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcwHTGllKkwiTOpzwX-TcSyDW4AZj67t3i1VbJ5aGIMX12vUcjSJ0eraLuJsMDMkw-PfL6A6RRpcxX-O2Z3-mOFo3Y9XvPP8KlJqinKEgjSMfV7Gnk5YANpnT2FZe4VYPNAWqjUaHc8_at/w640-h360-rw/black-wallpaper-pc-heroscreen.cc-4k.png");
background-size: cover;
background-repeat: no-repeat;

}


</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Sentiment Analysis & Product Classification")
st.markdown("---")

# User input
categories="[Package, Delivery, Built Quality, Customer Service, Primary functionality]"
prompt= '''You are given three tasks: 
category = "[Home Appliance, Electronics, Clothing, Personal Care, Healthcare ]"
1) Classify the given text into only and only these category: {category}. Just return one word single response per sentence from the category mentioned above
2) Classify them into specific products. 
Topic = "[Package, Delivery, Product Quality, Customer Service, Primary functionality]"
3) Classify the following sentences into only and only these Topics: {Topic}. Just return one word single response per sentence from the Topic mentioned above
Just return one-word answer in a new lines with its title for each task with no explanations.
The text is :'''

query = st.text_area("Enter your text here:")

# Generate response
if st.button("Generate Response"):
    if query:
        with st.spinner("Processing..."):
            senti=perform_sentiment_analysis(query)
            response = model.generate_content(prompt + query).text
            display_response(response)
    else:
        st.warning("Please enter some text.")
