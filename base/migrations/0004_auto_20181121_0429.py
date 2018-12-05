# Generated by Django 2.1.3 on 2018-11-21 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20181121_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='img',
            field=models.ImageField(blank=True, upload_to='links/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='link',
            name='group',
            field=models.CharField(choices=[('NAV', 'Barra de navegación'), ('CREDITS', 'Créditos')], max_length=50, verbose_name='Grupo'),
        ),
    ]
