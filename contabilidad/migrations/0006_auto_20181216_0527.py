# Generated by Django 2.1.3 on 2018-12-16 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0005_auto_20181215_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='cliente',
            field=models.ForeignKey(blank=True, default=None, help_text='Cliente del préstamo.', null=True, on_delete=django.db.models.deletion.PROTECT, to='clientes.Cliente', verbose_name='Cliente'),
        ),
    ]
