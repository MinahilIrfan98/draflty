import sqlite3
import os
from dotenv import load_dotenv
from urllib.parse import quote

from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver


load_dotenv(".env")

llm = init_chat_model(
    model=os.getenv("DRAFTLY_LLM_MODEL"),
    # temperature=0.3,
    api_key=os.getenv("GOOGLE_API_KEY"),
    thinking_level="medium",
    max_retries=3
)

connection=sqlite3.connect("memory.db")
sqlite_checkpoiter=SqliteSaver(connection)

agent = create_agent(
    model=llm,
    tools=[],
    system_prompt="You are a AI email draft agent!",
    checkpointer=InMemorySaver()
)

user_id = input("Conversation name: ")
thread_config = {"configurable": {"thread_id": user_id}}

while True:
    q = input("You: ")
    if q.lower() in ("quit", "bye", "exit"):
        break

    result = agent.invoke(
        {"messages": [{"role": "user", "content": q}]},
        config=thread_config
    )
    print("Agent: ", result["messages"][-1].text)