# Poetry:
- Poetry requires Python 3.8+. It is multi-platform and the goal is to make it work equally well on Linux, macOS and Windows.

# Installation:
1. Install pipx
   - https://pipx.pypa.io/stable/installation/
2. `pipx install poetry`
3. Create New Project
    - `cd /path/to/your/directory`
    - `poetry new my_project_name`
4. Add dependencies
   - `poetry add requests`
5. Activate venv
    - `poetry shell`
6. Install Project in Editable Mode (Optional):
   - `poetry install`


# FAQ's on Poetry:
### 1. How to configure poetry to use python3.12 for python3.9 project
   - First deactivate the env by exit from the poetry shell
   - Install python3.12
     - `brew install python@3.12`
   - `poetry env use python3.12`
   - Update pyproject.toml --> `python = "^3.12"`
   - After updating the Python version, reinstall your dependencies to ensure they are compatible with Python 3.12:
   - `poetry install`
   - `poetry lock` --> lock file gets updated with the proper version
   - `poetry shell`
   - `poetry run pytest`
   - Remove Old Virtual Environment (Optional)
     - `poetry env remove python3.9`
### 2. What does `poetry lock` command do?
   - If the `poetry.lock` file doesn’t exist: Poetry creates a new poetry.lock file. This file will contain a list of all
   resolved dependencies, including their specific versions, and hashes to ensure integrity.
   - If the `poetry.lock` file already exists: Poetry will update it to reflect any changes in your pyproject.toml file,
   such as added, removed, or updated dependencies.
### 3. What does `poetry install` command do?
   - Checks the `poetry.lock` file: The command first checks if a `poetry.lock` file exists. This file contains the exact 
   versions of all dependencies that have been resolved and locked for your project. If it exists, Poetry will install 
   the dependencies based on this file to ensure consistency.
### 4. `poetry install --no-root`?
   - The command `poetry install --no-root` is used to install the dependencies listed in your pyproject.toml and 
   poetry.lock files, but with one key difference: it does not install your project as a package in the environment.
### 5. Give me a solid reason to use `poetry` instead of `pip feeeze`?
   Scenario 
   - Imagine you have a Python project with the following dependencies specified in pyproject.toml:
   
   toml
   ```[tool.poetry.dependencies]
   python = "^3.9"
   flask = "^2.0"
   requests = "^2.25"
   Understanding Dependency Resolution
   Flask's Dependencies:
   ```
   Flask might depend on Werkzeug, Jinja2, Click, etc.
   Let's say Flask 2.0 depends on `Jinja2>=2.11.`

   Requests' Dependencies:
   Requests might depend on urllib3, chardet, etc.

   Let's say Requests 2.25 has a sub-dependency on urllib3<1.27.

   ### Potential Conflict:
   Imagine there's a package SomeLib that also depends on Jinja2 but requires a version of Jinja2<2.11 for some reason. 
   This creates a potential conflict because:
   
   Flask 2.0 requires Jinja2>=2.11. 
   SomeLib requires Jinja2<2.11.

   ### With Poetry's Dependency Resolution:
   #### Resolving Conflicts:
   
   When you run poetry lock, Poetry will attempt to resolve these dependencies by finding compatible versions that satisfy all constraints. 
   If no compatible version exists, Poetry will raise an error, informing you of the conflict so you can take action, 
   such as upgrading or changing one of the conflicting dependencies. In this case, Poetry might resolve to keep 
   Flask 2.0 and suggest removing or upgrading SomeLib since its requirements are incompatible.
   
   #### Resulting poetry.lock File:
   
   The poetry.lock file will contain the exact versions of Flask, Requests, and their compatible sub-dependencies (Werkzeug, Jinja2, urllib3, etc.), ensuring that this combination will work without issues in any environment.

   ### With pip freeze (Snapshot):

   #### Taking a Snapshot:
   Suppose you manually install Flask, Requests, and SomeLib without using Poetry, and then run pip freeze.
   The pip freeze command captures the currently installed versions, including any potentially conflicting ones, 
   without checking if they are truly compatible. You might end up with a requirements.txt file that lists:
   ```
   Flask==2.0.1
   Jinja2==2.10  # Installed because of SomeLib
   Requests==2.25.1
   urllib3==1.26.5
   SomeLib==1.0.0
   ```

   ### Potential Issues:
   
   This snapshot (requirements.txt) suggests that everything works on your current machine. However, 
   the conflict between `Jinja2>=2.11` (needed by Flask) and `Jinja2<2.11` (required by SomeLib) might lead to runtime errors in a different environment or after further development.
   The snapshot doesn’t provide any guarantee that these versions are actually compatible.

   #### Summary
   Poetry's Dependency Resolution: Carefully evaluates and resolves dependencies to ensure compatibility, generating a poetry.lock file that guarantees a working set of dependencies.
   pip freeze Snapshot: Simply records the currently installed versions, potentially including incompatible packages that were installed without any conflict resolution.
   This example demonstrates how Poetry’s approach to dependency management ensures a reliable and conflict-free environment, whereas pip freeze might result in a non-reproducible or broken setup.