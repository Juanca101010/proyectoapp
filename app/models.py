from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=True)

    class Meta:
        app_label = 'app'




class Facultad(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)

class EstadoVotacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)
    codigo = models.CharField(max_length=45, null=True)

class TipoVotacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)
    codigo = models.CharField(max_length=45, null=True)


class Estudiante(models.Model):
    id = models.IntegerField(primary_key=True)
    idFacultad = models.ForeignKey(
      Facultad, 
      on_delete=models.PROTECT
    )

    semestreActual = models.IntegerField(null=True)


class votacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=45, null=True)

    idTipo = models.ForeignKey(
      TipoVotacion, 
      on_delete=models.PROTECT
    )

    idEstado = models.ForeignKey(
      EstadoVotacion, 
      on_delete=models.PROTECT
    )

    idFacultad = models.ForeignKey(
      Facultad, 
      on_delete=models.PROTECT
    )

class Candidato(models.Model):
    id = models.IntegerField(primary_key=True)
    idEstudiante = models.ForeignKey(
      Estudiante, 
      on_delete=models.PROTECT,
      null=True
    )

    idVotacion = models.ForeignKey(
      votacion, 
      on_delete=models.PROTECT,
      null=True
    )
    semestre = models.IntegerField()
    propuesta = models.CharField(max_length=45, null=False)


class Decano(models.Model):
    id = models.IntegerField(primary_key=True)
    idFacultad = models.ForeignKey(
      Facultad, 
      on_delete=models.PROTECT,
      null=True
    )

class User(models.Model):
    first_name = models.CharField(max_length=45, null=False)
    last_name = models.CharField(max_length=45, null=False)
    email = models.CharField(max_length=45, null=False)
    password = models.CharField(max_length=45, null=False)
    is_superuser = models.BooleanField(null=True)
    # id = models.ForeignKey(
    #   Estudiante,
    #   on_delete=models.PROTECT,
    #   primary_key=True
    # )


class voto(models.Model):
    id = models.IntegerField(primary_key=True)
    idVotante = models.ForeignKey(
      Estudiante, 
      on_delete=models.PROTECT
    )

    idCandidato = models.ForeignKey(
      Candidato, 
      on_delete=models.PROTECT
    )

    fechaHora = models.DateTimeField(auto_now=False,auto_now_add=False)
