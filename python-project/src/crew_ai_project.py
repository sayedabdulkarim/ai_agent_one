import os 
from langchain_ollama import OllamaLLM

os.environ['37fb1573261727028f8baab406e729707337c314'] = ''
os.environ['OPEN_AI_KEY'] = ''

from crewai import Agent
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

#initialize the language model
llm = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama3.2:1b",
    verbose=True
)

# create a senior research agent with memory and verbose mode
researcher = Agent(
    role='senior_researcher',
    goal='Uncover ground breaking technologies in { topic }',
    verbose=True,
    backstory=(
        "Driven by curiosity, you are at the forefront of"
        "innovation, eager to explore and share knowledge that could change "
        "the world." 
    ),
    tools=[search_tool],
    allow_delegation=True
)

# create a writer agent with custom tools and delegation capabilities
writer = Agent(
    role='writer',
    goal='Write a report on { topic }',
    backstory=(
        "You are a skilled writer, able to transform complex ideas into "
        "engaging content. Your mission is to communicate the latest "
        "technological advancements to a broad audience."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Test function to check if llm is working
def test_llm():
    prompt = ["What is the future of AI?"]
    response = llm.generate(prompts=prompt)
    print("LLM Response:", response)

# Run the test function
if __name__ == "__main__":
    test_llm()