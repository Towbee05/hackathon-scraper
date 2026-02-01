# HACKATHON SCRAPER

## Overview

This is a simple CLI application for the purpose of a hackathon submission. This application scrapes a hackathon website ([devpost](https://devpost.com/hackathons) used for reference) in search for hackathons and stores the returned hackathons into a JSON file at the project directory.

## Tools Used

1. Python (main programming language).
2. Selenium (used for web scraping due to devpost dynamic structure)
3. Beautiful soup (to parse selenium fetched content into readable format)

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

6. Run virtual environment

    On windows
        ```bash
        .venv\Scripts\activate
        ```

    On linux/macOS
        ```bash
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

![Code environment](images/Screenshot%202026-02-01%20200240.png)
![Expected result](images/Screenshot%202026-02-01%20200558.png)

## Note

This web scraper is just for practical purposes and not meant for illegal purposes.
