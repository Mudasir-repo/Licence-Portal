# Generated by Django 4.2.15 on 2024-08-20 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licence_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
