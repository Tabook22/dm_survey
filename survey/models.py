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
    sr_ser = models.CharField(
        verbose_name="نوع الخدمة المقدمة", max_length=255, null=True, blank=True)
    sr_order = models.PositiveSmallIntegerField(
        verbose_name="ترتيب السؤال", default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=True)
    sr_status = models.BooleanField(
        choices=TRUE_FALSE_CHOICES, default=True, help_text="يظهز السؤال في الإستبيان", verbose_name="الحالة", null=True, blank=True)
    # verbose_name="الحالة", null=True, blank=True)

    class Meta:
        ordering = ('-sr_order',)

    def __str__(self):
        return self.sr_ser

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
