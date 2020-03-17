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
    sr_status = models.BooleanField(
        choices=TRUE_FALSE_CHOICES, default=True, help_text="يظهز السؤال في الإستبيان", verbose_name="الحالة", null=True, blank=True)
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
    sr_ser1 = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho1_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho1_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho1_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho1_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)

    sr_ser2 = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho2_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho2_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho2_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho2_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)

    sr_ser3 = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho3_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho3_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho3_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho3_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)

    sr_ser4 = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho4_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho4_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho4_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho4_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)

    sr_ser5 = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)
    cho5_1 = models.BooleanField(choices=TRUE_FALSE_CHOICES, help_text="مرضي", default=False)
    cho5_2 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="مرضي نوعاً ما", default=False)
    cho5_3 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="غير مرضي", default=False)
    cho5_4 = models.BooleanField(choices=TRUE_FALSE_CHOICES,help_text="لا أعلم", default=False)


    # class Meta:
    #     ordering = ('-sr_order',)

    def __str__(self):
        return self.id

    def clean(self):
        if self.sr_order < 1:
            raise ValidationError(
                ('Only numbers equal to 1 or greater are accepted.'))




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