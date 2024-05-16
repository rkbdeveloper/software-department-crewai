from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from tools import CreateFilesTool

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
  def __init__(self):
    self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
    self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.2)
    self.OpenAIGPT4o = ChatOpenAI(model_name="gpt-4o", temperature=0.2)
    self.Ollama = Ollama(model="openhermes")

  def senior_engineer_agent(self):
    return Agent(
      role="Senior Software Engineer",
      backstory=dedent(
        f"""
          You are a Senior Software Engineer at a leading tech company.
          Your expertise in programming is javascript. and do your best to
          produce perfect code.
        """
      ),
      goal="Create software as needed",
      allow_delegation=False,
      verbose=True,
      llm=self.OpenAIGPT4o,
    )

  def qa_engineer_agent(self):
    return Agent(
      role="Software Quality Control Engineer",
      backstory=dedent(
        f"""
          You are a software engineer that specializes in checking code
          for errors. You have an eye for detail and a knack for finding
          hidden bugs.
          You check for missing imports, variable declarations, mismatched
          brackets and syntax errors.
          You also check for security vulnerabilities, and logic errors.
          You are also able to create unit testings with perfect precision on checking if a specific file works fine.
        """
      ),
      goal="Create prefect code, by analizing the code that is given for errors. You are also able to generate unit testings",
      allow_delegation=False,
      verbose=True,
      llm=self.OpenAIGPT4o,
  )

  def devsecops_agent(self):
    return Agent(
      role="Lead DevSecOps",
      backstory=dedent(
        f"""
          You are a Lead DevSecOps. You are an expert at deploying stuff on Google App Engine.
          You are able to create yaml files with ease that considers all the factors for each environment of the project.
        """
      ),
      goal="Create yaml files for cloud build configuration files and for deployment of the app to specific environments",
      allow_delegation=False,
      verbose=True,
      llm=self.OpenAIGPT4o,
  )

  def documentation_officer_agent(self):
    return Agent(
      role="Lead Documentation Officer",
      backstory=dedent(
        f"""
          You are a documentation officer agent. You are an expert at creating README files and documentation for a software engineering project.
        """
      ),
      goal="Create elegant and readable README files",
      allow_delegation=False,
      verbose=True,
      llm=self.OpenAIGPT4o,
  )

  def repository_manager_agent(self):
    return Agent(
      role="Repository Manager",
      backstory=dedent(
        f"""
          You are a Repository Manager that specializes in creating files.
          You make sure that the specified files are created.
        """
      ),
      goal="Create files that are given",
      tools=[CreateFilesTool()],
      allow_delegation=False,
      verbose=True,
      llm=self.OpenAIGPT4o,
  )
