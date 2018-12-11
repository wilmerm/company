# Generated by Django 2.1.3 on 2018-12-11 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.TextField(help_text='Se acepta código HTML', verbose_name='Contenido')),
                ('description', models.TextField(blank=True, help_text='Descripción de la búsqueda', verbose_name='Descripción')),
                ('tags', models.CharField(blank=True, max_length=100, verbose_name='Etiquetas')),
                ('img', models.ImageField(blank=True, help_text='Imagen que se mostrará junto al título de la publicación', upload_to='blog/post/%Y/%m/', verbose_name='Imagen')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('visitas', models.IntegerField(default=0, editable=False, help_text='Cantidad de visitas a esta entrada', verbose_name='Visitas')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
            },
        ),
    ]
