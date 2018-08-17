# Generated by Django 2.1 on 2018-08-17 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TwitterClone', '0007_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to=settings.AUTH_USER_MODEL),
        ),
    ]
