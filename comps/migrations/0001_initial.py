# Generated by Django 3.1 on 2020-08-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('size_range', models.TextField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('entries', models.DecimalField(decimal_places=0, max_digits=4)),
                ('image_url', models.URLField(max_length=1024)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('end_date', models.DateField()),
            ],
        ),
    ]
