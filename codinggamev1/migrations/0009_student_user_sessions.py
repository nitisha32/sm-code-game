# Generated by Django 2.1.1 on 2019-08-05 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codinggamev1', '0008_studentperformance_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='user_sessions',
            field=models.TextField(default=''),
        ),
    ]
