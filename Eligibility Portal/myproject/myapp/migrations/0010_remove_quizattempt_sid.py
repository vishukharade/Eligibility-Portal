# Generated by Django 3.1.1 on 2020-10-10 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20201010_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizattempt',
            name='sid',
        ),
    ]
