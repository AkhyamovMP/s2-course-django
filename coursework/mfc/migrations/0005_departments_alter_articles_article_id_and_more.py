# Generated by Django 4.0.4 on 2022-05-31 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0004_alter_users_passport_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('departpment_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='department_id')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('address', models.CharField(max_length=150, verbose_name='address')),
            ],
        ),
        migrations.AlterField(
            model_name='articles',
            name='article_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='article_id'),
        ),
        migrations.AlterField(
            model_name='certificates',
            name='certificate_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='certificate_id'),
        ),
        migrations.AlterField(
            model_name='passports',
            name='passport_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='passport_id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='passport_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mfc.passports', unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(blank=True, max_length=30, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='user_id'),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(blank=True, max_length=30, verbose_name='username'),
        ),
    ]