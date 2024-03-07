from django.urls import path, include
from rosters import views

urlpatterns = [
    path("", views.home, name="home"),
    path("partial/", views.my_partial_view, name="my_partial"),
    path("create_roster/", views.create_roster, name="create_roster"),
]
