from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import MainSr,Main_Sr_Comm
from .forms import Main_Sr_Form

# Create your views here.

def add_survey(request):
    form=Main_Sr_Form()
    if request.method=="POST":
        context={'msg':'In the name of god most merci most mercifull'}
        if form.is_valid():
            dm_new_survey=MainSr(text=form.cleaned_data['text'])
            dm_new_survey.save()
            return redirect('index')
    else:
        context={'form':form,
                 'msg':"In the Name of God Most Merci Most Mercifull",
                 'srorg':'Dhofar mainicipility'}
        
    return render(request,"survey/add_survey.html",context)

