from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render

def about(request):
    return render(request, "testiappi/home.html", {})
