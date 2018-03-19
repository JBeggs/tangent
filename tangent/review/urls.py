from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from review import views
from tangent.urls import urlpatterns


urlpatterns += [

    url("", views.IndexTemplateView.as_view(), name="index"),

]
