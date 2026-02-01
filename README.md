# HACKATHON SCRAPER

## Overview

This is a simple CLI application for the purpose of a hackathon submission. This application scrapes a hackathon website ([devpost](https://devpost.com/hackathons) used for reference) in search for hackathons and stores the returned hackathons into a JSON file at the project directory.

## Tools Used

1. Python (main programming language).
2. Selenium (used for web scraping due to devpost dynamic structure)
3. Beautiful soup (to parse selenium fetched content into readable format)
4. Git and Github

## What github was used for in this project

Git served as the major version control system, I used it to keep track of my development history with clean, readable and understandable commits. Git is very useful as it keeps record of changes in files, because of this reason, it is very easy for me to go back into my code in order to locate bugs if any, and in special cases where my codebase maybe lost, I can easily rely on git for staged history.
Github served as a platform for me to create, share and view git staged changes. With github, I can see all the changes in my project and read through them.
I also used github actions to create a linter to lint my files whenever I push to production.

## Installation

1. Ensure python is installed, if not install from [python website](https://www.python.org/downloads/).
2. install uv: Open your terminal and run

    ```bash
     pip install uv
    ```

3. Clone file

    ```bash
    git clone "git@github.com:Towbee05/hackathon-scraper.git"
    ```

4. cd into working directory

    ```bash
    cd hackathon-scraper
    ```

5. Create a virtual environment

    ```bash
    uv venv .venv
    ```

6. Run virtual environment. First is for windows OS, and the second is for linux/macOS

    ```bash
    .venv\Scripts\activate

    .venv\bin\activate
    ```

7. Install all dependencies

    ```bash
    uv pip install -r requirements.txt
    ```

8. Run project

    ```bash
    uv run app/main.py
    ```

## Screenshots

![Code environment](./images/Screenshot%202026-02-01%20200240.png)
![Expected result](./images/Screenshot%202026-02-01%20200558.png)
![Github Interface](./images/Screenshot%202026-02-01%20202050.png)
![Github Commits Interface](./images/Screenshot%202026-02-01%20202011.png)

## Note

This web scraper is just for practical purposes and not meant for illegal purposes.
