# Generated by Django 4.0.1 on 2022-05-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_remove_advice_visit_id_remove_allergy_visit_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centralizedadminview',
            name='date',
        ),
        migrations.AddField(
            model_name='centralizedadminview',
            name='store_image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]