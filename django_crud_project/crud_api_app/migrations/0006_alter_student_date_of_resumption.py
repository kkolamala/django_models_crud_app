# Generated by Django 3.2.2 on 2021-05-09 15:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud_api_app', '0005_alter_student_date_of_resumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_resumption',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]