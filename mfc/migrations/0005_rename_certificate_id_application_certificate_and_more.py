# Generated by Django 4.0.4 on 2022-06-23 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0004_rename_user_id_application_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='certificate_id',
            new_name='certificate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='department_id',
            new_name='department',
        ),
    ]
