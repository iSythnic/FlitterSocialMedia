from distutils.command.upload import upload
from tokenize import blank_re
from django.contrib.auth.models import AbstractUser
from django.db import models

def filepath(request, filename):
    return f"posts/image/{request.user.id}/{request.id}/{filename}"

def filepathP(request, filename):
    return f"users/{request.user.id}/{request.id}/{filename}"

class User(AbstractUser):
    profileImage = models.ImageField(upload_to=filepathP, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment_user")
    content = models.CharField(max_length=200, blank=False)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post_user")
    headline = models.CharField(max_length=500, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="Post_likes")
    comments = models.ManyToManyField(Comment, blank=True, related_name="Post_comments")
    image = models.ImageField(upload_to=filepath, null=True, blank=False)