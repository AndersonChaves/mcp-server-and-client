from langchain_openai import AzureChatOpenAI
import os
 
from dotenv import load_dotenv
 
load_dotenv()
 
OPENAI_API_VERSION=os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME=os.getenv("DEPLOYMENT_NAME")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")
OPENAI_ENDPOINT=os.getenv("OPENAI_ENDPOINT")
 
def invoke_llm(messages: list) -> str:
    llm = AzureChatOpenAI(
        azure_deployment=DEPLOYMENT_NAME,
        api_version=OPENAI_API_VERSION,
        api_key=OPENAI_API_KEY,
        model=MODEL_NAME,
        azure_endpoint=OPENAI_ENDPOINT,
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )
    response = llm.invoke(messages)
    return response.content
 