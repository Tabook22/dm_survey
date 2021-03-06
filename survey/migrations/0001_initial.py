# Generated by Django 3.0.4 on 2020-03-21 08:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('sr_org', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المنفذة للمسح الميداني')),
                ('sr_loc', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المنفذة للخدمة')),
                ('sr_desc', models.TextField(blank=True, null=True, verbose_name='شرح مختصر عن الإستبيان')),
                ('sr_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='مزود الخدمة')),
                ('pro_desc', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.MainSr')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ser_title', models.CharField(blank=True, max_length=300, null=True, verbose_name='عنوان الخدمة')),
                ('ser_desc', models.TextField(blank=True, null=True, verbose_name='ملاحظات')),
                ('spid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.ServiceProvider')),
            ],
        ),
        migrations.CreateModel(
            name='MainSr2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_order', models.PositiveSmallIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='ترتيب السؤال')),
                ('sr_status', models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], default=True, help_text='يظهز السؤال في الإستبيان', null=True, verbose_name='الحالة')),
                ('sr_ser1', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho1_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho1_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho1_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho1_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser2', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho2_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho2_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho2_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho2_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser3', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho3_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho3_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho3_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho3_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser4', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho4_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho4_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho4_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho4_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser5', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho5_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho5_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho5_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho5_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser6', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho6_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho6_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho6_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho6_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser7', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho7_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho7_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho7_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho7_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser8', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho8_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho8_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho8_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho8_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser9', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho9_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho9_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho9_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho9_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser10', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho10_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho10_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho10_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho10_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser11', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho11_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho11_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho11_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho11_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser12', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho12_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho12_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho12_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho12_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser13', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho13_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho13_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho13_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho13_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser14', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho14_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho14_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho14_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho14_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser15', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho15_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho15_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho15_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho15_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser16', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho16_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho16_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho16_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho16_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser17', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho17_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho17_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho17_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho17_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser18', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho18_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho18_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho18_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho18_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser19', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho19_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho19_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho19_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho19_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser20', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho20_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho20_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho20_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho20_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser21', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho21_1', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي')),
                ('cho21_2', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='مرضي نوعاً ما')),
                ('cho21_3', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='غير مرضي')),
                ('cho21_4', models.BooleanField(choices=[(True, 'نعم'), (False, 'لا')], default=False, help_text='لا أعلم')),
                ('sr_ser22', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('gst_comm', models.TextField(blank=True, null=True, verbose_name='المقترحات')),
                ('mid', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='survey.MainSr')),
            ],
            options={
                'ordering': ('-sr_order',),
            },
        ),
        migrations.CreateModel(
            name='Main_Sr_Qys',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cho_1', models.BooleanField(default=False, verbose_name='مرضي')),
                ('cho_2', models.BooleanField(default=False, verbose_name='مرضي نوعاً ما')),
                ('cho_3', models.BooleanField(default=False, verbose_name='غير مرضي')),
                ('cho_4', models.BooleanField(default=False, verbose_name='لا أعلم')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.MainSr')),
            ],
        ),
        migrations.CreateModel(
            name='Main_Sr_Comm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_sgg', models.TextField(blank=True, null=True, verbose_name='ما هي مقترحاتك لتطوير خدمات البلدية التي تقدمها للمواطنيين')),
                ('mid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='survey.MainSr')),
            ],
        ),
        migrations.CreateModel(
            name='GustSr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('gstId', models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم المشارك')),
                ('gs_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='الاسم')),
                ('gst_age', models.CharField(blank=True, max_length=255, null=True, verbose_name='العمر')),
                ('gst_area', models.CharField(blank=True, max_length=255, null=True, verbose_name='المنطقة')),
                ('gst_deu', models.CharField(blank=True, max_length=255, null=True, verbose_name='المستوى التعليمي')),
                ('gst_mobile', models.CharField(blank=True, max_length=255, null=True, verbose_name='الهاتف/النقال')),
                ('gst_email', models.CharField(blank=True, max_length=255, null=True, verbose_name='البريد الإلكتروني')),
                ('mid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='survey.MainSr')),
            ],
        ),
    ]
