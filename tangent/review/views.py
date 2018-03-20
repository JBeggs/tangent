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
from django.db.models import Q


#Login template used for importing data and login
class LoginTemplateView(TemplateView):
    template_name = "login.html"

#this page should not be used
class IndexTemplateView(ListView):
    model = UserProfile
    template_name = "index.html"

#Dashboard page
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
        user.username        = obj['user']['username']
        user.email           = obj['user']['email']
        user.first_name      = obj['user']['first_name']
        user.last_name       = obj['user']['last_name']
        user.is_active       = obj['user']['is_active']
        user.is_staff        = obj['user']['is_staff']
        user.save()
        user.set_password(obj['user']['username'])
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
        profile.old_id              = obj['user']['id']
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
        review.employee        = UserProfile.objects.get(old_id=obj['employee'])
        review.position        = obj['position']
        review.save()
        #save...

    return HttpResponse(json.dumps(get_value), content_type="application/json")

@csrf_exempt
def search(request):
    #get the data from request
    get_value = request.body

    q=get_value.split("=")[1]
    
    # if the length is 2 or less then get all records
    if len(q)<3:
        users = UserProfile.objects.all()
    else:
        users = UserProfile.objects.filter(Q(user__first_name__icontains=q) | Q(user__last_name__icontains=q) | Q(email__icontains=q)).order_by("user__last_name")

    # html style for query
    html = """    <table id="employee_stats" class="table table-inverse ps" data-plugin="tablesorter">
                        <thead>
                          <tr>
                            <th>#</th>
                            <th>First</th>
                            <th>Last</th>
                            <th>E-mail</th>
                            <th>Phone</th>
                          </tr>
                        </thead>"""

    for user in users:
        html += """    <tbody>
                          <tr>
                            <td>"""+str(user.old_id)+""" </td>
                            <td>"""+str(user.user.first_name)+"""</td>
                            <td>"""+str(user.user.last_name)+"""</td>
                            <td>"""+str(user.email)+"""</td>
                            <td>"""+str(user.phone_number)+"""</td>
                          </tr>
                        </tbody> """ 

    html += """       </table>"""

    return HttpResponse(json.dumps(html), content_type="application/json")

@csrf_exempt
def profile(request):
    #get the data from request
    
    user = UserProfile.objects.get(user__id=request.user.id)

    # html style for query
    html = """    <table id="employee_stats" class="table table-inverse ps" data-plugin="tablesorter">
                        <thead>
                          <tr>
                            <th>#</th>
                            <th>First</th>
                            <th>Last</th>
                            <th>E-mail</th>
                            <th>Phone</th>
                          </tr>
                        </thead>"""

    html += """    <tbody>
                          <tr>
                            <td>"""+str(user.old_id)+""" </td>
                            <td>"""+str(user.user.first_name)+"""</td>
                            <td>"""+str(user.user.last_name)+"""</td>
                            <td>"""+str(user.email)+"""</td>
                            <td>"""+str(user.phone_number)+"""</td>
                          </tr>
                        </tbody> """ 

    html += """       </table>"""
    return HttpResponse(json.dumps(html), content_type="application/json")

