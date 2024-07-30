#from django.shortcuts import render

#from rest_framework import serializers
from rest_framework import viewsets
from .models import User, Expense
from .serializer import UserSerializer, ExpenseSerializer
from django.http import HttpResponse
import csv

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

    