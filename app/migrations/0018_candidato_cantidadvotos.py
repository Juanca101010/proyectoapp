# Generated by Django 4.0.4 on 2022-05-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_decano_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='cantidadVotos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
