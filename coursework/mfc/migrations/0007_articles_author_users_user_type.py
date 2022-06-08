# Generated by Django 4.0.4 on 2022-06-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0006_remove_departments_address_departments_building_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.CharField(default=1, max_length=128, verbose_name='author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='user_type',
            field=models.IntegerField(default=0, verbose_name='user_type'),
        ),
    ]
