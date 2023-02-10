from django.db import models


# Create your models here.

class Calculation(models.Model):
    """Track a calculation and its results"""

    input = models.IntegerField()
    output = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class PeriodicTaskCreation(models.Model):
    task_name = models.CharField(max_length=255)
    task_date_time = models.DateTimeField()
