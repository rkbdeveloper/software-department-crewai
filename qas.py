import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from decouple import config

from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
  def __init__(self, instructions, base_folder):
    self.instructions = instructions
    self.base_folder = base_folder

  def run(self):
    agents = CustomAgents()
    tasks = CustomTasks()

    senior_qa_engineer_agent = agents.senior_qa_engineer_agent()
    automation_qa_engineer_agent = agents.automation_qa_engineer_agent()
    repository_manager_agent = agents.repository_manager_agent()
    documentation_officer_agent = agents.documentation_officer_agent()
  
    qa_website = tasks.qa_website(
      senior_qa_engineer_agent,
    )

    automated_testing_playwright = tasks.automated_testing_playwright(
      automation_qa_engineer_agent,
      self.instructions,
      self.base_folder,
    )

    create_files_task = tasks.create_files(
      repository_manager_agent,
    )

    add_readme_task = tasks.add_readme(
      documentation_officer_agent,
      self.instructions,
    )

    crew = Crew(
      agents=[senior_qa_engineer_agent, automation_qa_engineer_agent,documentation_officer_agent, repository_manager_agent ],
      tasks=[qa_website, add_readme_task, automated_testing_playwright,  create_files_task],
      verbose=True,
    )

    result = crew.kickoff()
    return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Let's test a website!")
    print("-------------------------------")
    base_folder = input(dedent("""Base Folder for the files: """))
    instructions = input(dedent("""Which website to test, define as much as possible: """))

    custom_crew = CustomCrew(instructions, base_folder)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
