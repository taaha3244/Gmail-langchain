import os
from langchain_community.agent_toolkits import GmailToolkit
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI

load_dotenv()

openai_api_key=os.getenv('OPENAI_API_KEY')
GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')

toolkit = GmailToolkit()

tools=toolkit.get_tools()

instructions = """You are an assistant."""
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)

llm = ChatOpenAI(model='gpt-3.5-turbo',temperature=0, api_key=openai_api_key)

agent = create_openai_functions_agent(llm, toolkit.get_tools(), prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
    verbose=True,
)

agent_executor.invoke(
    {
        "input": "Create a gmail draft for me to edit of a letter from the perspective of a sentient parrot"
        " who is looking to collaborate on some research with her"
        " estranged friend, a cat. Under no circumstances may you send the message, however."
    }
)

agent_executor.invoke(
    {"input": "Could you search in my inbox for the latest email? what is the title?"}
)