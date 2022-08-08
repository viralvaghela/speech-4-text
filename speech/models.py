from django.db import models

from django.conf import settings
from django.contrib.auth.models import User

# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=50)
#     score = models.IntegerField(default=0,blank=True)
#     correct_words =models.CharField(max_length=5000,blank=True)

#     def __str__(self):
#         return self.name


class Paragrap(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=5000)

    def __str__(self):
        return self.title


class CorrectWord(models.Model):
    title = models.CharField(max_length=50)
    words = models.CharField(max_length=50)
    points = models.CharField(default=0,max_length=50 )
    grade = models.CharField(max_length=50)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.words
