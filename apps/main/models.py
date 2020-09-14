from django.db import models

from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/post')
    create_date = models.DateTimeField(auto_now_add=True)
    post_date = models.DateTimeField()
    last_update = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=255)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' posted by ' + str(self.author)
