import os 
os.environ['SERPER_API_KEY'] = ''
os.environ['OPEN_AI_KEY'] = ''

from crewai import Agent
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

# create a senior research agent with memory and verbose mode
researcher = Agent(
    role='senior_researcher',
    goal='Uncover ground breaking technologies in { topic }',
    verbose=True,
    backstory=(
        "Driven by curiosity, you are at the forefront of"
        "innovation, eager to explore and share knowledge that could change "
        "the world." 
    )
)