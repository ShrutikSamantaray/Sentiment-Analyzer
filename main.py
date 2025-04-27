import streamlit as st
import openai
from textblob import TextBlob

# Set your OpenAI API key
client = openai.OpenAI(
    api_key="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"
)

def perform_sentiment_analysis(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def display_response(sentiment, response):
    st.markdown(f"**Sentiment:** {sentiment}", unsafe_allow_html=True)
    st.markdown(f"**Response:** {response}", unsafe_allow_html=True)

st.set_page_config(page_title="Product Classification")

st.title("Sentiment Analysis")
st.markdown("---")

query = st.text_area("Enter your text here:")

if st.button("Generate Response"):
    if query:
        with st.spinner("Processing..."):
            senti = perform_sentiment_analysis(query)

            prompt = f"""Classify the following text into product categories and topics: {query}
Return only the category and topic."""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that classifies product-related texts."},
                    {"role": "user", "content": prompt}
                ]
            )

            reply = response.choices[0].message.content
            display_response(senti, reply)
    else:
        st.warning("Please enter some text.")
