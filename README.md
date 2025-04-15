# Dockerized ISS Tracker

This is a simple POC to demonstrate how to containerize a Python3 script and its dependencies.

Main concepts:

1. The script itself. See `iss.py` for fundamental logic of the application itself. Good code should include exception handling.
2. A `requirements.txt` file that lists any dependencies to be installed in support of the application.
3. The `Dokerfile` that will build the script and dependencies into an image.
4. A GitHub Action file in `.github/workflows/build.yml` that instructs when/how to build and push each new image.

