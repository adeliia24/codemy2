from django.db import models
from django.urls import  reverse
from  datetime import  date, datetime

# Create your models here.
from django.contrib.auth.models import User

class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255, default="CODEMY")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    publ_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return  self.title + '|' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')





