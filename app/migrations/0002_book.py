# Generated by Django 4.0.4 on 2022-06-10 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('Book_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Author_name', models.CharField(max_length=100)),
                ('Publish_date', models.DateField()),
            ],
        ),
    ]
