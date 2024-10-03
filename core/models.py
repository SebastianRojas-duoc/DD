from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True)

	def __str__(self):
		return self.nombre


class Registronoti(models.Model):
	
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	titulo = models.CharField(max_length=1000)
	subtitulo = models.CharField(max_length=1000)
	reportero = models.CharField(max_length=1000)
	link = models.CharField(max_length=1000)
	fecha = models.CharField(max_length=10)
	imagen = models.ImageField(upload_to='Noticias/')
	descripcion = models.CharField(max_length=100000)

	def __str__(self):
		return f"{self.titulo} {self.subtitulo}"
	

class Comentario(models.Model):

	nombre = models.CharField(max_length=100)
	correo = models.CharField(max_length=100)
	mensajes = models.CharField(max_length=100000)

	def __str__(self):
		return f"{self.nombre}"
	
class PerfilUsuario(models.Model):
	
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    genero = models.CharField(max_length=1,choices=[('', 'Seleccione una opción'),('M','Masculino'),('F','Femenino'),('O','Otro')])
	
	
    def __str__(self):
        return self.user.username
	