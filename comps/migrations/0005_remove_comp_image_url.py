# Generated by Django 3.1 on 2020-09-18 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0004_auto_20200905_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comp',
            name='image_url',
        ),
    ]
