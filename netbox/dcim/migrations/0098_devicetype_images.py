# Generated by Django 2.2.9 on 2020-02-20 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0097_interfacetemplate_type_other'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicetype',
            name='front_image',
            field=models.ImageField(blank=True, upload_to='devicetype-images'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='rear_image',
            field=models.ImageField(blank=True, upload_to='devicetype-images'),
        ),
    ]
