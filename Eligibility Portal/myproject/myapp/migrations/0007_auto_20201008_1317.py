# Generated by Django 3.1.1 on 2020-10-08 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_finalresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finalresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('div', models.CharField(max_length=100)),
                ('strtime', models.CharField(max_length=100)),
                ('endtime', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Finalresults',
            },
        ),
        migrations.DeleteModel(
            name='Finalresult',
        ),
    ]
