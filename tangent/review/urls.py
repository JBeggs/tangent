from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from review import views

urlpatterns = [

# Static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
