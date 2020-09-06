# Generated by Django 3.1 on 2020-09-05 13:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comps', '0002_auto_20200829_1219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comp',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='comp',
            name='end_date',
        ),
        migrations.AddField(
            model_name='comp',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]