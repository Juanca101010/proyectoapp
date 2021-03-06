# Generated by Django 4.0.4 on 2022-04-15 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_decano'),
    ]

    operations = [
        migrations.CreateModel(
            name='voto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fechaHora', models.DateTimeField()),
                ('idCandidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.candidato')),
                ('idVotante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.estudiante')),
            ],
        ),
    ]
