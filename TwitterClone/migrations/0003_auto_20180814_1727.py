# Generated by Django 2.1 on 2018-08-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TwitterClone", "0002_auto_20180813_0231"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="segue",
            field=models.ManyToManyField(null=True, to="TwitterClone.Perfil"),
        ),
    ]
