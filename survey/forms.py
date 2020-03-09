from django import forms
from .models import MainSr, Main_Sr_Comm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Main_Sr_Form(forms.ModelForm):
    class Meta:
        modle=MainSr
        exclude=('id','sr_emp' ,'sr_org',)