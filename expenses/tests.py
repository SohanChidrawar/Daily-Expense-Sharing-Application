from django.test import TestCase
from django.urls import reverse
from django.urls import reverse, get_resolver
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Expense, ExpenseParticipant

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "email": "john@example.com",
            "name": "John Doe",
            "mobile_number": "1234567890"
        }

    def test_create_user(self):
        #print(get_resolver().reverse_dict)  # Debug print to check all registered URL patterns
        response = self.client.post(reverse('user-list'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, 'john@example.com')

class ExpenseTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email="john@example.com", name="John Doe", mobile_number="1234567890")
        self.expense_data = {
            "description": "Dinner",
            "total_amount": 100.00,
            "expense_type": "equal",
            "created_by": self.user.id,
            "participants": [
                {"User": self.user.id, "amount": 100.00}  # Ensure correct data
            ]
        }

    def test_create_expense(self):
        response = self.client.post(reverse('expense-list'), self.expense_data, format='json')
        print(response.status_code)  # Debug print to check response status code
        print(response.content)  # Debug print to check response content
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Expense.objects.count(), 1)
        self.assertEqual(ExpenseParticipant.objects.count(), 1)
        self.assertEqual(Expense.objects.get().description, 'Dinner')
        self.assertEqual(ExpenseParticipant.objects.get().user, self.user)
