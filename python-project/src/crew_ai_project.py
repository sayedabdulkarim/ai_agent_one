import os 
from langchain_ollama import OllamaLLM

os.environ['SERPER_API_KEY'] = '37fb1573261727028f8baab406e729707337c314'

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
search_tool = SerperDevTool()

# Initialize the language model
llm = OllamaLLM(
    base_url="http://localhost:11434",
    model="llama3.2:1b",
    verbose=True
)

topic = "quantum computing"

### CREATE AGENTS START ###

# Create agents with explicit LLM
researcher = Agent(
    role='senior_researcher',
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    backstory=(
        "Driven by curiosity, you are at the forefront of"
        "innovation, eager to explore and share knowledge that could change "
        "the world." 
    ),
    tools=[search_tool],
    allow_delegation=True,
    llm=llm  # Add this line
)

writer = Agent(
    role='writer',
    goal='Write a report on {topic}',
    backstory=(
        "You are a skilled writer, able to transform complex ideas into "
        "engaging content. Your mission is to communicate the latest "
        "technological advancements to a broad audience."
    ),
    tools=[search_tool],
    allow_delegation=False,
    llm=llm  # Add this line
)

### CREATE AGENTS END ###


### CREATE TASKS START ###

# create a research task for the researcher agent
research_task = Task(
    description=(
        "Identify the next big thing in {topic}."
        "Focus on pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points"
        "its market opportunity and potential risk."
    ),
    expected_output="A 2 paragraph report on the latest trends in {topic}.",
    agent=researcher,
    tools=[search_tool]
)

# create a writing task for the writer agent
writing_task = Task(
    description=(
        "Write a report on the latest advancements in {topic}."
        "Your report should be engaging, informative, and accessible to a "
        "broad audience. Focus on the key benefits and potential impact of "
        "the technology."
    ),
    expected_output="A 100-word article on {topic}.",
    agent=writer,
    async_execution=False,
    tools=[search_tool],
    output_file="new_blog_post.md"
)

### CREATE TASKS END ###

### create a crew with the agents and tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, writing_task],
    process=Process.sequential
)

# run the crew
result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)