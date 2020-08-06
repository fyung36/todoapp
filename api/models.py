from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=255)
   # user = models.ForeignKey(User, on_delete=models.CASCADE())
    task_date = models.DateField(default=False,blank=True,null=True)
    task_time = models.DateTimeField()
    completed = models.BooleanField(default=False, blank=True,null=True)

    def __str__(self):
        return self.task_title