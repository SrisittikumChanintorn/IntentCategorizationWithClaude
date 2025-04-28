# Intent Categorization by using Claude

An intelligent intent classification system that leverages Anthropic's Claude LLM to categorize user queries without requiring traditional supervised learning approaches.

## About Natural Language Understanding (NLU) & This Project

Natural Language Understanding (NLU) is a critical component in modern conversational AI systems. Traditional approaches to intent classification often require extensive labeled datasets and supervised learning models to categorize user inputs effectively.

This project takes a different approach by using Semantic Language Models (SLMs) to perform intent categorization. Instead of training a dedicated classifier, we harness Claude's powerful language understanding capabilities to categorize user queries into predefined domains:
- Healthcare
- Legal
- Education
- Other topics

By using an SLM for intent categorization, we can map user queries to the appropriate agentic workflow without the overhead of preparing and training supervised learning models. This approach provides several advantages:

1. No need for labeled training data
2. Simpler implementation and maintenance
3. Flexibility to easily add new intent categories
4. Ability to handle nuanced and complex queries

While this approach slightly increases inference costs (by making an additional API call for categorization), it dramatically reduces development time and improves extensibility for future advanced chatbot implementations requiring task-specific workflows.

## Project Structure

```bash
.
├── chatbot.py         # Contains intent categorization logic and admin response functions
├── main.py            # Main execution script with chat loop functionality
├── README.md          # Documentation (this file)
└── requirements.txt   # Project dependencies
```

## How It Works

1. User inputs a query in the command-line interface
2. The system sends the query to Claude with specific instructions to identify the intent
3. Based on the returned intent category, the appropriate admin handler is called
4. The system responds with domain-specific messaging
5. The loop continues until the user exits

## Key Components

- **Intent Categorizer**: Uses prompt engineering with Claude to classify user queries
- **Domain-Specific Handlers**: Separate functions for healthcare, legal, education, and other queries
- **Chat Loop**: Simple command-line interface for user interaction

## Installation and Usage

### Prerequisites
- Python 3.6+
- An Anthropic API key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/connectclaude-api.git
cd connectclaude-api
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Replace the API key in `main.py` with your actual Anthropic API key.

### Running the Application

Start the application by running:
```bash
python main.py
```

Enter your queries at the prompt. Type 'quit', 'q', or 'exit' to end the session.

## Future Enhancements

- Add more specialized intent categories
- Improve the admin response handlers with more detailed information
- Implement conversation history for context-aware responses
- Create a web interface for easier interaction
- Add support for multi-turn conversations
