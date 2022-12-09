from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db import models

def filepath(request, filename):
    return f"posts/image/{request.user.id}/{request.id}/{filename}"

def filepathP(request, filename):
    return f"users/{request.user.id}/{request.id}/{filename}"

class User(AbstractUser):
    profileImage = models.ImageField(upload_to=filepathP, null=True, blank=True)
    biography = models.CharField(max_length=150, blank=True)
    def serializeFullProfile(self, requestingUser):
        return {
            "id": self.id,
            "username": self.username, 
            "userimage": (self.profileImage.url if self.profileImage else "None"),
            "followerCount": self.followers.count(),
            "followingCount": self.following.count(),
            "isRequestedUserFollowing": (requestingUser in self.followers.all()),
            "biography": self.biography,
            "isSelf": (requestingUser.id is self.id)
        }

class UserFollowing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    timestap = models.DateTimeField(default=timezone.now())
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'], name="unique_user_following")
        ]

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

    def serializeFeed(self):
        return {
            "id": self.id,
            "username": self.user.username,
            "userimage": (self.user.profileImage.url if self.user.profileImage else "None"),
            "headline": self.headline,
            "likes": self.likes.all().count(),
            "timestamp": self.dateFormat(),
            "image": self.image.url
        }