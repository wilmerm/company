# Generated by Django 2.1.3 on 2018-12-14 23:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contabilidad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='user',
            field=models.ForeignKey(default=None, help_text='Usuario que creó esto.', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]