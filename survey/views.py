from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import MainSr, MainSr2, Main_Sr_Comm,Main_Sr_Qys
from .forms import Main_Sr_Form, QysChoice_Form,Main_Sr2_Form
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime
from dateutil import tz
from django.forms.models import model_to_dict


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
        else:
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
    form=Main_Sr2_Form()
    
    if request.method=="POST":
        context = {'form': form}
        srser1=request.POST.get('sr_ser1')
        cho11=request.POST.get('cho1_1')
        srser2=request.POST.get('sr_ser2')
        cho21=request.POST.get('cho2_1')
        srser3=request.POST.get('sr_ser3')
        cho31=request.POST.get('cho3_1')
        srser4=request.POST.get('sr_ser4')
        cho41=request.POST.get('cho4_1')
        srser5=request.POST.get('sr_ser1')
        cho51=request.POST.get('cho5_1')
        srser6=request.POST.get('sr_ser1')
        cho61=request.POST.get('cho6_1')
        srser7=request.POST.get('sr_ser7')
        cho71=request.POST.get('cho7_1')
        srser8=request.POST.get('sr_ser8')
        cho81=request.POST.get('cho8_1')
        srser9=request.POST.get('sr_ser9')
        cho91=request.POST.get('cho9_1')
        srser10=request.POST.get('sr_ser10')
        cho101=request.POST.get('cho10_1')
        srser11=request.POST.get('sr_ser11')
        cho111=request.POST.get('cho11_1')
        srser12=request.POST.get('sr_ser12')
        cho121=request.POST.get('cho12_1')
        srser13=request.POST.get('sr_ser13')
        cho131=request.POST.get('cho13_1')
        srser14=request.POST.get('sr_ser1')
        cho141=request.POST.get('cho14_1')
        srser15=request.POST.get('sr_ser15')
        cho151=request.POST.get('cho15_1')
        srser16=request.POST.get('sr_ser16')
        cho161=request.POST.get('cho16_1')
        srser17=request.POST.get('sr_ser17')
        cho171=request.POST.get('cho17_1')
        srser18=request.POST.get('sr_ser18')
        cho181=request.POST.get('cho18_1')
        srser19=request.POST.get('sr_ser19')
        cho191=request.POST.get('cho19_1')
        srser20=request.POST.get('sr_ser20')
        cho201=request.POST.get('cho20_1')
        srser21=request.POST.get('sr_ser21')
        cho211=request.POST.get('cho21_1')
        srser22=request.POST.get('sr_ser22')
        gstcomm=request.POST.get('gst_comm')
        #get MainSr active Survery
        gstmid=MainSr.objects.get(sr_status=True)
        gst_id=request.POST.get('gstId')
        print("============================")
        print(cho21)
        gstrsp=MainSr2(
            sr_ser1=srser1,
            cho1_1=cho11,
            sr_ser2=srser2,
            cho2_1=cho21,
            sr_ser3=srser3,
            cho3_1=cho31,
            sr_ser4=srser4,
            cho4_1=cho41,
            sr_ser5=srser5,
            cho5_1=cho51,
            sr_ser6=srser6,
            cho6_1=cho61,
            sr_ser7=srser7,
            cho7_1=cho71,
            sr_ser8=srser8,
            cho8_1=cho81,
            sr_ser9=srser9,
            cho9_1=cho91,
            sr_ser10=srser10,
            cho10_1=cho101,
            sr_ser11=srser11,
            cho11_1=cho111,
            sr_ser12=srser12,
            cho12_1=cho121,
            sr_ser13=srser13,
            cho13_1=cho131,
            sr_ser14=srser14,
            cho14_1=cho141,
            sr_ser15=srser15,
            cho15_1=cho151,
            sr_ser16=srser16,
            cho16_1=cho161,
            sr_ser17=srser17,
            cho17_1=cho171,
            sr_ser18=srser18,
            cho18_1=cho181,
            sr_ser19=srser19,
            cho19_1=cho191,
            sr_ser20=srser20,
            cho20_1=cho201,
            sr_ser21=srser21,
            cho21_1=cho211,
            sr_ser22=srser22,
            gst_comm=gstcomm,
            mid=gstmid,
            gstId=gst_id
            )
        gstrsp.save()
        return render(request, "index.html")
    else:
        #here we are trying to generate a random gust id to put it inside th survery because each gust must have a gust id to participate in the survey
        #generate a random gust numbers based on current time, to be used as gust id  
        dateTimeObj=datetime.now()
        timestampStr = dateTimeObj.strftime("%d%m%Y%H%M%S%f")
        #ctm=datetime.datetime.now().time()
        gstId=timestampStr

        #here i want to get the id of the active suvery from MainSr model
        getActSr=MainSr2.objects.get(gstId=1234)
        my_dict2={}
        my_dict = getActSr.__dict__
        my_dict2={'sr_ser1':my_dict['sr_ser1'],
        'sr_ser1':my_dict['sr_ser1'],
        'sr_ser2':my_dict['sr_ser2'],
        'sr_ser3':my_dict['sr_ser3'],
        'sr_ser4':my_dict['sr_ser14'],
        'sr_ser5':my_dict['sr_ser5'],
        'sr_ser6':my_dict['sr_ser6'],
        'sr_ser7':my_dict['sr_ser7'],
        'sr_ser8':my_dict['sr_ser8'],
        'sr_ser9':my_dict['sr_ser9'],
        'sr_ser10':my_dict['sr_ser10'],
        'sr_ser11':my_dict['sr_ser11'],
        'sr_ser12':my_dict['sr_ser12'],
        'sr_ser13':my_dict['sr_ser13'],
        'sr_ser14':my_dict['sr_ser14'],
        'sr_ser15':my_dict['sr_ser15'],
        'sr_ser16':my_dict['sr_ser16'],
        'sr_ser17':my_dict['sr_ser17'],
        'sr_ser18':my_dict['sr_ser18'],
        'sr_ser19':my_dict['sr_ser19'],
        'sr_ser20':my_dict['sr_ser20'],
        'sr_ser21':my_dict['sr_ser21'],
        }
        context = {'form': form,
                    'srgstId':gstId,
                    'mid':getActSr.id,
                    'my_dict2':my_dict2,
                    'getActSr':getActSr}
    return render(request, "survey/gust_sr.html", context)


