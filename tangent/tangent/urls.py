from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from review import views, imports
from django.contrib.auth import views as auth_views

urlpatterns = [

    # some ajax request stuff
    url(r'^import_employees/$', imports.import_employees, name='import_employees'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/$', views.profile, name='profile'),
    # main pages
    url(r"^dashboard/", views.DashboardTemplateView.as_view(), name="dashboard"),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^', admin.site.urls),
    url("", views.DashboardTemplateView.as_view(), name="dashboard"),

# Static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
