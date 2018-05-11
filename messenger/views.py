from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic

from .models import message


# Show the all the properties in the db.

class messageListView(generic.ListView):
    model = message
    template_name = "messenger/list.html"

class messageDetailView(generic.DetailView):
    model = message
    template_name = "messenger/detail.html"
