from datetime import datetime
from sqlite3 import Timestamp
from time import strftime
from django.contrib.auth.models import AbstractUser
from django.db import models

def filepath(request, filename):
    return f"posts/image/{request.user.id}/{request.id}/{filename}"

def filepathP(request, filename):
    return f"users/{request.user.id}/{request.id}/{filename}"

class User(AbstractUser):
    profileImage = models.ImageField(upload_to=filepathP, null=True, blank=True)
    following = models.ManyToManyField('self', blank=True, related_name="User_follwoing", symmetrical=False)
    followers = models.ManyToManyField('self', blank=True, related_name="User_followers", symmetrical=False)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Comment_user")
    content = models.CharField(max_length=200, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Post_user")
    headline = models.CharField(max_length=500, blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name="Post_likes")
    comments = models.ManyToManyField(Comment, blank=True, related_name="Post_comments")
    image = models.ImageField(upload_to=filepath, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def dateFormat(self):
        time = datetime.now()
        if self.timestamp.day == time.day:
            return f"{time.hour - self.timestamp.hour} hours ago"
        elif self.timestamp.month == time.month:
            return f"{time.day - self.timestamp.day} days ago"
        elif self.timestamp.year == time.year:
            return self.timestamp.strftime("b% %d")
        else:
            return f"{time.year - self.timestamp.year} years ago"

    def serialize(self):
        return {
            "id": self.id,
            "headline": self.headline,
            "likes": self.likes.all().count(),
            "comments": self.comments.all().count(),
            "timestamp": self.dateFormat(),
            "image": self.image.url
        }