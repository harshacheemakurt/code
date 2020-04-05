from django.db import models
from datetime import datetime

# Create your models here.

class Quiz(models.Model):
    question = models.TextField(max_length= 250)
    option1= models.TextField(max_length= 50)
    option2 = models.TextField(max_length=50)
    option3 = models.TextField(max_length=50)
    option4 = models.TextField(max_length=50)
    created_date = models.DateTimeField(default= datetime.now)
    is_published = models.BooleanField(default=True)  # to choose which question needs to be displayed
    answers = models.TextField(max_length= 500, blank= True)

    def __str__(self):
        return self.question
