# Generated by Django 4.0.4 on 2022-05-28 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_candidato_cantidadvotos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votacion',
            name='tipo',
            field=models.IntegerField(),
        ),
    ]
