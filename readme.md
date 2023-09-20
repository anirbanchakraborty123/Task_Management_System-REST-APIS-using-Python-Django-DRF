# Task Management CRUD Rest API using Python-Djnago-Drf

This is a RESTful API for managing tasks with features like pagination, filtering, and sorting.

## Setup Instructions

1. Clone the repository:
   ```
   - git clone https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF.git
   ```

2. Create a virtual environment:
   ```
   - python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
      ```
       venv\Scripts\activate
      ```
  
   - On macOS and Linux:
     ```
       source venv/bin/activate
     ```
  
4. Install dependencies:
```
   - pip install -r requirements.txt
```

5. Apply migrations:
```
   - python manage.py migrate
```
6. Start the development server:
```
   - python manage.py runserver
```
7. The API's will be accessible at 'http://localhost:8000/api/v1/' with mandatory JWT bearer access_token Authentication Header.
```
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
  ```  
### Swagger OPEN API Documentation:

   You can view swagger api document of all available Rest apis:
   - You can test them after authentication:
     ```
   - http://127.0.0.1:8000/docs/
     ```
## API Endpoints

   - Create a new task: 'POST /tasks/'
     
     <img width="630" alt="create_task" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/ee847bf7-2392-41ec-b846-0ba51c76c73e">

   - Retrieve a specific task by ID: 'GET /tasks/<task_id>/'
     
     <img width="637" alt="get_tasks_by_id" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/5a350693-c6f6-4afd-8f33-2a5af9ff0544">

   - Retrieve all tasks: 'GET /tasks/'
     
     <img width="629" alt="alltasks" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/9d56ce03-bb12-4c2c-9491-86c96301f792">
     
   - Update a task: 'PUT /tasks/<task_id>/'
     
     <img width="635" alt="update_tasks_by_id" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/e5e521d1-b3d0-45b8-8425-b5a205ed0103">

   - Delete a task: 'DELETE /tasks/<task_id>/'
     
      <img width="640" alt="delete_task_by_id" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/d0a67250-8ea3-4396-8fe7-cbda4f4a10f9">

   - Sort tasks: 'GET /tasks/sort/?sort_by=due_date or ?sort_by=title'
     
     <img width="639" alt="sort" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/fcd4ad9e-5cb4-4cc7-9730-4461f836ab2a">

   - Filter tasks: 'GET /tasks/filter/?status=in_progress or ?due_date=due_date'
     
     <img width="636" alt="filter" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/2c4567b2-0f17-42aa-8d33-71dec01ec54d">


### Filtering and Sorting

   You can filter and sort tasks by adding query parameters to the endpoint:
   - Filter by status: '?status=<status>'
   - Filter by due date: '?due_date=<date>'
   - Sort by due date: '?sort_by=due_date'
   - Sort by title: '?sort_by=title'


8. Running Tests

   - To run unit tests, use the following command:
   ```
    python manage.py test
   ```
    <img width="626" alt="test" src="https://github.com/anirbanchakraborty123/Task_Management_System-REST-APIS-using-Python-Django-DRF/assets/29591938/4ab52720-4149-48aa-b656-d9ecbd39f6d8">


10. Run the Development Server
```
   python manage.py runserver
```

