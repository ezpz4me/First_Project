# Generated by Django 4.0.4 on 2022-04-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_alter_signup_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
