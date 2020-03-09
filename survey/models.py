from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MainSr(models.Model):
    sr_emp = models.ForeignKey(User, on_delete=models.CASCADE) # models.ForeignKey(settings.AUTH_USER_MODEL)
    dt=models.DateTimeField(auto_now_add=True)
    sr_org=models.CharField(verbose_name="الجهة المنفذة للمسح الميداني", max_length=255, null=True, blank=True)
    sr_loc=models.CharField(verbose_name="الجهة المنفذة للخدمة", max_length=255,null=True, blank=True)
    sr_ser =models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho_1=models.BooleanField("مرضي", default=False)
    cho_2=models.BooleanField("مرضي نوعاً ما", default=False)
    cho_3=models.BooleanField("غير مرضي", default=False)
    cho_4=models.BooleanField("لا أعلم", default=False)
    sr_order=models.IntegerField(verbose_name="ترتيب السؤال",null=True,blank=True)
    sr_status=models.BooleanField(verbose_name="الحالة",null=True, blank=True)
    
    class Meta:
        ordering=('-sr_order',)
    
    def __str__(self):
        return self.sr_ser

class Main_Sr_Comm(models.Model):
    mid=models.ForeignKey(MainSr, on_delete=models.CASCADE)
    sr_sgg=models.TextField("ما هي مقترحاتك لتطوير خدمات البلدية التي تقدمها للمواطنيين", null=True, blank=True)

    # def __str__(self):
    #    return self.mid