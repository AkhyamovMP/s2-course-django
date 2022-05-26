# Generated by Django 4.0.4 on 2022-05-24 15:53

from django.db import migrations, models
import django.db.models.deletion
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0002_articles_users_passport_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='passport_id',
            field=models.ForeignKey(null=sqlalchemy.sql.expression.true, on_delete=django.db.models.deletion.CASCADE, to='mfc.passports', unique=sqlalchemy.sql.expression.true),
        ),
    ]