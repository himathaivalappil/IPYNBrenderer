from genericpath import getsize
import os 
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter the project name: ")
    if project_name != '':
        break

logging.info("Creating project with name : {project_name}")

# list of files to create
list_of_files = [

    f".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "setup.py",
    "setup.cfg",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini"
]

for filepath in list_of_files:
    file_dir,file_name = os.path.split(Path(filepath))

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info("Creating a directory for file: {file_name}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info("Creating new file: {file_name} at path {filepath}")

    else:
        logging.info("File is already present at path: {}".format(filepath))

    