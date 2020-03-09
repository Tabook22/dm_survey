# Generated by Django 3.0.4 on 2020-03-09 06:41

from django.conf import settings
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
                ('sr_ser', models.CharField(blank=True, max_length=255, null=True, verbose_name='نوع الخدمة المقدمة')),
                ('cho_1', models.BooleanField(default=False, verbose_name='مرضي')),
                ('cho_2', models.BooleanField(default=False, verbose_name='مرضي نوعاً ما')),
                ('cho_3', models.BooleanField(default=False, verbose_name='غير مرضي')),
                ('cho_4', models.BooleanField(default=False, verbose_name='لا أعلم')),
                ('sr_order', models.IntegerField(blank=True, null=True, verbose_name='ترتيب السؤال')),
                ('sr_status', models.BooleanField(blank=True, null=True, verbose_name='الحالة')),
                ('sr_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('sr_order',),
            },
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
