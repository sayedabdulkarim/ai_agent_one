import os 
os.environ['SERPER_API_KEY'] = ''
os.environ['OPEN_AI_KEY'] = ''

from crewai import Agent
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()