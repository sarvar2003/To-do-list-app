from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

class Task(models.Model):
    title = models.CharField(max_length=300, blank = True, null = True)
    task = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:]

    def get_absolute_url(self):
        return reverse_lazy('task_list')


# Create your models here.
