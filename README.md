python-template
===============

* Uses Poetry as the python virtual environment
Insallation instructions: https://python-poetry.org/docs/


To run the code leveraging poetry commands
------------
* Allow virtual env in project and install project dependencies  
  `poetry config virtualenvs.in-project true`
  `poetry install`
  
* To Run a python program  
  `poetry run <my_python_app.py>`
  
* To add a repository to poetry.  
  `poetry add <repo-name>`

--OPTIONAL--
* Run tests
  `poetry run pytest`
