# Generated by Django 4.0.1 on 2022-05-29 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_centralizedadminview_store_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='centralizedadminview',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
