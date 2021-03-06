# Generated by Django 2.1.3 on 2018-12-14 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0002_auto_20181211_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='carta_de_trabajo_file',
            field=models.FileField(blank=True, upload_to='prestamos/solicitud/%Y/%m/', verbose_name='Carta de trabajo'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='cedula_file',
            field=models.FileField(default=None, upload_to='prestamos/solicitud/%Y/%m/', verbose_name='Cédula'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre del conyugue'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_trabajo_direccion',
            field=models.CharField(blank=True, max_length=200, verbose_name='Dirección del trabajo dle conyugue'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_trabajo_ingresos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Sus ingresos mensuales dentro de la empresa.', max_digits=11, verbose_name='Ingresos mensuales del conyugue'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_trabajo_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Lugar de trabajo del conyugue'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_trabajo_posicion',
            field=models.CharField(blank=True, help_text='Puesto que ocupa el conyugue dentro de la empresa.', max_length=50, verbose_name='Puesto que ocupa'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='conyugue_trabajo_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono del trabajo del conyugue'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='direccion',
            field=models.CharField(default='', help_text='Dirección de su residencia o domicilio.', max_length=200, verbose_name='Dirección'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='estado_civil',
            field=models.CharField(choices=[('SOLTERO', 'Soltero'), ('CASADO', 'Casado'), ('UNION_LIBRE', 'Unión libre'), ('OTRO', 'Otro')], default='', max_length=10, verbose_name='Estado civil'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref1_celular',
            field=models.CharField(blank=True, max_length=20, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref1_direccion',
            field=models.CharField(blank=True, max_length=200, verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref1_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref1_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref2_celular',
            field=models.CharField(blank=True, max_length=20, verbose_name='Celular'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref2_direccion',
            field=models.CharField(blank=True, max_length=200, verbose_name='Dirección'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref2_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref2_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref3_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre de la empresa'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref3_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref4_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Nombre de la empresa'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='ref4_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_direccion',
            field=models.CharField(blank=True, max_length=200, verbose_name='Dirección del trabajo'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_ingresos',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Sus ingresos mensuales dentro de la empresa.', max_digits=11, verbose_name='Ingresos mensuales'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_inicio',
            field=models.DateField(blank=True, default=None, help_text='Fecha en que empezó a formar parte de la empresa como empleado.', verbose_name='Fecha en que ingresó'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_nombre',
            field=models.CharField(blank=True, max_length=50, verbose_name='Lugar de trabajo'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_posicion',
            field=models.CharField(blank=True, help_text='Puesto que ocupa dentro de la empresa.', max_length=50, verbose_name='Puesto que ocupa'),
        ),
        migrations.AddField(
            model_name='solicitud',
            name='trabajo_telefono',
            field=models.CharField(blank=True, max_length=20, verbose_name='Teléfono del trabajo'),
        ),
    ]
