from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add_survey(request):
    return render(request,"survey/add_survey.html")

