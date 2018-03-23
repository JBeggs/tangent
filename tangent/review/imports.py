# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
# needed for requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
#import my models
from review.models import UserProfile,User,Position, Review, Leave, Customer, Group, PublicHoliday
#a few more tools that I might need
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView,ListView
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate
import json
from django.db.models import Q


# Import the users from request
@csrf_exempt
def import_employees(request):
    #get the data from the request
    get_value = json.loads(request.body)

    if 'user' in get_value[0]:
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



    elif 'salary' and 'employee' and 'position' in get_value[0]:
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


    elif 'leave_days' and 'half_day' in get_value[0]:
        #delete old records
        Leave.objects.all().delete()
        #loop and import
        for obj in get_value:
            leave                 = Leave()
            Leave.old_id          = obj['id']
            Leave.employee        = obj['employee']
            Leave.start_date      = obj['start_date']
            Leave.end_date        = obj['end_date']
            Leave.status          = obj['status']
            Leave.half_day        = obj['half_day']
            Leave.type            = obj['type']
            Leave.upload          = obj['upload']
            Leave.leave_days      = obj['leave_days']
            leave.save()


    elif 'unique' and 'date' in get_value[0]:

        #delete old records
        PublicHoliday.objects.all().delete()
        #loop and import
        for obj in get_value:
            holiday         = PublicHoliday()
            holiday.old_id  = obj['id']
            holiday.name    = obj['name']
            holiday.date    = obj['date']
            holiday.unique  = obj['unique']
            holiday.save()


    elif 'code' and 'description' in get_value[0]:

        #delete old records
        Customer.objects.all().delete()
        #loop and import
        for obj in get_value:
            customer                    = Customer()
            customer.old_id             = obj['id']
            customer.code               = obj['code']
            customer.name               = obj['name']
            customer.description        = obj['description']
            customer.physical_address   = obj['physical_address']
            customer.save()


    elif 'url' and 'name' in get_value[0]:

        #delete old records
        Group.objects.all().delete()
        #loop and import
        for obj in get_value:
            holiday         = Group()
            holiday.name    = obj['name']
            holiday.save()




    return HttpResponse(json.dumps(get_value), content_type="application/json")
