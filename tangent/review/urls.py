from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from review import views

urlpatterns = [

    ## login not working on django side, looking for a bug...

    # some ajax request stuff
    url(r'^import_employees/$', views.import_employees, name='import_employees'),
    url(r'^import_review/$', views.import_review, name='import_review'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    # Actual pages login and index
    url(r"^login/", views.LoginTemplateView.as_view(), name="login"),
    url("", views.IndexTemplateView.as_view(), name="index"),

# Static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
