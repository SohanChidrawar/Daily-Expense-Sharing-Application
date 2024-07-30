from rest_framework import serializers
from .models import User, Expense, ExpenseParticipant

# Serializer for User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'mobile_number']

# Serializer for ExpenseParticipant model
class ExpenseParticipantSerializer(serializers.ModelSerializer):
    User = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = ExpenseParticipant
        fields = ['user', 'amount', 'percentage','User']

# Serializer for Expense model
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

    # Overriding the create method to handle nested data
    def create(self, validated_data):
        participants_data = validated_data.pop('participants')        # Extracting participants data
        expense = Expense.objects.create(**validated_data)            # Creating Expense instance
        for participant_data in participants_data:
            ExpenseParticipant.objects.create(expense=expense, **participant_data)      # Creating ExpenseParticipant instances
        return expense

