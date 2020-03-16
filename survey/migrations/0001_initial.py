# Generated by Django 3.0.4 on 2020-03-16 11:29

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
            name='GustSr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('gstname', models.CharField(blank=True, max_length=255, null=True, verbose_name='البريد الإلكتروني')),
            ],
        ),
        migrations.CreateModel(
            name='MainSr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(auto_now_add=True)),
                ('sr_org', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المنفذة للمسح الميداني')),
                ('sr_loc', models.CharField(blank=True, max_length=255, null=True, verbose_name='الجهة المنفذة للخدمة')),
                ('sr_ser', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('sr_order', models.PositiveSmallIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='ترتيب السؤال')),
                ('sr_status', models.BooleanField(blank=True, choices=[(True, 'نعم'), (False, 'لا')], default=True, help_text='يظهز السؤال في الإستبيان', null=True, verbose_name='الحالة')),
                ('cho_1', models.BooleanField(default=False, verbose_name='مرضي')),
                ('cho_2', models.BooleanField(default=False, verbose_name='مرضي نوعاً ما')),
                ('cho_3', models.BooleanField(default=False, verbose_name='غير مرضي')),
                ('cho_4', models.BooleanField(default=False, verbose_name='لا أعلم')),
                ('sr_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-sr_order',),
            },
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
    ]
