from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import MainSr, Main_Sr_Comm,Main_Sr_Qys
from .forms import Main_Sr_Form, QysChoice_Form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
# adding new survey details

@login_required(login_url='/login/') #redirect when user is not logged in
def add_survey(request):
    form = Main_Sr_Form()
    dm_new_survey = MainSr()
    context = {'form': form,
               'msg': "In the Name of God Most Merci Most Mercifull"}

    if request.method == "POST":
        # getting the id of the Place which will be saved. the id will be sent inside a hidden filed from the form
        sremp = request.user
        srorg = request.POST.get("sr_org")
        srloc = request.POST.get("sr_loc")
        srser = request.POST.get("sr_ser")
        srorder = request.POST.get("sr_order")
        srstatus = request.POST.get("sr_status")
        if srstatus == 'true':
            srstatus = True
        elif srstatus == "false":
            srstatus = False

        # adding data to the model
        dm_new_survey = MainSr(sr_emp=sremp, sr_org=srorg, sr_loc=srloc, sr_ser=srser,
                               sr_order=srorder, sr_status=srstatus)
        dm_new_survey.save()

        #here now we are going to add the main questions (true or false questions)

       
        gst_new_survey = Main_Sr_Qys()
        gst_new_survey = Main_Sr_Qys(mid=dm_new_survey,cho_1=False, cho_2=False, cho_3=False, cho_4=False)
        gst_new_survey.save()


        context = {'form': form}
        return render(request, "index.html", context)
    else:
        context = {'form': form,
                   'msg': "الرجاء تعبئة الفورمة"}

    return render(request, "survey/add_survey.html", context)


def survey_list(request):
    pass

#Gust new service this will add guest replies to the survey into the database
def gust_sr(request):
    form = QysChoice_Form()
    gst_new_survey = Main_Sr_Qys()
    context = {'form': form}

    if request.method == "POST":
        # getting the id of the Place which will be saved. the id will be sent inside a hidden filed from the form
        #sremp = request.user
        maid=request.POST.get("mid")
        id=MainSr.objects.get(id=maid)

        cho1 = request.POST.get("cho_1")
        cho2 = request.POST.get("cho_2")
        cho3= request.POST.get("cho_3")
        cho4 = request.POST.get("cho_4")
       
    
        # adding data to the model
        gst_new_survey = Main_Sr_Qys(mid=id,cho_1=False, cho_2=False, cho_3=False, cho_4=False)
        gst_new_survey.save()
        context = {'form': form}
        return render(request, "index.html", context)
    else:
        context = {'form': form,
                   'msg': "الرجاء تعبئة الفورمة"}
        

    return render(request, "survey/gust_sr.html", context)


