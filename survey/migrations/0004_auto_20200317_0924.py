# Generated by Django 3.0.4 on 2020-03-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_mainsr_gstid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainsr',
            name='gstId',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='رقم المشارك'),
        ),
    ]
