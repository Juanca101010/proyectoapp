# Generated by Django 4.0.4 on 2022-04-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoVotacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('codigo', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVotacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45, null=True)),
                ('codigo', models.CharField(max_length=45, null=True)),
            ],
        ),
    ]
