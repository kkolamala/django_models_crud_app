# Generated by Django 3.2.2 on 2021-05-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_api_app', '0004_alter_student_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_resumption',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
