# Generated by Django 4.2.3 on 2023-07-14 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_weatherdata_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='detailType',
        ),
    ]
