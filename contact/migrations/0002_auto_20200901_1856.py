# Generated by Django 3.1 on 2020-09-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]