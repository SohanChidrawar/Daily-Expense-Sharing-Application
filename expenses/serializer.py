# from rest_framework import serializers
# from .models import User, Expense, ExpenseParticipant

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         # Fields to be serialized for User
#         fields = ['id', 'email', 'name', 'mobile_number']

# class ExpenseParticipantSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExpenseParticipant
#         # Fields to be serialized for Expense Participant
#         fields = ['user', 'amount', 'percentage']

# class ExpenseSerializer(serializers.ModelSerializer):
#     participants = ExpenseParticipantSerializer(many=True)

#     class Meta:
#         model = Expense
#         # field to serialized for expenses
#         fields = ['id', 'description', 'total_amount', 'expense_type', 'created_by', 'participants']

#     def validate(self, data):
#         # Validate that the total percentage for percentage splits adds up to 100
#         if data['expense_type'] == 'percentage':
#             total_percentage = sum(participant['percentage'] for participant in data['participants'])
#             if total_percentage != 100:
#                 raise serializers.ValidationError("Total percentage must equal 100.")
#         return data

#     def create(self, validated_data):
#         # Create an Expense instance and associated ExpenseParticipants
#         participants_data = validated_data.pop('participants')
#         expense = Expense.objects.create(**validated_data)

#         for participant_data in participants_data:
#             ExpenseParticipant.objects.create(expense=expense, **participant_data)
#         return expense

from rest_framework import serializers
from .models import User, Expense, ExpenseParticipant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'mobile_number']

class ExpenseParticipantSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ExpenseParticipant
        fields = ['user', 'amount', 'percentage','User']

class ExpenseSerializer(serializers.ModelSerializer):
    participants = ExpenseParticipantSerializer(many=True)

    class Meta:
        model = Expense
        fields = ['id', 'description', 'total_amount', 'expense_type', 'created_by', 'participants']

    def validate(self, data):
        if data['expense_type'] == 'percentage':
            total_percentage = sum(participant['percentage'] for participant in data['participants'])
            if total_percentage != 100:
                raise serializers.ValidationError("Total percentage must equal 100.")
        return data

    def create(self, validated_data):
        participants_data = validated_data.pop('participants')
        expense = Expense.objects.create(**validated_data)
        for participant_data in participants_data:
            ExpenseParticipant.objects.create(expense=expense, **participant_data)
        return expense

