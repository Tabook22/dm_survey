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
        cho12=request.POST.get('cho1_2')
        cho13=request.POST.get('cho1_3')
        cho14=request.POST.get('cho1_4')
        srser2=request.POST.get('sr_ser2')
        cho21=request.POST.get('cho2_1')
        cho22=request.POST.get('cho2_2')
        cho23=request.POST.get('cho12_3')
        cho24=request.POST.get('cho2_4')
        srser3=request.POST.get('sr_ser3')
        cho31=request.POST.get('cho3_1')
        cho32=request.POST.get('cho3_2')
        cho33=request.POST.get('cho3_3')
        cho34=request.POST.get('cho3_4')
        srser4=request.POST.get('sr_ser4')
        cho41=request.POST.get('cho4_1')
        cho42=request.POST.get('cho4_2')
        cho43=request.POST.get('cho4_3')
        cho44=request.POST.get('cho4_4')
        srser5=request.POST.get('sr_ser1')
        cho51=request.POST.get('cho5_1')
        cho52=request.POST.get('cho5_2')
        cho53=request.POST.get('cho5_3')
        cho54=request.POST.get('cho5_4')
        srser6=request.POST.get('sr_ser1')
        cho61=request.POST.get('cho6_1')
        cho62=request.POST.get('cho6_2')
        cho63=request.POST.get('cho6_3')
        cho64=request.POST.get('cho6_4')
        srser7=request.POST.get('sr_ser7')
        cho71=request.POST.get('cho7_1')
        cho72=request.POST.get('cho7_2')
        cho73=request.POST.get('cho7_3')
        cho74=request.POST.get('cho7_4')
        srser8=request.POST.get('sr_ser8')
        cho81=request.POST.get('cho8_1')
        cho82=request.POST.get('cho8_2')
        cho83=request.POST.get('cho8_3')
        cho84=request.POST.get('cho8_4')
        srser9=request.POST.get('sr_ser9')
        cho91=request.POST.get('cho9_1')
        cho92=request.POST.get('cho9_2')
        cho93=request.POST.get('cho9_3')
        cho94=request.POST.get('cho9_4')
        srser10=request.POST.get('sr_ser10')
        cho101=request.POST.get('cho10_1')
        cho102=request.POST.get('cho10_2')
        cho103=request.POST.get('cho10_3')
        cho104=request.POST.get('cho10_4')
        srser11=request.POST.get('sr_ser11')
        cho111=request.POST.get('cho11_1')
        cho112=request.POST.get('cho11_2')
        cho113=request.POST.get('cho11_3')
        cho114=request.POST.get('cho11_4')
        srser12=request.POST.get('sr_ser12')
        cho121=request.POST.get('cho12_1')
        cho122=request.POST.get('cho12_2')
        cho123=request.POST.get('cho12_3')
        cho124=request.POST.get('cho12_4')
        srser13=request.POST.get('sr_ser13')
        cho131=request.POST.get('cho13_1')
        cho132=request.POST.get('cho13_2')
        cho133=request.POST.get('cho13_3')
        cho134=request.POST.get('cho13_4')
        srser14=request.POST.get('sr_ser1')
        cho141=request.POST.get('cho14_1')
        cho142=request.POST.get('cho14_2')
        cho143=request.POST.get('cho14_3')
        cho144=request.POST.get('cho14_4')
        srser15=request.POST.get('sr_ser15')
        cho151=request.POST.get('cho15_1')
        cho152=request.POST.get('cho15_2')
        cho153=request.POST.get('cho15_3')
        cho154=request.POST.get('cho15_4')
        srser16=request.POST.get('sr_ser16')
        cho161=request.POST.get('cho16_1')
        cho162=request.POST.get('cho16_2')
        cho163=request.POST.get('cho16_3')
        cho164=request.POST.get('cho16_4')
        srser17=request.POST.get('sr_ser17')
        cho171=request.POST.get('cho17_1')
        cho172=request.POST.get('cho17_2')
        cho173=request.POST.get('cho17_3')
        cho174=request.POST.get('cho17_4')
        srser18=request.POST.get('sr_ser18')
        cho181=request.POST.get('cho18_1')
        cho182=request.POST.get('cho18_2')
        cho183=request.POST.get('cho18_3')
        cho184=request.POST.get('cho18_4')
        srser19=request.POST.get('sr_ser19')
        cho191=request.POST.get('cho19_1')
        cho192=request.POST.get('cho19_2')
        cho193=request.POST.get('cho19_3')
        cho194=request.POST.get('cho19_4')
        srser20=request.POST.get('sr_ser20')
        cho201=request.POST.get('cho20_1')
        cho202=request.POST.get('cho20_2')
        cho203=request.POST.get('cho20_3')
        cho204=request.POST.get('cho20_4')
        srser21=request.POST.get('sr_ser21')
        cho211=request.POST.get('cho21_1')
        cho212=request.POST.get('cho21_2')
        cho213=request.POST.get('cho21_3')
        cho214=request.POST.get('cho21_4')
        srser22=request.POST.get('sr_ser22')
        gstcomm=request.POST.get('gst_comm')
        #get MainSr active Survery
        gstmid=MainSr.objects.get(sr_status=True)
        gst_id=request.POST.get('gstId')

        gstrsp=MainSr2(
            sr_ser1=srser1,
            cho1_1=cho11,
            cho1_2=cho12,
            cho1_3=cho13,
            cho1_4=cho14,
            sr_ser2=srser2,
            cho2_1=cho21,
            cho2_2=cho22,
            cho2_3=cho23,
            cho2_4=cho24,
            sr_ser3=srser3,
            cho3_1=cho31,
            cho3_2=cho32,
            cho3_3=cho33,
            cho3_4=cho34,
            sr_ser4=srser4,
            cho4_1=cho41,
            cho4_2=cho42,
            cho4_3=cho43,
            cho4_4=cho44,
            sr_ser5=srser5,
            cho5_1=cho51,
            cho5_2=cho52,
            cho5_3=cho53,
            cho5_4=cho54,
            sr_ser6=srser6,
            cho6_1=cho61,
            cho6_2=cho62,
            cho6_3=cho63,
            cho6_4=cho64,
            sr_ser7=srser7,
            cho7_1=cho71,
            cho7_2=cho72,
            cho7_3=cho73,
            cho7_4=cho74,
            sr_ser8=srser8,
            cho8_1=cho81,
            cho8_2=cho82,
            cho8_3=cho83,
            cho8_4=cho84,
            sr_ser9=srser9,
            cho9_1=cho91,
            cho9_2=cho92,
            cho9_3=cho93,
            cho9_4=cho94,
            sr_ser10=srser10,
            cho10_1=cho101,
            cho10_2=cho102,
            cho10_3=cho103,
            cho10_4=cho104,
            sr_ser11=srser11,
            cho11_1=cho111,
            cho11_2=cho112,
            cho11_3=cho113,
            cho11_4=cho114,
            sr_ser12=srser12,
            cho12_1=cho121,
            cho12_2=cho122,
            cho12_3=cho123,
            cho12_4=cho124,
            sr_ser13=srser13,
            cho13_1=cho131,
            cho13_2=cho132,
            cho13_3=cho133,
            cho13_4=cho134,
            sr_ser14=srser14,
            cho14_1=cho141,
            cho14_2=cho142,
            cho14_3=cho143,
            cho14_4=cho144,
            sr_ser15=srser15,
            cho15_1=cho151,
            cho15_2=cho152,
            cho15_3=cho153,
            cho15_4=cho154,
            sr_ser16=srser16,
            cho16_1=cho161,
            cho16_2=cho162,
            cho16_3=cho163,
            cho16_4=cho164,
            sr_ser17=srser17,
            cho17_1=cho171,
            cho17_2=cho172,
            cho17_3=cho173,
            cho17_4=cho174,
            sr_ser18=srser18,
            cho18_1=cho181,
            cho18_2=cho182,
            cho18_3=cho183,
            cho18_4=cho184,
            sr_ser19=srser19,
            cho19_1=cho191,
            cho19_2=cho192,
            cho19_3=cho193,
            cho19_4=cho194,
            sr_ser20=srser20,
            cho20_1=cho201,
            cho20_2=cho202,
            cho20_3=cho203,
            cho20_4=cho204,
            sr_ser21=srser21,
            cho21_1=cho211,
            cho21_2=cho212,
            cho21_3=cho213,
            cho21_4=cho214,
            sr_ser22=srser22,
            gst_comm=gstcomm,
            mid=gstmid,
            gstId=gst_id
            )
        gstrsp.save()
        return render(request, "survey/gust_sr.html", context)
    else:
        #here we are trying to generate a random gust id to put it inside th survery because each gust must have a gust id to participate in the survey
        #generate a random gust numbers based on current time, to be used as gust id  
        dateTimeObj=datetime.now()
        timestampStr = dateTimeObj.strftime("%d%m%Y%H%M%S%f")
        #ctm=datetime.datetime.now().time()
        gstId=timestampStr

        #here i want to get the id of the active suvery from MainSr model
        getActSr=MainSr.objects.get(sr_status=True)
        context = {'form': form,
                    'srgstId':gstId,
                    'mid':getActSr.id}
    return render(request, "survey/gust_sr.html", context)


