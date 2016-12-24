# Happy or Not

This project is a demo to show how to use https://www.microsoft.com/cognitive-services.  You will need to obtain a key for the Emotion API [here](https://www.microsoft.com/cognitive-services/en-US/subscriptions).

You can find a demo at http://happyimagetester.azurewebsites.net/

Prefer Node.js? Check out this [sample in Node.js](https://github.com/jsturtevant/happy-image-tester-nodejs).

## Setup
### Use Docker (https://www.docker.com/) 
1. Clone this repo and move into folder: ```CD happy-image-tester-django```
2. Add environemnt variable with your Cognitive Services key to your current console session:
    mac: ```export OXFORD_KEY=<yourkey>```
    windows: ```set "OXFORD_KEY=<yourkey>"```
3. Run ```docker-compose -f ./docker-compose.debug.yml up``` from same session
4. Browse to the website: open favorite browser to 127.0.0.1:8000
5. Use sample images to upload a file

### Without docker
This project can be [Setup on Windows](#setup-windows) or [Mac](#setup-mac).  You will need to add the Emotion API key to your environment variables (see below on how to do that for local environment). 

#### Setup Windows
1. [Install Python 3.5 or greater](https://www.python.org/downloads/) (it will work with 2.7 if you want to use it)
2. Open command prompt and Clone this repo
3. Move into cloned repo folder: ```CD happy-image-tester-django```
4. Create a virtual environment: ```c:\python34\python.exe -m venv env```  (your path to Python may vary)
5. Install library requirements: ```env\scripts\pip install -r requirements.txt```
6. Open the file ```env\scripts\activation.bat``` 
7. At the end of the file before ```:END``` add  ```set "OXFORD_KEY=<yourkey>"``` and save file.
8. Activate Virtual Environment: ```env\Scripts\activate.bat```
9. Start development server: ```env\scripts\python manage.py runserver```
10. Browse to the website: open favorite browser to 127.0.0.1:8000
11. Use sample images to upload a file.

When done with development de-activate virtual environment with ```env\Scripts\deactivate.bat```

#### Setup Mac
1. [Install Python 3.5 or greater](https://www.python.org/downloads/) (it will work with 2.7 if you want to use it)
2. Open command prompt and Clone this repo
3. Move into cloned repo folder: ```CD happy-image-tester-django```
4. Create a virtual environment: ```python3 -m venv env```
5. Install library requirements: ```env/bin/pip install -r requirements.txt```
6. Open the file ```env/bin/activate``` in your favorite text editor
7. At the middle of the file, after  ```EXPORT PATH``` add  ```export "OXFORD_KEY=<yourkey>"``` and save file.
8. Activate Virtual Environment: ```source env/bin/activate```
9. Start development server: ```env/bin/python manage.py runserver```
10. Browse to the website: open favorite browser to 127.0.0.1:8000
11. Use sample images to upload a file.

When down with development de-activate virtual Environment with ```deactivate```




