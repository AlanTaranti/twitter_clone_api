# Generated by Django 2.1 on 2018-08-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TwitterClone", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="perfil",
            name="segue",
            field=models.ManyToManyField(
                null=True, related_name="seguido", to="TwitterClone.Perfil"
            ),
        ),
    ]
