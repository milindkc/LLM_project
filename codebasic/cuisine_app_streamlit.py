import streamlit as st
# from langchain.chat_models import ChatOpenAI  #Do not use this import
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("api_key")

# Initialize the OpenAI LLM
llm = ChatOpenAI(api_key = api_key ,model_name="gpt-4", temperature=0.7)

# Streamlit UI
st.title("🍽️ Cuisine-Based Dish Generator")

# Cuisine selection
cuisines = ["Italian", "Mexican", "Indian", "Chinese", "French", "Japanese", "Thai", "Greek", "Spanish", "Mediterranean"]
selected_cuisine = st.selectbox("Select a cuisine:", cuisines)

# Generate dishes
if st.button("Get 10 Dishes"):
    prompt = f"List 10 famous dishes from {selected_cuisine} cuisine."
    response = llm.invoke([HumanMessage(content=prompt)])
    
    dishes = response.content.split("\n")  # Split response into a list
    st.subheader(f"🍽️ 10 Popular {selected_cuisine} Dishes")
    
    for i, dish in enumerate(dishes, start=1):
        st.write(f"{i}. {dish}")

"Run the app by executing `streamlit run cuisine_app_streamlit.py` in the terminal."