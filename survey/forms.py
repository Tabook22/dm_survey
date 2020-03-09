from django import forms
from .models import MainSr, Main_Sr_Comm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Main_Sr_Form(forms.ModelForm):
    class Meta:
        model=MainSr
        exclude=('id','sr_emp',)
        #widgets= ({'sr_org':'form-control', 'placeholder':'الجهة المنظمة للمسح الميداني', 'aria-label':'Orgnizer', 'aria-describedby':'add-orgnizer'})
        