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
            'cho1_2',
            'cho1_3',
            'cho1_4',
            'sr_ser2',
            'cho2_1',
            'cho2_2',
            'cho2_3',
            'cho2_4',         
            'sr_ser3',
            'cho3_1',
            'cho3_2',
            'cho3_3',
            'cho3_4',
            'sr_ser4',
            'cho4_1',
            'cho4_2',
            'cho4_3',
            'cho4_4',
            'sr_ser5',
            'cho5_1',
            'cho5_2',
            'cho5_3',
            'cho5_4',
            'sr_ser6',
            'cho6_1',
            'cho6_2',
            'cho6_3',
            'cho6_4',
            'sr_ser7',
            'cho7_1',
            'cho7_2',
            'cho7_3',
            'cho7_4',
            'sr_ser8',
            'cho8_1',
            'cho8_2',
            'cho8_3',
            'cho8_4',
            'sr_ser9',
            'cho9_1',
            'cho9_2',
            'cho9_3',
            'cho9_4',
            'sr_ser10',
            'cho10_1',
            'cho10_2',
            'cho10_3',
            'cho10_4',
            'sr_ser11',
            'cho11_1',
            'cho11_2',
            'cho11_3',
            'cho11_4',
            'sr_ser12',
            'cho12_1',
            'cho12_2',
            'cho12_3',
            'cho12_4',
            'sr_ser13',
            'cho13_1',
            'cho13_2',
            'cho13_3',
            'cho13_4',
            'sr_ser14',
            'cho14_1',
            'cho14_2',
            'cho14_3',
            'cho14_4',
            'sr_ser15',
            'cho15_1',
            'cho15_2',
            'cho15_3',
            'cho15_4',
            'sr_ser16',
            'cho16_1',
            'cho16_2',
            'cho16_3',
            'cho16_4',
            'sr_ser17',
            'cho17_1',
            'cho17_2',
            'cho17_3',
            'cho17_4',
            'sr_ser18',
            'cho18_1',
            'cho18_2',
            'cho18_3',
            'cho18_4',
            'sr_ser19',
            'cho19_1',
            'cho19_2',
            'cho19_3',
            'cho19_4',
            'sr_ser20',
            'cho20_1',
            'cho20_2',
            'cho20_3',
            'cho20_4',
            'sr_ser21',
            'cho21_1',
            'cho21_2',
            'cho21_3',
            'cho21_4',
            'sr_ser22',
            'gst_comm',
        ]
        widgets ={
            'mid':forms.HiddenInput(),
            'gstId':forms.HiddenInput(),
            'sr_ser1':forms.TextInput(attrs={'readonly': 'readonly','class': 'form-control','dir':'rtl'}),
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
