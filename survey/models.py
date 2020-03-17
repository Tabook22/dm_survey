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
    gstId=models.CharField(
        verbose_name="رقم المشارك", max_length=255, null=True, blank=True)
    dt = models.DateTimeField(auto_now_add=True)
    sr_org = models.CharField(
        verbose_name="الجهة المنفذة للمسح الميداني", max_length=255, null=True, blank=True)
    sr_loc = models.CharField(
        verbose_name="الجهة المنفذة للخدمة", max_length=255, null=True, blank=True)
    sr_ser = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    sr_order = models.PositiveSmallIntegerField(
        verbose_name="ترتيب السؤال", default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=True)
    sr_status = models.BooleanField(choices=TRUE_FALSE_CHOICES, default=True, help_text="يظهز السؤال في الإستبيان", verbose_name="الحالة", null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)

    class Meta:
        ordering = ('-sr_order',)

    def __str__(self):
        return self.sr_ser

    def clean(self):
        if self.sr_order < 1:
            raise ValidationError(
                ('Only numbers equal to 1 or greater are accepted.'))



class MainSr2(models.Model):
    TRUE_FALSE_CHOICES = (
        (True, 'نعم'),
        (False, 'لا')
    )
    # models.ForeignKey(settings.AUTH_USER_MODEL)
    sr_ser1 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True )
    cho1_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho1_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho1_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho1_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser2 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho2_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho2_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho2_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho2_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser3 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho3_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho3_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho3_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho3_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser4 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho4_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho4_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho4_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho4_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser5 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho5_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho5_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho5_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho5_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser6 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho6_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho6_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho6_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho6_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser7 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho7_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho7_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho7_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho7_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser8 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho8_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho8_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho8_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho8_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser9 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho9_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho9_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho9_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho9_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser10 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho10_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho10_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho10_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho10_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser11 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho11_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho11_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho11_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho11_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser12 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho12_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho12_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho12_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho12_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser13 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho13_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho13_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho13_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho13_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser14 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho14_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho14_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho14_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho14_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser15 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho15_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho15_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho15_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho15_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser16 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho16_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho16_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho16_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho16_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser17 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho17_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho17_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho17_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho17_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser18 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho18_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho18_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho18_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho18_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser19 = models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho19_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho19_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho19_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho19_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser20=models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho20_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho20_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho20_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho20_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser21=models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    cho21_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho21_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho21_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho21_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)
    sr_ser22=models.CharField(verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    gst_comm=models.TextField(verbose_name="المقترحات", null=True, blank=True)
    
    
    # class Meta:
    #     ordering = ('-sr_order',)

    # def __str__(self):
    #     return self.id

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
    gstname = models.CharField(verbose_name="الاسم", max_length=255, null=True, blank=True)
    gstname = models.CharField(verbose_name="العمر", max_length=255, null=True, blank=True)
    gstname = models.CharField(verbose_name="المنطقة", max_length=255, null=True, blank=True)
    gstname = models.CharField(verbose_name="المستوى التعليمي", max_length=255, null=True, blank=True)
    gstname = models.CharField(verbose_name="الهاتف/النقال", max_length=255, null=True, blank=True)
    gstname = models.CharField(verbose_name="البريد الإلكتروني", max_length=255, null=True, blank=True)


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