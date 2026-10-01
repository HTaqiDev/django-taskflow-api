from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from tasks.models import Task, Category

class TaskFlowAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='hossein', password='password123')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.category = Category.objects.create(name='Backend Development', description='Python & Django tasks')

    def test_user_registration(self):
        response = self.client.post('/api/auth/register/', {
            'username': 'newdeveloper',
            'password': 'password123',
            'email': 'dev@example.com'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        client = APIClient()
        response = client.post('/api/auth/login/', {
            'username': 'hossein',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_create_task(self):
        response = self.client.post('/api/tasks/', {
            'title': 'Build Django REST API',
            'description': 'Create TaskFlow portfolio project',
            'status': 'in_progress',
            'priority': 'high',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().owner, self.user)

    def test_get_tasks_list(self):
        Task.objects.create(owner=self.user, title='Task 1', status='pending')
        Task.objects.create(owner=self.user, title='Task 2', status='completed')

        response = self.client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_filter_tasks_by_status(self):
        Task.objects.create(owner=self.user, title='Task 1', status='pending')
        Task.objects.create(owner=self.user, title='Task 2', status='completed')

        response = self.client.get('/api/tasks/?status=completed')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['title'], 'Task 2')

    def test_unauthenticated_access_denied(self):
        unauthenticated_client = APIClient()
        response = unauthenticated_client.get('/api/tasks/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
