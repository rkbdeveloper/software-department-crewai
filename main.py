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

    senior_engineer_agent = agents.senior_engineer_agent()
    qa_engineer_agent = agents.qa_engineer_agent()
    repository_manager_agent = agents.repository_manager_agent()
    documentation_officer_agent = agents.documentation_officer_agent()
    devsecops_agent = agents.devsecops_agent()

    initial_website_task = tasks.code_initial_website(
      senior_engineer_agent,
      self.instructions,
      self.base_folder,
    )

    add_unit_tests_task = tasks.add_unit_tests(
      qa_engineer_agent,
      self.instructions,
    )

    qa_website_task = tasks.qa_code(
      qa_engineer_agent,
    )

    add_readme_task = tasks.add_readme(
      documentation_officer_agent,
      self.instructions,
    )

    create_dev_sec_ops_files_task = tasks.create_dev_sec_ops_files(
      devsecops_agent,
      self.base_folder,
    )

    create_files_task = tasks.create_files(
      repository_manager_agent,
    )

    crew = Crew(
      agents=[senior_engineer_agent, qa_engineer_agent, documentation_officer_agent, devsecops_agent, qa_engineer_agent, repository_manager_agent],
      tasks=[initial_website_task, add_unit_tests_task, add_readme_task, create_dev_sec_ops_files_task, qa_website_task, create_files_task],
      verbose=True,
    )

    result = crew.kickoff()
    return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Let's create a website!")
    print("-------------------------------")
    base_folder = input(dedent("""Base Folder for the files: """))
    instructions = input(dedent("""Instructions for the website, define as much as possible: """))

    custom_crew = CustomCrew(instructions, base_folder)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
