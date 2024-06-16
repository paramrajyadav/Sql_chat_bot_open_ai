import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_openai import ChatOpenAI
from huggingface_hub import notebook_login
from huggingface_hub import hf_secrets


# Load environment variables from .env file
def initiate_chat(querry):
    load_dotenv()

    notebook_login()

    # Set environment variables for API keys
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

    # Define the SQL database URI
    db_uri = "sqlite:///db.db"

    # Initialize the SQLDatabase object
    db = SQLDatabase.from_uri(db_uri)
    # api_key = hf_secrets.get("open_api")

    # Initialize the ChatOpenAI object with the desired model
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    # Create the SQL agent
    agent_executor = create_sql_agent(llm, db=db, agent_type="openai-tools", verbose=True)

    # Define the query to get the sum of all salaries
    

    # Execute the query using the agent
    try:
        result = agent_executor.invoke(querry)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return "Error: " + str(e)
