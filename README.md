# Google Classroom Downloader using Google Cloud API

This project provides a script for downloading files from Google Classroom using the Google Cloud API.

## Prerequisites

- A Google Cloud Account with configured access.
- Project environment setup using `pipenv`.

## 1. Google Cloud Platform Setup

- **Create a Google Cloud Project**: Go to the Google Cloud Console and create a new project.
- **Enable APIs**: Enable the Google Classroom API and Google Drive API for your project.
- **Configure OAuth Consent Screen**: Set up the OAuth consent screen. Add the necessary scopes:
  - `https://www.googleapis.com/auth/classroom.courses.readonly`
  - `https://www.googleapis.com/auth/classroom.announcements.readonly`
  - `https://www.googleapis.com/auth/classroom.student-submissions.me.readonly`
  - `https://www.googleapis.com/auth/drive`
- **Create Credentials**: Create an OAuth 2.0 Client ID and download the JSON file containing your credentials.
- **Test User**: Set your Google Classroom email as a test user.

## 2. Runtime Setup

- Download and place the Credentials JSON file in the project directory (named `./credentials.json`).

## 3. Running the Script

Run the script using the following command:

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

## 4. Authentication on Desktop

The script will open a browser window for authentication. Log in with your Google account that has access to the Classroom and grant the necessary permissions to the app.

- If an "Access Blocked" error occurs, include the user's email in your list of testing users.

## 5. Download Process

The download will begin automatically in a synchronous manner. Progress for each course will be displayed in the console.

## 6. Output

The script creates a directory for each course. Within each course directory, it creates a folder for each `courseWorkMaterial` (represented by a purple book with a ribbon in Classroom). You can modify the script as needed, but the primary function is to download all files from the courseWorkMaterials.

## 7. Troubleshooting

- **Authentication Issues**: If you encounter authentication problems, delete the `token.json` file and run the script again.
- **Pipenv Issues**: If there are issues with `pipenv`, you can manually install dependencies using `pip install -r requirements.txt`.
- **Generate `requirements.txt`**:

```
pipenv lock -r > requirements.txt
```


## 8. Acknowledgements

- [Google Classroom API](https://developers.google.com/classroom/quickstart/python)
- [Google Drive API](https://developers.google.com/drive/api/v3/quickstart/python)

## 9. About This Project

This project is a Google App, but it is not intended for deployment as a Google App. It is designed for personal use as a script to download files from Google Classroom. It is not affiliated with Google in any way.
