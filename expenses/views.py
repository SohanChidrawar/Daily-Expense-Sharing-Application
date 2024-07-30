from rest_framework import generics
from rest_framework import viewsets
from .models import User, Expense
from .serializer import UserSerializer, ExpenseSerializer
from django.http import HttpResponse
import csv

# API view to create and list users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# API view to retrieve user details
class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()  # Queryset to get user details
    serializer_class = UserSerializer  # Serializer to use for this view

# API view to create and list user expense
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        return Expense.objects.prefetch_related('participants')

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def download_balance_sheet(self, request, pk=None):
        expense = self.get_object()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="balance_sheet_{expense.id}.csv"'
        writer = csv.writer(response)
        writer.writerow(['User', 'Amount', 'Percentage'])
        for participant in expense.participants.all():
            writer.writerow([participant.user.name, participant.amount, participant.percentage])
        return response
    
# API view to retrieve individual user expenses
class UserExpenseListView(generics.ListAPIView):
    serializer_class = ExpenseSerializer  # Serializer to use for this view

    # Filtering expenses by user
    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Extracting user_id from URL
        return Expense.objects.filter(created_by_id=user_id)  # Filtering expenses by created_by field

    
