import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["math_server.py"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    agent = create_agent(
        model="ollama:qwen3.5:4b",
        tools=tools,
    )

    return await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is 12 multiplied by 8?"}]}
    )


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)