# Generated by Django 2.1.3 on 2018-12-15 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0004_auto_20181215_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='user',
            field=models.ForeignKey(blank=True, default=None, editable=False, help_text='Usuario que registró la solicitud (opcional)', on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
    ]