from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('index/', index, name="index"),
    path('survey/', include('survey.urls')),
    path('sr_user/', include('sr_user.urls'))
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

