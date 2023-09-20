from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User

class TaskAPITestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
                username='test', email='test@gmail.com', password='top_secret')
        self.client = APIClient()
        token = AccessToken.for_user(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        self.task_data = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'status': 'created',
            'due_date': '2023-09-28',
        }
        self.task = Task.objects.create(**self.task_data)
        self.task1 = Task.objects.create(title="Task 1", description="Description 1", status="in_progress", due_date="2023-09-20")
        self.task2 = Task.objects.create(title="Task 2", description="Description 2", status="completed", due_date="2023-10-25")
        
    def test_create_task(self):
        """ Test case to check create new task - api """
        
        response = self.client.post('/api/v1/tasks/', self.task_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Task.objects.count(), 4)
        
    def test_retrieve_task(self):
        """ Test case to check task with specific id - api"""
        
        response = self.client.get(f'/api/v1/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.task_data['title'])

    def test_update_task(self):
        """ Test case to check update task for particular id  - api"""
        updated_data = {
            'title': 'Updated Task',
            'status': 'completed',
        }
        response = self.client.patch(f'/api/v1/tasks/{self.task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, updated_data['title'])
        self.assertEqual(self.task.status, updated_data['status'])

    def test_delete_task(self):
        """ Test case to delete task with specific id - api"""
        
        response = self.client.delete(f'/api/v1/tasks/{self.task.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Task.objects.filter(id=self.task.id).count(), 0)  # Check that the task is deleted
    
    def test_sort_by_due_date(self):
        """ Test case to test the Task sort - api. """
        
        response = self.client.get('/api/v1/tasks/sort/?sort_by=due_date')
        self.assertEqual(response.status_code, 200)
        sorted_tasks = response.json()
        self.assertEqual(sorted_tasks['count'], 3) # Checks Valid Response
        self.assertNotEqual(sorted_tasks['count'], 8) # Checks Invalid/Incorrect Response
       
    def test_filter_by_due_date(self):
        """ Test case to test the Task filter - api. """
        
        response = self.client.get('/api/v1/tasks/filter/?due_date=2023-09-20')
        self.assertEqual(response.status_code, 200)
        sorted_tasks = response.json()
        self.assertEqual(sorted_tasks['count'], 1) # Checks Valid Response
        self.assertNotEqual(sorted_tasks['count'], 8) # Checks Invalid/Incorrect Response
        

