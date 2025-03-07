from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)

def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)

def registration(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    name = request.POST.get("username")
    password = request.POST.get("password")
    if name is None or password is None:
        return render(request, 'djangoapp/index.html')
    u = authenticate(request, username=name, password=password)
    login(request, u)
    return render(request, 'djangoapp/index.html')


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return render(request, 'djangoapp/index.html')
# ...

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    name = request.POST.get("username")
    first_name = request.POST.get("firstname")
    last_name = request.POST.get("lastname")
    password = request.POST.get("password")

    if name is None or password is None or first_name is None or last_name is None:
        print("Some data missing")
        print(name, first_name, last_name, password)
        return redirect("/djangoapp")

    u = authenticate(request, username=name, password=password)
    if u is None:
        print("user doesn't exist yet")
        new_user = User.objects.create_user(username=name, first_name=first_name, last_name=last_name, password=password, ).save()
        login(request, new_user)
        return redirect("/djangoapp")
    else:
        print("user already in db")
        login(request, u)
        return redirect("/djangoapp")
        



# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

