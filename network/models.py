from distutils.command.upload import upload
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment_user")
    content = models.CharField(max_length=200, blank=False)

def filepath(request, filename):
    return f"posts/image/{request.user.id}/{request.id}/{filename}"

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post_user")
    headline = models.CharField(max_length=200, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="Post_likes")
    comments = models.ManyToManyField(Comment, blank=True, related_name="Post_comments")
    image = models.ImageField(upload_to=filepath, null=True, blank=False)