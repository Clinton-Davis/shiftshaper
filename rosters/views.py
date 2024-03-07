from django.http import HttpResponse
from django.shortcuts import render

from rosters.forms import RosterForm


def home(request):
    form = RosterForm()
    context = {"form": form}
    return render(request, "home.html", context)


def my_partial_view(request):
    return HttpResponse("<p>This is a partial response loaded with HTMX.</p>")


def create_roster(request):
    if request.method == "POST":
        form = RosterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Roster created successfully")
    else:
        form = RosterForm()
    context = {"form": form}
    return render(request, "home.html", context)
