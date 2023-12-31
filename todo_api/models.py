from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default= False, blank= True)
    updated = models.DateField(auto_now=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True)

    def __str__(self) -> str:
        return self.task