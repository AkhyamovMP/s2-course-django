# Generated by Django 4.0.4 on 2022-06-20 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mfc', '0010_certificates_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificates',
            name='type',
            field=models.CharField(choices=[('CR', 'Справка'), ('EX', 'Выписка')], default='CR', max_length=2),
        ),
        migrations.CreateModel(
            name='application',
            fields=[
                ('application_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='aoolication_id')),
                ('application_date', models.DateField(verbose_name='application_date')),
                ('certificate_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mfc.certificates')),
                ('department_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mfc.departments')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mfc.users')),
            ],
        ),
    ]
