from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ensure the correct environment variable is set
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
llm = ChatOpenAI(openai_api_key=api_key, model="gpt-4", temperature=0.7)

# Invoke the model
response = llm.invoke("what is the capital of india")
print(response.content)
