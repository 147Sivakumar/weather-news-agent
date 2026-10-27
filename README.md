# AutoGen Weather News Agent

## Project Overview
The AutoGen Weather News Agent is a Python-based AI application that searches for recent weather-related news for a user-specified city using DuckDuckGo and summarizes the results using an OpenAI model.

## Features
- Accepts a city name from the user.
- Searches recent weather news using DuckDuckGo.
- Uses an AutoGen AI agent to summarize search results.
- Provides weather alerts and practical safety tips when supported by available information.
- Uses environment variables to protect the OpenAI API key.

## Technologies Used
- Python 3.12
- Microsoft AutoGen
- OpenAI GPT-4o-mini
- DuckDuckGo Search (`ddgs`)
- Python Dotenv

## Project Structure

```text
weather-news-agent/
├── weather_news.py
├── .env
├── .gitignore
└── README.md
```

**Note:** The `.env` file contains your API key and must not be uploaded to GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd weather-news-agent
```

### 2. Create and activate a virtual environment

On Windows Command Prompt:

```cmd
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```cmd
python -m pip install -U autogen-agentchat "autogen-ext[openai]" ddgs python-dotenv
```

### 4. Configure the API key

Create a `.env` file in the project directory:

```text
OPENAI_API_KEY=your_openai_api_key
```

Replace the placeholder with your own API key.

### 5. Run the application

```cmd
python weather_news.py
```

Enter a city name when prompted, for example:

```text
Which city? Puducherry
```

The agent searches for recent weather news and produces a concise summary with a safety tip.

## Security

Add the following entries to `.gitignore`:

```text
.env
venv/
__pycache__/
*.pyc
```

Never commit your API key or virtual environment to a public repository.

## Limitations
- Search results may be outdated, incomplete, or unrelated to current conditions.
- The application depends on internet access and a valid OpenAI API key.
- Search results alone do not guarantee an accurate live weather forecast.
- Always verify urgent weather warnings with official sources such as the India Meteorological Department (IMD).

## Author
Developed as a Python and AutoGen AI agent project.
