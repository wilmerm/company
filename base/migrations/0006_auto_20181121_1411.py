# Generated by Django 2.1.3 on 2018-11-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20181121_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='url',
            field=models.URLField(blank=True, help_text='En caso de no especificar una View, se usa esta dirección si la especifica.', verbose_name='Url (opcional)'),
        ),
        migrations.AlterField(
            model_name='link',
            name='cssclass',
            field=models.CharField(blank=True, default='link', help_text='Nombre de la clase del stilo CSS que tendrá este enlace.', max_length=50, verbose_name='CSS class'),
        ),
        migrations.AlterField(
            model_name='link',
            name='group',
            field=models.CharField(choices=[('NAV', 'Barra de navegación'), ('CREDITS', 'Créditos')], help_text='Grupo de enlaces al cual pertenece.', max_length=50, verbose_name='Grupo'),
        ),
        migrations.AlterField(
            model_name='link',
            name='img',
            field=models.ImageField(blank=True, help_text='Icono (imagen) opcional, que tendrá este enlace.', upload_to='links/', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='link',
            name='viewname',
            field=models.CharField(blank=True, help_text='Nombre de la vista (View) a la cual apuntará la url.', max_length=20, verbose_name='View'),
        ),
    ]
