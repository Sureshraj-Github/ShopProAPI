# Generated by Django 3.2.6 on 2022-04-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_ipdadmission_ipdpatientenquiry_ipdpatientsearch_ipdregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdadmission',
            name='primary_doc',
            field=models.CharField(max_length=100),
        ),
    ]
