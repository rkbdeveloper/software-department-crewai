from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
  def __tip_section(self):
    return "If you do your BEST WORK, I'll give you a $10,000 commission!"

  def code_initial_website(self, agent, instructions, base_folder):
    return Task(
      description=dedent(
        f"""
          {self.__tip_section()}

          You will code a website using node, nextjs, nestjs, typescript, tailwind, jest and react.
          Here are more instructions on what kind of website to build:

          Instructions
          ------------

          {instructions}
        """
      ),
      expected_output=dedent(
          f"""
            Base folder for all the files should be on {base_folder}
            Your final output should be in array workable string json format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )

  def add_unit_tests(self, agent, instructions):
    return Task(
      description=dedent(
        f"""
          You are helping create a website using javascript, these are the instructions:

          Instructions
          ------------
          {instructions}

          Using the code you got, add unit testings the the files that needs unit testings.
        """
      ),
      expected_output=dedent(
          f"""
            Your final output should be in array workable string json array format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure you include all the files appending your generated unit tests.
            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )
  
  def add_readme(self, agent, instructions):
    return Task(
      description=dedent(
        f"""
          You are helping create a website using javascript, these are the instructions:

          Instructions
          ------------
          {instructions}

          Using the code you got, make a README file on essential things like running the project.
        """
      ),
      expected_output=dedent(
          f"""
            Your final output should be in array workable string json array format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure you include all the files from the previous agent in the return appending your generated README file.
            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )
  
  def create_dev_sec_ops_files(self, agent, base_folder):
    return Task(
      description=dedent(
        f"""
          You are helping create a website using javascript.

          Using the code you got in json format, make the necessary yaml files to run this application in Google App Engine.
          The yaml files should have different environments for dev, staging, and prod.
          You will also create a on-pull-request-dev.yaml (file name will depend on environment) file inside the appengine folder of the project,
          which will be used as a Cloud Build configuration file in Google App Engine.
          Deployment yaml files like app-dev.yaml should just be in the root folder. Cloud build configuration files should only the ones inside the appengine folder.
          This should be the base folder of the files {base_folder}
        """
      ),
      expected_output=dedent(
          f"""
            Your final output should be in array workable string json array format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure you include all the files from the previous agent in the return appending your generated yaml files to the json array.
            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )
  
  def qa_code(self, agent):
    return Task(
      description=dedent(
        f"""
          You are helping create a website using javascript.

          Using the code you got, check for errors. Check for logic errors,
          syntax errors, missing imports, variable declarations, mismatched brackets,
          and security vulnerabilities.
        """
      ),
      expected_output=dedent(
          f"""
            Your final output should be in array workable string json array format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure you include all the files and just updating the files you feel like needs updating in the json array.
            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )
  
  def create_files(self, agent):
    return Task(
      description=dedent(
        f"""
          You are helping create a website using javascript.

          Using the json you got, you create files base on their file paths and content.
          You pass the json immediately to the tool, if the json string is not parsable, please fix it.
        """
      ),
      expected_output=dedent(
          f"""
            You use the tools given to you to create files.
          """
      ),
      agent=agent,
    )

  def qa_website(self, agent):
    return Task(
      description=dedent(
        f"""
          You are helping test a website manually.

          Using the website you got, perform manual QA testing. Check for functionality issues,
          user interface inconsistencies, broken links, responsiveness on different devices,
          and overall user experience. Ensure that all features work as expected and report any bugs or issues found.
        """
      ),
      expected_output=dedent(
          f"""
            Your final output should be a detailed report in array workable string json array format like below:
            [{{ "issue": "...", "description": "...", "steps_to_reproduce": "...", "severity": "..." }}, ...]

            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )

  def automated_testing_playwright(self, agent, instructions, base_folder):
    return Task(
      description=dedent(
        f"""
         You are helping create automated tests for a website using Playwright.

          Instructions
          ------------
          {instructions}

          Using the code you got, write automated tests for the website. Ensure that the tests cover critical functionalities,
          user interface elements, and responsiveness on different devices (minimum of 3 devices). The tests should be written in a way that they can be
          easily run and maintained and should include all necessary files(i.e. package.json) for execution. like 
        """
      ),
      expected_output=dedent(
          f"""
            Base folder for all the files should be on {base_folder}
            Your final output should be in array workable string json array format like below:
            [{{ "filePath": "...", "content": "..." }}, {{ "filePath": "...", "content": "..." }}, ...]

            Make sure you include all the files appending your generated Playwright tests.
            Make sure that the file name have spec.
            Make sure to not add anything around, just the string json array.
            Make sure your output is stringified, please include the new lines in the stringified version.
          """
      ),
      agent=agent,
    )