# Generated by Django 3.1.1 on 2020-10-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_list1questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='list1questions',
            name='correct',
            field=models.CharField(default='A', max_length=500),
        ),
        migrations.AddField(
            model_name='listquestions',
            name='correct',
            field=models.CharField(default='A', max_length=500),
        ),
    ]
