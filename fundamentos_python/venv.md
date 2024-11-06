# Virtual enviroment

Allow you to work on projects without affecting the system-wide Python setup or other projects' dependencies

```sh
python -m venv clase5-venv

# Activate
source clase5-venv/bin/activate

# pip install <package_name>
# ....

# Deactivate
deactivate
```

```sh
# List all the packages and their versions currently installed in the virtual environment. 
pip freeze > requirements.txt

# Install all the dependencies mentioned in requirements.txt, ensuring that the environment is configured identically.
pip install -r requirements.txt
```
