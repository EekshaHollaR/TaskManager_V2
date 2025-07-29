from django.db import models

class taskBoard(models.Model):
    task_name=models.CharField(max_length=100)
    task_description=models.TextField()

