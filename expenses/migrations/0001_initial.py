# Generated by Django 4.2 on 2024-07-29 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense_type', models.CharField(choices=[('equal', 'Equal'), ('exact', 'Exact'), ('percentage', 'Percentage')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.expense')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expenses.user')),
            ],
            options={
                'unique_together': {('user', 'expense')},
            },
        ),
        migrations.AddField(
            model_name='expense',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_expenses', to='expenses.user'),
        ),
        migrations.AddField(
            model_name='expense',
            name='participants',
            field=models.ManyToManyField(through='expenses.ExpenseParticipant', to='expenses.user'),
        ),
    ]
