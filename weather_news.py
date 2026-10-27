
# Project: AutoGen Weather News Agent
# Description: Search today's weather news using DuckDuckGo and AutoGen.

# Step 1: Import the required Python libraries and AutoGen modules.
import asyncio
import os
from dotenv import load_dotenv

from ddgs import DDGS
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Step 2: Create a web search tool using DuckDuckGo (free, no API key).
def search_weather_news(city: str) -> str:
    """
    Search recent news about today's weather in the specified city.
    Return relevant weather news headlines and summaries, not general trivia.
    """

    # Step 3: Search for recent weather news for the specified city.
    try:
        results = DDGS().news(
            query=f"{city} weather today",
            max_results=5,
        )

        # Step 4: Extract news headlines, dates, and summaries.
        articles = []
        for item in results:
            title = item.get("title", "No title")
            body = item.get("body", "")
            date = item.get("date", "")

            articles.append(
                f"Headline: {title}\nDate: {date}\nSummary: {body}"
            )

        # Step 5: Handle empty results and return the collected news.
        if not articles:
            return f"No recent weather news found for {city}."

        return "\n\n".join(articles)

    except Exception as exc:
        return f"Weather news search failed for {city}: {exc}"


# Step 6: Ask the user to enter a city and validate the input.
async def main():
    city = input("Which city? ").strip()

    if not city:
        print("Please enter a city.")
        return

    # Step 7: Check whether the OpenAI API key is configured.
    
    # Step 7: Load and check the OpenAI API key from the .env file.
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        print("API key missing. Check your .env file.")
        return


    # Step 8: Initialize the OpenAI model client using GPT-4o-mini.
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=os.environ["OPENAI_API_KEY"],
    )

    # Step 9: Create the AutoGen agent and register the search tool.
    agent = AssistantAgent(
        name="weather_news",
        model_client=model_client,
        tools=[search_weather_news],

        # Step 10: Instruct the agent to respond in exactly three short lines.
        system_message=(
            "You are a weather news assistant. "
            "Always call search_weather_news for the requested city. "
            "Use only facts supported by the search results. "
            "Check the dates of the results and never present old news "
            "as today's confirmed weather. "
            "Reply in exactly 3 short lines, with no blank lines: "
            "Line 1: Today's weather, if verified; otherwise say "
            "current conditions could not be verified. "
            "Line 2: The most relevant recent weather news or alert, "
            "including its date when useful. "
            "Line 3: One practical safety tip. "
            "Never invent weather conditions or alerts."
        ),

        # Step 11: Enable reflection to summarize the tool results.
        reflect_on_tool_use=True,
    )

    # Step 12: Run the agent and display tool calls and responses.
    try:
        await Console(
            agent.run_stream(
                task=f"Give me today's weather news for {city}."
            )
        )

    # Step 13: Close the model client after execution.
    finally:
        await model_client.close()


# Step 14: Start the application using asyncio.
if __name__ == "__main__":
    asyncio.run(main())
