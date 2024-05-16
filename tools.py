from crewai_tools import BaseTool
import os
import json
from textwrap import dedent

class CreateFilesTool(BaseTool):
	name: str = "Create Files Tool"
	description: str = dedent(
		f"""
			Creates the files.
			It just takes a json str.
		"""
	)
	
	def _run(self, jsonFiles: str) -> str:
		cleanedFiles = jsonFiles.replace("json```", "").replace("````", "").replace("python```", "")
		loadedJson = json.loads(cleanedFiles, strict=False)
		fileNames = []

		for value in loadedJson:
			os.makedirs(os.path.dirname(value["filePath"]), exist_ok=True)
			f = open(value["filePath"], "w")
			f.write(value["content"])
			f.close()

			fileNames.append(value["filePath"])

		stringFileNames = ", ".join(fileNames)

		return "Successfully created files " + stringFileNames