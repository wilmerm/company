# Generated by Django 2.1.3 on 2018-12-16 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0006_auto_20181216_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='tags',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='user',
            field=models.ForeignKey(default=None, help_text='Usuario que creó esto.', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]