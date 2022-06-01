# Generated by Django 3.2.6 on 2022-03-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_tokencreation'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpdReceptionView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('patient_id', models.CharField(max_length=100)),
                ('patient_name', models.CharField(max_length=100)),
                ('token_no', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
    ]