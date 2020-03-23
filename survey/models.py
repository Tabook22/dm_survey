from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
# Create your models here.


class MainSr(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'نعم'),
        (False, 'لا')
    )
    # models.ForeignKey(settings.AUTH_USER_MODEL)
    sr_emp = models.ForeignKey(User, on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now_add=True)
    sr_org = models.CharField(
        verbose_name="الجهة المنفذة للمسح الميداني", max_length=255, null=True, blank=True)
    sr_loc = models.CharField(
        verbose_name="الجهة المنفذة للخدمة", max_length=255, null=True, blank=True)
    sr_desc=models.TextField(verbose_name="شرح مختصر عن الإستبيان", null=True, blank=True)
    sr_status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=True, help_text="يظهز السؤال في الإستبيان", verbose_name="الحالة", null=True, blank=True)
    
    def __str__(self):
        return self.sr_org



class MainSr2(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'نعم'),
        (False, 'لا')
    )
    # models.ForeignKey(settings.AUTH_USER_MODEL)
    gstId=models.CharField(verbose_name="رقم المشارك", max_length=255, null=True, blank=True)
    mid = models.ForeignKey(MainSr, on_delete=models.CASCADE, default='')
    sr_order = models.PositiveSmallIntegerField(verbose_name="ترتيب السؤال", default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=True)
    sr_status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=True, help_text="يظهز السؤال في الإستبيان", verbose_name="الحالة", null=True, blank=True)
    sr_ser1 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True )
    cho1_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser2 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho2_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser3 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho3_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser4 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho4_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser5 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho5_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser6 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho6_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser7 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho7_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser8 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho8_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser9 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho9_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser10 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho10_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser11 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho11_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser12 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho12_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser13 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho13_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser14 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho14_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser15 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho15_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser16 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho16_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser17 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho17_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser18 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho18_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser19 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho19_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser20= models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho20_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser21= models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho21_1 = models.CharField(max_length=5,default=False, null=True, blank=True)
    sr_ser22=models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    gst_comm=models.TextField(verbose_name="المقترحات", null=True, blank=True)
    
    class Meta:
        ordering = ('-sr_order',)

    def __str__(self):
        return self.id

    # def clean(self):
    #     if self.sr_order < 1:
    #         raise ValidationError(
    #             ('Only numbers equal to 1 or greater are accepted.'))




class Main_Sr_Qys(models.Model):
    mid = models.ForeignKey(MainSr, on_delete=models.CASCADE)
    cho_1 = models.BooleanField("مرضي", default=False)
    cho_2 = models.BooleanField("مرضي نوعاً ما", default=False)
    cho_3 = models.BooleanField("غير مرضي", default=False)
    cho_4 = models.BooleanField("لا أعلم", default=False)


class GustSr(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    mid = models.ForeignKey(MainSr, on_delete=models.CASCADE, default=1)
    gstId=models.CharField(verbose_name="رقم المشارك", max_length=255, null=True, blank=True)
    gs_name = models.CharField(verbose_name="الاسم", max_length=255, null=True, blank=True)
    gst_age = models.CharField(verbose_name="العمر", max_length=255, null=True, blank=True)
    gst_area = models.CharField(verbose_name="المنطقة", max_length=255, null=True, blank=True)
    gst_deu = models.CharField(verbose_name="المستوى التعليمي", max_length=255, null=True, blank=True)
    gst_mobile = models.CharField(verbose_name="الهاتف/النقال", max_length=255, null=True, blank=True)
    gst_email = models.CharField(verbose_name="البريد الإلكتروني", max_length=255, null=True, blank=True)


class ServiceProvider(models.Model):
    mid = models.ForeignKey(MainSr, on_delete=models.CASCADE)
    pro_title=models.CharField(verbose_name="مزود الخدمة", max_length=255, null=True, blank=True)
    pro_desc=models.TextField("ملاحظات", null=True, blank=True)


class Service(models.Model):
    spid=models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    ser_title=models.CharField(verbose_name="عنوان الخدمة", max_length=300, null=True, blank=True)
    ser_desc=models.TextField("ملاحظات", null=True, blank=True)

class Main_Sr_Comm(models.Model):
    mid = models.ForeignKey(MainSr, on_delete=models.CASCADE)
    sr_sgg = models.TextField(
        "ما هي مقترحاتك لتطوير خدمات البلدية التي تقدمها للمواطنيين", null=True, blank=True)

    # def __str__(self):
    #    return self.mid


# class PersonalInfo(models.Model):
    # job categrory 1- searching for job, 2-private job, 3-government job
    # gender=
    # age
    # homeloc where is he lives in salalah or tagq or murbat for example
    # education level