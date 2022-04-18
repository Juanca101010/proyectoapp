# Generated by Django 4.0.4 on 2022-04-18 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0012_alter_user_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='idEstudiante',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='idVotacion',
        ),
        migrations.RemoveField(
            model_name='decano',
            name='idFacultad',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='idFacultad',
        ),
        migrations.RemoveField(
            model_name='votacion',
            name='idEstado',
        ),
        migrations.RemoveField(
            model_name='votacion',
            name='idFacultad',
        ),
        migrations.RemoveField(
            model_name='votacion',
            name='idTipo',
        ),
        migrations.RemoveField(
            model_name='voto',
            name='fechaHora',
        ),
        migrations.RemoveField(
            model_name='voto',
            name='idCandidato',
        ),
        migrations.RemoveField(
            model_name='voto',
            name='idVotante',
        ),
        migrations.AddField(
            model_name='candidato',
            name='Votacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='votacion_candidatos', to='app.votacion'),
        ),
        migrations.AddField(
            model_name='candidato',
            name='estudiante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='estudiante_candidatos', to='app.estudiante'),
        ),
        migrations.AddField(
            model_name='decano',
            name='facultad',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='decanos', to='app.facultad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='decano',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='decano', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='documento',
            field=models.IntegerField(default=12345),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='facultad',
            field=models.ForeignKey(default=124, on_delete=django.db.models.deletion.PROTECT, related_name='estudiantes', to='app.facultad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='estudiante', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='votacion',
            name='estado',
            field=models.ForeignKey(default=1234, on_delete=django.db.models.deletion.PROTECT, related_name='estado_votaciones', to='app.estadovotacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votacion',
            name='facultad',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, related_name='facultad_votaciones', to='app.facultad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votacion',
            name='fechaFinal',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='votacion',
            name='fechaInicio',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='votacion',
            name='tipo',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.PROTECT, related_name='tipos_votaciones', to='app.tipovotacion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voto',
            name='FechaHora',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='voto',
            name='candidato',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.PROTECT, related_name='candidatos', to='app.candidato'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='voto',
            name='votante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='votantes', to='app.estudiante'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidato',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='propuesta',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='semestre',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='decano',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estadovotacion',
            name='codigo',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estadovotacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estadovotacion',
            name='nombre',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='semestreActual',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='facultad',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='facultad',
            name='nombre',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipovotacion',
            name='codigo',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tipovotacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tipovotacion',
            name='nombre',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='votacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='votacion',
            name='nombre',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
