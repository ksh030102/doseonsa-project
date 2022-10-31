from distutils.command.upload import upload
from importlib.resources import contents
from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200, null=False)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now=True)

class WebzineContents(models.Model):
    title = models.CharField(max_length=100, null=False)
    contents = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Photo(models.Model):
    post = models.ForeignKey(WebzineContents, on_delete=models.CASCADE, null=True)
    cardnews = models.ImageField(upload_to='images/', null=True)