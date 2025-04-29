import os
import anthropic
from chatbot import *



# Initialize Necessary Parameters
MODEL_NAME = "claude-3-5-sonnet-20240620"
MAX_TOKENS = 1000
INSTRUCTION = """You are intent categorizer. Base on the user's input, answer "healthcare" if the user asks about health, healthcare, diseases, or illnesses.
                        Answer "legal", if the user asks about legal.
                        Answer "education", if the user asks about education, academic, Pysics, Chemistry, Biology, Mathematics, or otherล subjects."""


# Initalize API Key
API_KEY = 'YOUR_API_KEY'  # Replace with your actual API key

# Initialize the Anthropic API client
LLM1 = anthropic.Anthropic(api_key=API_KEY)


# Start the chat loop
chat_history = []
QUERY = None  # Initialize query to avoid potential reference error

while True:
    if not QUERY:
        QUERY = input("User: ")
    if QUERY in ['quit', 'q', 'exit']:
        break

    INTENT = intent_categorizer(query=QUERY, llm=LLM1, model_name=MODEL_NAME, max_tokens=MAX_TOKENS, instruction=INSTRUCTION)
    print("Intent:", INTENT)

    if INTENT.lower().strip() == "healthcare":
        call_admin_healthcare()
        break
    elif INTENT.lower().strip() == "legal":
        call_admin_legal()
        break
    elif INTENT.lower().strip() == "education":
        call_admin_education()
        break
    else:
        call_admin_others()
        break

    query = None
    
