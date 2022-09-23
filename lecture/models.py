from django.db import models

# Create your models here.

class Lecture(models.Model):
    age = models.CharField(max_length=1000, null=True)
    category = models.CharField(max_length=1000, null=True)
    lectureId = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)
    totalCredits = models.CharField(max_length=1000, null=True)
    nonTotalCredits = models.CharField(max_length=1000, null=True)
    practiceCredits = models.CharField(max_length=1000, null=True)
    time = models.CharField(max_length=1000, null=True)
    room = models.CharField(max_length=1000, null=True)
    professor = models.CharField(max_length=1000, null=True)
    campus = models.CharField(max_length=1000, null=True)
    note = models.CharField(max_length=1000, null=True)


    # age = models.IntegerField()
    # category = models.CharField(max_length=1000, null=True)
    # lectureId = models.CharField(max_length=1000, null=True)
    # name = models.CharField(max_length=1000, null=True)
    # totalCredits = models.IntegerField(null=True)
    # nonTotalCredits = models.IntegerField(null=True)
    # practiceCredits = models.IntegerField(null=True)
    # time = models.CharField(max_length=1000, null=True)
    # room = models.CharField(max_length=1000, null=True)
    # professor = models.CharField(max_length=1000, null=True)
    # campus = models.BooleanField()
    # note = models.CharField(max_length=1000, null=True)