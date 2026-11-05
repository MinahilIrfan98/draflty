import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from pydantic import BaseModel

load_dotenv(".env")

llm = init_chat_model(
    model=os.getenv("DRAFTLY_LLM_MODEL"),
    temperature=0.3,
    max_retries=3,
)

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are an AI email draft agent.",
    response_format=Draft
)

#q = input("query: ")
#result = agent.invoke({"messages": [{"role": "user", "content": q}]})
#print(result["messages"][-1].text)

messages=[]
while True:
    q=input("Query:")
    if q.lower() in ("quit", "bye", "exit"):
        break


    messages.append({"role": "user", "content":q})
    result=agent.invoke({"messages": messages})
    messages=result["messages"]
    print("Agent:",result["messages"][-1].text)