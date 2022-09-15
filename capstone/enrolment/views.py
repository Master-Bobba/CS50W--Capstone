from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse 

from .models import User



# Create your views here.
def index(request):
    if request.user.is_authenticated:
        pass # return render home page
    
    # else prompt the user to sign in
    else:
        pass