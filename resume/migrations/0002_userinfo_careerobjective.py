# Generated by Django 4.0.4 on 2022-06-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='CareerObjective',
            field=models.TextField(default=''),
        ),
    ]