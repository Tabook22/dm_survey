from django.urls import path
from .views import add_survey

urlpatterns = [
    path('add_survey/', add_survey, name=('add_survey')),
]
