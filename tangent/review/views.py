# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.template.response import TemplateResponse



class LoginTemplateView(TemplateView):
    template_name = "login.html"

class LogoutTemplateView(TemplateView):
    template_name = "logout.html"

class IndexTemplateView(TemplateView):
    template_name = "index.html"
