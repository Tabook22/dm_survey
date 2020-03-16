from django import forms
from django.urls import reverse
from .models import MainSr, Main_Sr_Comm, ServiceProvider, Service, Main_Sr_Qys
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
            'sr_ser',
            'cho_1',
            'cho_2',
            'cho_3',
            'cho_4',
        ]


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
