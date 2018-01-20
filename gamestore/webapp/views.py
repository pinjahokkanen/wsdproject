from django.http import HttpResponse, Http404
from django.shortcuts import render

def index(request):
    return render(request, "webapp/index.html", {})
# Create your views here.
