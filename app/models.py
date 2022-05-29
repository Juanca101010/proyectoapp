from django.db import models
from django.contrib.auth.models import User

class Facultad(models.Model):
    nombre= models.CharField(max_length=45, null=False)

    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'

# tiene uno a uno con User
# preguntar lo del null u primary key
#en la tabla decano no deberia existir un id user???

class Decano (models.Model):
    facultad= models.ForeignKey(
        Facultad,
        related_name='decanos',
        null=False,
        on_delete=models.PROTECT
    )
    user = models.OneToOneField(
        User,
        related_name='decano',
        null=True,
        primary_key=False,
        on_delete=models.PROTECT
    )

    def _str_(self):
        return "%s" % (self.facultad)

    class Meta:
        app_label= 'app'

class Estudiante (models.Model):
    semestreActual= models.IntegerField(null=False)
    documento=models.IntegerField(null=False)

    facultad= models.ForeignKey(
        Facultad,
        related_name='estudiantes',
        null=False,
        on_delete=models.PROTECT
    )
    user = models.OneToOneField(
        User,
        related_name='estudiante',
        null=True,
        primary_key=False,
        on_delete=models.PROTECT
    )
    

    def _str_(self):
        return "%s %s" % (self.user, self.facultad)

    class Meta:
        app_label= 'app'

# postulacion, Votacion, cerrada
class EstadoVotacion (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    codigo= models.CharField(max_length=45, null=False)

    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'

# semestre, facultad
class TipoVotacion (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    codigo= models.CharField(max_length=45, null=False)

    def _str_(self):
        return "%s" % (self.nombre)

    class Meta:
        app_label= 'app'

class Votacion (models.Model):
    nombre= models.CharField(max_length=45, null=False)
    tipo= models.ForeignKey(
        TipoVotacion,
        related_name='tipos_votaciones',
        on_delete=models.PROTECT
    )
    estado= models.ForeignKey(EstadoVotacion,
        related_name='estado_votaciones',
        on_delete=models.PROTECT
    )
    facultad= models.ForeignKey(Facultad,
        related_name='facultad_votaciones',
        null=False,
        on_delete=models.PROTECT
    )

    fechaInicio=models.DateField(auto_now=False, auto_now_add=False, null=True)
    fechaFinal=models.DateField(auto_now=False, auto_now_add=False,null=True)

    def _str_(self):
        return self.nombre

    class Meta:
        app_label= 'app'

class Candidato (models.Model):
    estudiante=models.ForeignKey(
        Estudiante,
        related_name='estudiante_candidatos',
        null=True,
        on_delete=models.PROTECT
    )
    Votacion=models.ForeignKey(
        Votacion,
        related_name='votacion_candidatos',
        null=True,
        on_delete=models.PROTECT
    )
    semestre= models.IntegerField(null=True)
    propuesta=models.CharField(max_length=45, null=True)
    cantidadVotos=models.IntegerField(
        null=False,
    )

    def _str_(self):
        return self.estudiante

    class Meta:
        app_label= 'app'

class Voto (models.Model):
    votante=models.ForeignKey(
        Estudiante,
        related_name='votantes',
        null=False,
        on_delete=models.PROTECT
    )
    candidato=models.ForeignKey(
        Candidato,
        related_name='candidatos',
        null=False,
        on_delete=models.PROTECT
    )
    votacion=models.ForeignKey(
        Votacion,
        related_name='votacion',
        null=False,
        on_delete=models.PROTECT
    )
    FechaHora=models.DateTimeField(null=True)

    def _str_(self):
        return self.candidato

    class Meta:
        app_label= 'app'