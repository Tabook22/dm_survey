from django.urls import path
from .views import add_survey, survey_list, gust_sr
app_name = "survey"
urlpatterns = [
    path('add_survey/', add_survey, name=('add_survey')),
    path('survey_list/', survey_list, name=('survey_list')),
    path('gust_sr/', gust_sr,name="gust_sr")
]
