"""
URL configuration for tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#V1
from django.shortcuts import redirect
#V2
# from django.views.generic import RedirectView


def redirect_home(request):
    return redirect("list_projects")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    # path("tasks/", include("tasks.urls")),
     #V1
    path("", redirect_home, name="home"),
    path("projects/", include("projects.urls")),

    # V2
    # path("", RedirectView.as_view(pattern_name="home", permanent=True), name='home'),
]
