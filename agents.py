from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"  # or gpt-4-turbo, etc.

# --- Create Blog Researcher Agent ---
blog_researcher = Agent(
    role="Blog Researcher from YouTube videos",
    goal="Get relevant video content about {topic} from YouTube channels",
    verbose=True,
    memory=True,
    backstory=(
        "An expert in understanding YouTube videos on AI, Data Science, "
        "Machine Learning, and Generative AI, and providing meaningful summaries and suggestions."
    ),
    tools=[yt_tool],  # attach your YouTube search/analysis tool here
    llm=os.environ["OPENAI_MODEL_NAME"],  # directly use model name here
    allow_delegation=True
)

# --- Create Blog Writer Agent ---
blog_writer = Agent(
    role="Senior Blog Writer",
    goal="Narrate compelling tech stories about {topic} videos from YouTube channels",
    verbose=True,
    memory=True,
    backstory=(
        "A skilled storyteller who simplifies complex AI and data science topics "
        "into engaging, human-readable blog articles."
    ),
    tools=[yt_tool],
    llm=os.environ["OPENAI_MODEL_NAME"],
    allow_delegation=False
)
