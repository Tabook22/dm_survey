from django.urls import path
from .views import add_survey, survey_list
app_name = "survey"
urlpatterns = [
    path('add_survey/', add_survey, name=('add_survey')),
    path('survey_list/', survey_list, name=('survey_list'))
]
