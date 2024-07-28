# Generated by Django 5.0.4 on 2024-07-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_number', models.CharField(max_length=12)),
                ('instrument', models.CharField(max_length=30)),
            ],
        ),
    ]