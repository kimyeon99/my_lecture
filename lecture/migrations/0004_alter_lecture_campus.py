# Generated by Django 4.0.3 on 2022-09-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_alter_lecture_campus_alter_lecture_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='campus',
            field=models.BooleanField(max_length=1000),
        ),
    ]
