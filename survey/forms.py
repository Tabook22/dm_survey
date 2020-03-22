from django import forms
from django.urls import reverse
from .models import MainSr, MainSr2, Main_Sr_Comm, ServiceProvider, Service, Main_Sr_Qys
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Row, Column, Field, HTML, Fieldset
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class Main_Sr_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Main_Sr_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        #self.helper.form_action = reverse('survey:survey_list')
        # self.helper.layout = Layout(
        #     Row(
        #         Column('sr_org', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_loc', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_ser', css_class='form-group col-md-6 mb-0'),
        #         Column('sr_status', css_class='form-group col-md-6 mb-0'),
        #         css_class='form-row'
        #     ),
        #     Row(
        #         Column('sr_order', css_class='form-group col-md-12 mb-0'),
        #         css_class='form-row'
        #     ),
        #     # Row(
        #     #     Column('un',css_class='form-group col-md-12 mb-0'),
        #     #     css_class='form-row'
        #     # ),
        #     Submit('submit', 'Add area(s) of experties')
        # )

    class Meta:
        model = MainSr
        fields = [
            'sr_org',
            'sr_loc',
            'sr_desc',
        ]


class Main_Sr2_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Main_Sr2_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self) # the form helper objects tells crispy form  that we need to wrap our form object in form tags
        self.helper.form_method = 'post'
        self.helper.form_show_labels = True

        
    class Meta:
        model = MainSr2
        # widgets={
        #     'sr_ser':forms.TextInput(attrs={'class':'form-control', 'placeholder':'الخدمة'}),
        #     'cho_1'
        # }
        fields = [
            'mid',
            'gstId',
            'sr_order',
            'sr_status',
            'sr_ser1',
            'cho1_1',
            'sr_ser2',
            'cho2_1',         
            'sr_ser3',
            'cho3_1',
            'sr_ser4',
            'cho4_1',
            'sr_ser5',
            'cho5_1',
            'sr_ser6',
            'cho6_1',
            'sr_ser7',
            'cho7_1',
            'sr_ser8',
            'cho8_1',
            'sr_ser9',
            'cho9_1',
            'sr_ser10',
            'cho10_1',
            'sr_ser11',
            'cho11_1',
            'sr_ser12',
            'cho12_1',
            'sr_ser13',
            'cho13_1',
            'sr_ser14',
            'cho14_1',
            'sr_ser15',
            'cho15_1',
            'sr_ser16',
            'cho16_1',
            'sr_ser17',
            'sr_ser18',
            'cho18_1',
            'sr_ser19',
            'cho19_1',
            'sr_ser20',
            'cho20_1',
            'sr_ser21',
            'cho21_1',
            'sr_ser22',
            'gst_comm',
        ]
        widgets ={
            'mid':forms.HiddenInput(),
            'gstId':forms.HiddenInput(),
            'sr_ser1':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'cho1_1':forms.RadioSelect(attrs={'type':'radio' ,'name':'cho1_1','style':'min-width:100px'}),
            'sr_ser2':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser3':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser4':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser5':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser6':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser7':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser8':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser9':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser10':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser11':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser12':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser13':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser14':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser15':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser16':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser17':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser18':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser19':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser20':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser21':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'sr_ser22':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
            'gst_comm':forms.Textarea(attrs={'col':'40','row':'10','class': 'form-control','dir':'rtl'}),
        }



class ServiceProvider_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ServiceProvider_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
  
    class Meta:
        model = ServiceProvider
        fields = [
            'mid',
            'pro_title',
            'pro_desc',
        ]


class Service_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Service_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
  
    class Meta:
        model = Service
        fields = [
            'spid',
            'ser_title',
            'ser_desc',
        ]

class QysChoice_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QysChoice_Form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        #self.helper.form_show_labels = False #this is used to remove all labels, if you want to do the labeling your-self
    class Meta:
        model = Main_Sr_Qys
        fields = [
            'mid',
            'cho_1',
            'cho_2',
            'cho_3',
            'cho_4',
        ]
