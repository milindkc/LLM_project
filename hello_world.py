from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure the correct environment variable is set
api_key = os.getenv("api_key")

# Initialize OpenAI model
llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-4", temperature=0.7)

# Invoke the model
response = llm.predict("what is the capital of india")
print(response)
