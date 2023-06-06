from django.urls import path, include
from projects.views import(
    projects_list,
    show_project,
)


urlpatterns = [
    path("", projects_list, name="list_projects"),
    # path("", projects_list, name="home"),
    path("<int:id>", show_project, name="show_project"),
]
