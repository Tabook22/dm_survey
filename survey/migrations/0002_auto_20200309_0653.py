# Generated by Django 3.0.4 on 2020-03-09 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainsr',
            options={'ordering': ('-sr_order',)},
        ),
    ]