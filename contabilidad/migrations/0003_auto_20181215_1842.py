# Generated by Django 2.1.3 on 2018-12-15 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0002_auto_20181214_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='cliente',
            field=models.ForeignKey(help_text='Cliente del préstamo.', on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente', verbose_name='Cliente'),
        ),
    ]