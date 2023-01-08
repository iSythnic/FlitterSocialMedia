
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<int:id>", views.profile, name="profile"),

    path("share", views.handle_post, name="handle_post"),
    path("loadfeed", views.handle_feed, name="handle_feed"),
    path("getUserPosts/<int:id>", views.fetch_user_posts, name="fetch_user_posts")
]
