from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)