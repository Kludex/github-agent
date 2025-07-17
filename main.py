import asyncio

from pydantic_settings import BaseSettings

from pydantic_ai import Agent


class Settings(BaseSettings): ...


agent = Agent(
    "anthropic:claude-sonnet-4-0",
    instructions="""
You are a GitHub bot. Your job is to help users and maintainers.

You can:
1. Label issues to categorize them.
2. Assign issues to maintainers.
3. Comment on issues to provide helpful information.
""",
)


async def main():
    return
    result = await agent.run()
    print(result.output)


if __name__ == "__main__":
    asyncio.run(main())
