# Google Classroom Downloader by Google Cloud API

- Requires Google Cloud Account and configuration
- Project environment setup using `pipenv`

## 1. Google Cloud Platform Setup
Create a Google Cloud Project: Go to Google Cloud Console and create a new project.
Enable APIs: Enable the Google Classroom API and Google Drive API for your project.
Configure OAuth Consent Screen: Set up the OAuth consent screen. Add the necessary scopes:
https://www.googleapis.com/auth/classroom.courses.readonly
https://www.googleapis.com/auth/classroom.announcements.readonly
https://www.googleapis.com/auth/classroom.student-submissions.me.readonly
https://www.googleapis.com/auth/drive
Create Credentials: Create an OAuth 2.0 Client ID. Download the JSON file containing your credentials.

- Set your google classroom email as test user.
## 2. Runtime Setup
Downloaded Credentials to the project directory as ./credentials.json file to your Google Colab environment.

## 3. Running the Script
Once everything is set up, you can run the script 

```
pipenv run python src/index.py
```

It will prompt to select courses

```
(0) MATH II
(1) ALCHEMY
(2) ALGORITHMS
(3) ROBOTICS
(4) SPANISH
(5) ETC
Select courses by index (e.g., 1,2,3): 0,1,2,3,5
```
## 3. Authentication in Desktop

The script will open a browser window and you need to select your google account with your classroom, give the permisions all to your app.

- if Access blocked Error you should include the user email to your testing users

## 6. Download

The download initializes automatically sincronously and you can see the progress in the console by course.

## 7. Output

The script creates a folder per course and it creates inside of each course a folder for each courseWorkMaterials, you are free to modify the script to your needs but the main idea is to download all the files from the courseWorkMaterials. (displayed as a purple book with a ribbon in the classroom)

## 8. Troubleshooting

- If you have problems with the authentication you can delete the token.json file and run the script again.
- If you have problems with the pipenv you can install the dependencies manually using pip install -r requirements.txt
- Generate requirements.txt
```
pipenv lock -r > requirements.txt
```

## 9. Acknowledgements

- [Google Classroom API](https://developers.google.com/classroom/quickstart/python)
- [Google Drive API](https://developers.google.com/drive/api/v3/quickstart/python)

## 10. Google App

This project is a Google App but is not intended to be deployed as a Google App, it is intended to be used as a script to download files from Google Classroom for personal use.
