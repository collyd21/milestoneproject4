# Generated by Django 3.1 on 2020-08-29 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comp',
            options={'ordering': ['-end_date']},
        ),
    ]