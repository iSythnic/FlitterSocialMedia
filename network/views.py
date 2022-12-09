from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.db import Error
from .models import *
from django.views.decorators.csrf import csrf_exempt

from .models import User


def index(request):
    return render(request, "network/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def handle_post(request):
    user = request.user
    if request.method != "POST":
        return JsonResponse({"error": "POST request is required"}, status=400)
    elif not user.is_authenticated:
        return JsonResponse({"error": "Forbidden, unauthorized access"}, status=403)

    print(request.POST['CaptionInput'])
    print(request.FILES)
    caption = request.POST['CaptionInput']
    file = request.FILES['FileInput']
    try:
        post = Post(user=user, headline=caption, image=file)
        post.save()
    except Error as er:
        return JsonResponse({"error": er}, status=500)
        
    return JsonResponse({"message": "Sucessfully shared a post"}, status=201)

def handle_feed(request):
    user = request.user
    if request.method != "GET":
        return JsonResponse({"error": "GET request is required"}, status=400)
    elif not user.is_authenticated:
        return JsonResponse({"error": "Not authorized to handle this request"}, status=402)
    try:
        posts = Post.objects.filter(user__in=user.following.all(), timestamp__year=datetime.now().year, timestamp__month=datetime.now().month).order_by("-timestamp")
    except Error as er:
        return JsonResponse({"error": er}, status=500)

    return JsonResponse([post.serializeFeed() for post in posts], status=200, safe=False)

def profile(request, id):
    user = request.user
    if request.method != "GET":
        return JsonResponse({"error": "GET request is required"}, status=400)
    elif not user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    try:
        requestedUser = User.objects.get(id=id)
    except Error as er:
        return JsonResponse({"error": er}, status=500)
    print(requestedUser.serializeFullProfile(user))
    return render(request, "network/profile.html", requestedUser.serializeFullProfile(user))

def fetch_user_posts(request, id):
    user = request.user
    