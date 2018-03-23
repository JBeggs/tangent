# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Created User Profile models with to ForeignKey's
# Linked to django User and Position...
class Position(models.Model):
    old_id          = models.CharField(max_length=50)
    name            = models.CharField(max_length=50)
    level           = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

# Linked to User and Position
class UserProfile(models.Model):
    old_id              = models.CharField(max_length=50)
    date_added          = models.DateTimeField(auto_now_add=True)
    user                = models.ForeignKey(User, blank=True, null=True)
    position            = models.ForeignKey(Position, blank=True, null=True)
    phone_number        = models.CharField(max_length=50)
    email               = models.CharField(max_length=50)
    github_user         = models.CharField(max_length=50)
    birth_date          = models.CharField(max_length=50)
    gender              = models.CharField(max_length=50)
    race                = models.CharField(max_length=50)
    years_worked        = models.CharField(max_length=50)
    age                 = models.CharField(max_length=50)
    days_to_birthday    = models.CharField(max_length=50)

    def __unicode__(self):
        return self.user.first_name


# Working on review import need some help...
class Group(models.Model):
    name        = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name

# Working on review import need some help...
class Review(models.Model):
    old_id          = models.CharField(max_length=50)
    date            = models.CharField(max_length=50)
    salary          = models.CharField(max_length=50)
    type            = models.CharField(max_length=50)
    employee        = models.CharField(max_length=50)
    position        = models.CharField(max_length=50)
    def __unicode__(self):
        return self.user.position

class Leave(models.Model):
    old_id          = models.CharField(max_length=50)
    employee        = models.CharField(max_length=50)
    start_date      = models.CharField(max_length=50)
    end_date        = models.CharField(max_length=50)
    status          = models.CharField(max_length=50)
    half_day        = models.CharField(max_length=50)
    type            = models.CharField(max_length=50)
    upload          = models.CharField(max_length=50)
    leave_days      = models.CharField(max_length=50)
    def __unicode__(self):
        return self.status

# Working on review import need some help...
class PublicHoliday(models.Model):
    old_id          = models.CharField(max_length=50)
    name            = models.CharField(max_length=50)
    date            = models.CharField(max_length=50)
    unique          = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name + " : " + self.date


class Customer(models.Model):
    old_id              = models.CharField(max_length=50)
    name                = models.CharField(max_length=50)
    code                = models.CharField(max_length=50)
    description         = models.CharField(max_length=50)
    physical_address    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
