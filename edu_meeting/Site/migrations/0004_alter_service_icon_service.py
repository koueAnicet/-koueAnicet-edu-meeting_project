# Generated by Django 4.0.6 on 2022-07-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0003_alter_aboutuniversity_number_static'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon_service',
            field=models.ImageField(upload_to='service_site'),
        ),
    ]
