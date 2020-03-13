from django.urls import path 
from .views import login, logout, register
from django.contrib.auth import views as auth_views
app_name="sr_user"
urlpatterns = [
   path('login/', auth_views.LoginView.as_view(template_name='sr_user/login.html'), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name="logout"),
   path('register/', register, name="register")
]