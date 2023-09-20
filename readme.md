# Task Management CRUD Rest API using Python-Djnago-Drf

This is a RESTful API for managing tasks with features like pagination, filtering, and sorting.

## Setup Instructions

1. Clone the repository:

   - git clone https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF.git

2. Create a virtual environment:

   - python -m venv venv

3. Activate the virtual environment:
   - On Windows:
       venv\Scripts\activate
  
   - On macOS and Linux:
       source venv/bin/activate
  
4. Install dependencies:

   - pip install -r requirements.txt

5. Apply migrations:

   - python manage.py migrate

6. Start the development server:

   - python manage.py runserver

7. The API's will be accessible at 'http://localhost:8000/api/v1/' with mandatory JWT bearer access_token Authentication Header.

   - You can get new access_token using login creds-(username,passsowrd) on below apis
   - Get new access_token 'POST /token/'
      - payload={
        username,password
      }
      - response={
        access_token,refresh_token
      }
   - Refresh expired access_token by passing refresh_token to 'POST /token/refresh/'
     - payload={
        refresh_token
     }
     - response={
        access_token,refresh_token
     }
    
### Swagger OPEN API Documentation:

   You can view swagger api document of all available Rest apis:
   - You can test them after authentication:
   - http://127.0.0.1:8000/docs/

## API Endpoints

   - Create a new task: 'POST /tasks/'
   - Retrieve a specific task by ID: 'GET /tasks/<task_id>/'
   - Retrieve all tasks: 'GET /tasks/'
   ![alt text](https://ibb.co/jJS3Nv6)
   - Update a task: 'PUT /tasks/<task_id>/'
   - Delete a task: 'DELETE /tasks/<task_id>/'
   - Sort tasks: 'GET /tasks/sort/?sort_by=due_date or ?sort_by=title'
   - Filter tasks: 'GET /tasks/filter/?status=in_progress or ?due_date=due_date'

### Filtering and Sorting

   You can filter and sort tasks by adding query parameters to the endpoint:
   - Filter by status: '?status=<status>'
   - Filter by due date: '?due_date=<date>'
   - Sort by due date: '?sort_by=due_date'
   - Sort by title: '?sort_by=title'


8. Running Tests

   - To run unit tests, use the following command:
    python manage.py test

9. Run the Development Server

   python manage.py runserver


