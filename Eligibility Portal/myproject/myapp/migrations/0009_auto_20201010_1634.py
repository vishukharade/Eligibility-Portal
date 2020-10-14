# Generated by Django 3.1.1 on 2020-10-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_listquestions_qtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='quizattempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
            ],
            options={
                'db_table': 'quizattempt',
            },
        ),
        migrations.DeleteModel(
            name='List1questions',
        ),
    ]