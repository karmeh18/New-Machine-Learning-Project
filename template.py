import os, sys
from pathlib import Path
import logging

list_of_files=[
    "src/__init__.py",
    "src/components/__init__.py",
    "src/config/__init__.py",
    "src/constant/__init__.py",
    "src/entity/__init__.py",
    "src/exception/__init__.py",
    "src/logger/__init__.py",
    "src/pipeline/__init__.py",
    "src/utils/__init__.py",
    "src/config/config.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "logs.py",
    "exception.py",
    "setup.py",
    "requirements.txt"
]

# Loop through the list to create folders and files
for file_path in list_of_files:
    path = Path(file_path)
    
    # Create the parent directories if they don't exist
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Create the file
    path.touch(exist_ok=True)

print("All specified folders and files have been created.")