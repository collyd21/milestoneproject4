# Generated by Django 3.1 on 2020-09-04 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
