# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
# needed for requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
#import my models
from review.models import UserProfile,User,Position, Review
#a few more tools that I might need
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView,ListView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json

#Login template used for importing data and login
class LoginTemplateView(TemplateView):
    template_name = "login.html"

#Display basic data.
#Not finished need to fix login user display
#Not happy with html layout and implementation
#Using list few and correctly pulling relationship data
class IndexTemplateView(ListView):
    model = UserProfile
    template_name = "index.html"


class DashboardTemplateView(ListView):
    model = UserProfile
    template_name = "dashboard.html"

# Import the users from request
@csrf_exempt
def import_employees(request):
    #get the data from the request
    get_value = json.loads(request.body)

    #kill previous users...and there relationship models
    UserProfile.objects.all().delete()
    Position.objects.all().delete()
    User.objects.all().delete()

    #there are only a few users so this works
    for obj in get_value:
        #add data to new User object
        user                 = User()
        user.old_id          = obj['user']['id']
        user.username        = obj['user']['username']
        user.email           = obj['user']['email']
        user.first_name      = obj['user']['first_name']
        user.last_name       = obj['user']['last_name']
        user.is_active       = obj['user']['is_active']
        user.is_staff        = obj['user']['is_staff']
        user.save()
        #add the data to new Position object
        position                 = Position()
        position.old_id          = obj['position']['id']
        position.name            = obj['position']['name']
        position.level           = obj['position']['level']
        position.save()
        #add the data to new UserProfile object
        profile                     = UserProfile()
        #Add the relationships...
        #I need to be doing this everyday...
        profile.user                = user
        profile.position            = position
        profile.phone_number        = obj['phone_number']
        profile.email               = obj['email']
        profile.github_user         = obj['github_user']
        profile.birth_date          = obj['birth_date']
        profile.gender              = obj['gender']
        profile.race                = obj['race']
        profile.years_worked        = obj['years_worked']
        profile.age                 = obj['age']
        profile.days_to_birthday    = obj['days_to_birthday']
        profile.save()
        #Dont forget to save

    return HttpResponse(json.dumps(get_value), content_type="application/json")

# Import the reviews from request
@csrf_exempt
def import_review(request):
    #get the data from request
    get_value = json.loads(request.body)
    #delete old records
    Review.objects.all().delete()
    #loop and import
    for obj in get_value:
        review                 = Review()
        review.date            = obj['date']
        review.salary          = obj['salary']
        review.type            = obj['type']
        review.employee        = obj['employee']
        review.position        = obj['position']
        review.save()
        #save...

    return HttpResponse(json.dumps(get_value), content_type="application/json")

# Hack to login user
# Not working to well
@csrf_exempt
def login_user(request):


    for obj in request.GET:
        user = obj.replace('"',"")

    u = User.objects.get(username=user)
    u.set_password(user)
    u.save()

    user = authenticate(username=user, password=user)

    return HttpResponse(json.dumps({"url":"/"}), content_type="application/json")

