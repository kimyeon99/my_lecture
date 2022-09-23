# Generated by Django 4.0.3 on 2022-09-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_alter_lecture_campus_alter_lecture_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecture',
            name='campus',
            field=models.BooleanField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='category',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='lectureId',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='name',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='nonTotalCredits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='practiceCredits',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='professor',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='room',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='time',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='totalCredits',
            field=models.IntegerField(null=True),
        ),
    ]
