# Happy or Not

This project is a demo to show how to use https://www.projectoxford.ai/.  You will need to obtain a key for the Emotion API [here](https://www.projectoxford.ai/Subscription).

You can find a demo at http://happyornot.azurewebsites.net/

## Setup
This project can be [Setup on Windows](#setup-windows) or [Mac](#setup-mac).  You will need to add the Emotion API key to your environment variables. (instructions coming soon)

### Setup Windows
1. [Install Python 3.5 or greater](https://www.python.org/downloads/) (it will work with 2.7 if you want to use it)
2. Open command prompt and Clone this repo
3. Move into cloned repo folder: ```CD happy-or-not-django```
4. Create a virtual environment: ```c:\python34\python.exe -m venv env```
5. Install library requirements: ```env\scripts\pip install -r requirements.txt```
6. Start development server: ```env\scripts\python manage.py runserver```
7. Browse to the website: open favorite browser to 127.0.0.1:8000
8. Use sample images to upload a file.

### Setup Mac
1. [Install Python 3.5 or greater](https://www.python.org/downloads/) (it will work with 2.7 if you want to use it)
2. Open command prompt and Clone this repo
3. Move into cloned repo folder: ```CD happy-or-not-django```
4. Create a virtual environment: ```python3 -m venv env```
5. Install library requirements: ```env/bin/pip install -r requirements.txt```
6. Start development server: ```env/bin/python manage.py runserver```
7. Browse to the website: open favorite browser to 127.0.0.1:8000
8. Use sample images to upload a file.




