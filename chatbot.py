# Categorizes the user query into a specific intent using an LLM model.
def intent_categorizer(query, llm, model_name, max_tokens, instruction ):

    full_query = f"\nUser: {query}"

    chain = llm.messages.create(
        model=model_name,
        max_tokens=max_tokens,
        system=f"{instruction}",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": full_query
                    }
                ]
            }
        ]
    )

    result = chain.content[0].text

    return result

# Handles user queries related to healthcare.
def call_admin_healthcare():
    return print("Hello, I'm admin from ABC company who will answer questions about healthcare.")

# Handles user queries related to legal matters.
def call_admin_legal():
    return print("Hello, I'm admin of ABC company who will answer questions about legal.")

# Handles user queries related to education topics.
def call_admin_education():
    return print("Hello, I'm admin of ABC company who will answer questions about education.")

# Handles user queries that do not fit predefined intents.
def call_admin_others():
    return print("Hello, I'm admin of ABC company.")