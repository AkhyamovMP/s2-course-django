# Generated by Django 4.0.4 on 2022-06-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='application_date'),
        ),
    ]
