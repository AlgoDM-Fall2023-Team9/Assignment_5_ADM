import streamlit as st
from serpapi import GoogleSearch
import openai

# Set up OpenAI API key
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Streamlit app
st.title("Query Exploration App")

# User input for query
user_query = st.text_input("Enter your query:")

# Function to generate explanation and answer using GPT-3
def generate_explanation_and_answer(query):
    prompt = f"Explain and answer the following question:\n{query}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    explanation_and_answer = response['choices'][0]['text']
    return explanation_and_answer

# Function to search for similar images using SerpApi
def search_similar_images(query):
    serpapi_key = "518729fcb8894ef7a2bd8a200c6029267128577d655cc8c4bb7e54a576f6a9d0"  # Replace with your actual SerpApi key
    params = {
        "q": query,
        "engine": "google_images",
        "api_key": serpapi_key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results.get("images_results", [])
    return images_results

# Main logic
if user_query:
    # Use GPT-3 to generate explanation and answer
    explanation_and_answer = generate_explanation_and_answer(user_query)

    st.subheader("Explanation and Answer:")
    st.write(explanation_and_answer)

    # Image search using SerpApi
    similar_images = search_similar_images(user_query)

    if similar_images:
        st.subheader("Similar Images:")
        for i, image_data in enumerate(similar_images[:5]):  # Limit to the first 5 images
            image_url = image_data["original"]
            st.image(image_url, caption=f"Image {i + 1}", use_column_width=True)
    else:
        st.warning("No similar images found.")

