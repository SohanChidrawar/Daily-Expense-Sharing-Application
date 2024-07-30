
from django.db import models

# User model to store user details
class User(models.Model):
    # represent user in application
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Expense model to store expense details
class Expense(models.Model):
    # represent expenses as per statement
    EXPENSE_TYPE_CHOICES = [
        ('equal', 'Equal'),
        ('exact', 'Exact'),
        ('percentage', 'Percentage')
    ]

    description = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=10, choices=EXPENSE_TYPE_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_expenses')
    participants = models.ManyToManyField(User, through='ExpenseParticipant')

    def __str__(self):
        return self.description
    
    def calculate_splits(self):
        if self.expense_type == 'equal':
            split_amount = self.total_amount / self.participants.count()
            for participant in self.expenseparticipant_set.all():
                participant.amount = split_amount
                participant.save()
        elif self.expense_type == 'percentage':
            for participant in self.expenseparticipant_set.all():
                participant.amount = (self.total_amount * participant.percentage) / 100
                participant.save()
        # For exact splits, amounts are already specified in the creation process in serializer.py

# ExpenseParticipant model to store details of each participant in an expense
class ExpenseParticipant(models.Model):
    # Represents a participant's share in an expense
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # def __str__(self):
    #     return "{self.user.name} - {self.expense.participants}"

    class Meta:
        unique_together = ('user', 'expense')   # Ensures a user can only be part of an expense once

