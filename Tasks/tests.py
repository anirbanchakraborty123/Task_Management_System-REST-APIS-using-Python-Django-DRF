from django.test import TestCase
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(title="Task 1", description="Description 1", status="in_progress", due_date="2023-09-30")
        self.task2 = Task.objects.create(title="Task 2", description="Description 2", status="completed", due_date="2023-10-15")

    def test_sort_by_due_date(self):
        response = self.client.get('/api/v1/tasks/sort/?sort_by=due_date')
        self.assertEqual(response.status_code, 200)
        sorted_tasks = response.json()
        self.assertEqual(sorted_tasks['count'], 2)
        
    def test_filter_by_due_date(self):
        response = self.client.get('/api/v1/tasks/filter/?due_date=2023-09-30')
        self.assertEqual(response.status_code, 200)
        sorted_tasks = response.json()
        self.assertEqual(sorted_tasks['count'], 1)
        

