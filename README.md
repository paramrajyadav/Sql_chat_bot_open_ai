# SQL Chatbot for Easy Data Extraction

This repository provides a user-friendly SQL chatbot that simplifies extracting information from your tabular files. Leverage the power of OpenAI's language processing and LangChain's SQL generation capabilities to perform insightful queries in a natural language interface.

## Features

- **Intuitive Chat Interface:** Interact with your data in a conversational manner using plain English queries.
- **Streamlit UI:** Enjoy a visually appealing web app for seamless interaction with the chatbot.
- **SQLite Support:** Utilize SQLite, a lightweight and embedded database engine, for efficient data storage.

## Requirements

- Python 3.x (https://www.python.org/downloads/)
- OpenAI API Key (https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key)
- LangChain API Key ([invalid URL removed]) (Note: Check LangChain documentation for API key acquisition instructions)
- `requirements.txt` (included)

## Installation and Configuration

```bash
git clone https://github.com/paramrajyadav/sql_chat_bot.git
```
```bash
cd sql_chat_bot
```
```bash
pip install -r requirements.txt
```

# Create a .env file and add these lines, replacing placeholders with your actual keys:
OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langchain_api_key

## Usage
Run the application: streamlit run app.py

Access the Streamlit app in your web browser (usually http://localhost:8501).

Interact with the chatbot by typing natural language queries in the input field.

The chatbot will translate your queries into SQL and retrieve the desired information from your table.


## Sample Queries
"Show me all customers in California."

"What are the average order values per product category?"

"Find orders placed between January and March 2024."


## Contributing

We welcome contributions from the community! Here are some ways you can get involved:

* **Bug reports:** If you find a bug, please create an issue on the GitHub repository. Be sure to include clear steps to reproduce the bug.
* **Feature requests:** If you have an idea for a new feature, please create an issue on the GitHub repository. Describe the feature in detail and explain why it would be valuable.
* **Pull requests:** If you have implemented a bug fix or feature, you can submit a pull request. Make sure to follow the contributing guidelines (if available) and test your changes thoroughly.
