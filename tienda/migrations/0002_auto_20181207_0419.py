# Generated by Django 2.1.3 on 2018-12-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_height',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='img_width',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
