# Generated by Django 2.1.1 on 2019-08-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codinggamev1', '0006_auto_20190803_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='codingq',
            name='secondary_target_positions',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]