# Generated by Django 2.1.3 on 2018-12-09 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_visitas'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(default='', help_text='Descripción de la búsqueda', verbose_name='Descripción'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(help_text='Se acepta código HTML', verbose_name='Contenido'),
        ),
    ]
