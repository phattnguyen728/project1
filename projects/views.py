from django.shortcuts import render
from projects.models import Project

# Create your views here.

def projects_list(request):
    list = Project.objects.all()
    context = {
        "list": list,
    }
    return render(request, "projects/list.html", context)
