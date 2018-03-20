# Generated by Django 2.0.3 on 2018-03-20 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=32)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(default=1)),
                ('fields', models.TextField()),
                ('table', models.CharField(max_length=16, unique=True)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=64)),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
