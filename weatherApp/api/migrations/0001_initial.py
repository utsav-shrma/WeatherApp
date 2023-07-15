# Generated by Django 4.2.3 on 2023-07-14 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('detailType', models.CharField(choices=[('H', '1 One'), ('D', '48 Hour'), ('W', '7 Days')], default='H', max_length=1)),
                ('expTime', models.DateTimeField()),
            ],
        ),
    ]