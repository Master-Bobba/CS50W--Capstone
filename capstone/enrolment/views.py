from re import L
from sqlite3 import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse 

from .models import User, Subject

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "enrolment/index.html")

    # else prompt the user to sign in
    else:
        return render(request, "enrolment/login.html", {
            "message": ""
        })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # if authentication is successful 
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "enrolment/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "enrolment/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        print(request.POST["status"])
        if request.POST["status"] == "choose":
            return render(request, "enrolment/register.html", {
                "message": "Please select 'Student' or 'Professor'!"
            })
        username = request.POST["username"]
        email = request.POST["email"]
        status = request.POST["status"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "enrolment/register.html", {
                "message": "Passwords must match."
            })
        try: 
            user = User.objects.create_user(username, email, password)
            user.status = status
            user.save()
        except IntegrityError:
            return render(request, "enrolment/register.html", {
                "message": "Username already taken!"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "enrolment/register.html")

def timetable(request):
    return render(request, "enrolment/timetable.html")

def enrolment(request):
    student=User.objects.get(username = request.user)
    subjects = Subject.objects.all()
    return render(request, "enrolment/enrolment.html", {
        "subjects": subjects
    })

def moodle(request):
    user = User.objects.get(username = request.user)
    enrolledClasses = Subject.objects.filter(students = user)
    return render(request, "enrolment/moodle.html", {
        "classes": enrolledClasses
    })