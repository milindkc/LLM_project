""" This file demonstrates how to chain multiple components together. """

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables 
load_dotenv()

# Ensure the correct environment variable is set
api_key = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI model
llm = ChatOpenAI(openai_api_key=api_key, model="gpt-4", temperature=0.7)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are best cook in town."),
    ("user", "{input}")
])

chain = prompt | llm 
chain_response = chain.invoke({"input": "how to create lemonade?"})
print(chain_response.content)



