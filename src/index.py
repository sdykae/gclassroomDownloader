from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os
import concurrent.futures
from googleapiclient.http import MediaIoBaseDownload
import io

def main():
    SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.coursework.me',
    'https://www.googleapis.com/auth/classroom.announcements',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]


    creds = get_credentials(SCOPES)
    service = build('classroom', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    # Get list of courses
    courses = service.courses().list().execute().get('courses', [])
    if not courses:
        print('No courses found.')
        return

    # Display courses and get user selection
    for i, course in enumerate(courses):
        print(f"({i}) {course['name']}")
    selected_indexes = input("Select courses by index (e.g., 1,2,3): ").split(',')

    # Process each selected course
    for index in selected_indexes:
        try:
            course_index = int(index.strip())
            course = courses[course_index]
            print(f"Downloading materials for course: {course['name']}")
            download_material_files(service, drive_service, course['id'], course['name'])
        except (IndexError, ValueError):
            print(f"Invalid selection: {index}")

def get_credentials(scopes):
    creds = None  # Initialize creds to None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', scopes)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def display_course_contents(service, course_id):
    try:
        course_works = service.courses().courseWork().list(courseId=course_id).execute().get('courseWork', [])
        if not course_works:
            print("No contents found.")
            return
        for work in course_works:
            print(f"- {work['title']}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_course_announcements(service, course_id):
    try:
        announcements = service.courses().announcements().list(courseId=course_id).execute().get('announcements', [])
        if not announcements:
            print("No announcements found.")
            return
        for announcement in announcements:
            print(f"- {announcement['text']}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_course_students(service, course_id):
    try:
        students = service.courses().students().list(courseId=course_id).execute().get('students', [])
        if not students:
            print("No students found.")
            return
        for student in students:
            print(f"- {student['profile']['name']['fullName']}")
    except Exception as e:
        print(f"An error occurred: {e}")

def display_course_work_materials(service, course_id):
    try:
        materials = service.courses().courseWorkMaterials().list(courseId=course_id).execute().get('courseWorkMaterial', [])
        if not materials:
            print("No course work materials found.")
            return
        for material in materials:
            print(f"- {material['title']} - {material.get('description', 'No description')}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_material_files(service, drive_service, course_id, course_name):
    materials = service.courses().courseWorkMaterials().list(courseId=course_id).execute().get('courseWorkMaterial', [])
    
    for material in materials:
        material_title = material['title']
        material_dir = os.path.join(course_name, material_title)
        os.makedirs(material_dir, exist_ok=True)

        # Assuming materials contain files or Drive references
        file_ids = extract_file_ids(material)  # Implement this function based on material structure
        
        for file_id in file_ids:
            try:
                download_file(drive_service, file_id, material_dir)
            except Exception as e:
                print(f"An error occurred while downloading file {file_id}: {e}")

def download_file(drive_service, file_id, destination_folder):
    try:
        file_metadata = drive_service.files().get(fileId=file_id, fields='name').execute()
        file_name = file_metadata.get('name', 'unknown')

        request = drive_service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

        with open(os.path.join(destination_folder, file_name), 'wb') as f:
            f.write(fh.getbuffer())
    except Exception as e:
        print(f"An error occurred while downloading file {file_id}: {e}")


def extract_file_ids(material):
    file_ids = []
    # Assuming 'material' contains a list of files or references to Drive files
    if 'materials' in material:
        for item in material['materials']:
            if 'driveFile' in item:
                drive_file = item['driveFile']
                if 'driveFile' in drive_file:
                    file_id = drive_file['driveFile'].get('id')
                    if file_id:
                        file_ids.append(file_id)
    return file_ids

if __name__ == '__main__':
    main()
