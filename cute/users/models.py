from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name='username')
    email = models.CharField(max_length=60, verbose_name='email')
    password = models.CharField(max_length=20, verbose_name='password')
    
    ##def __str__(self):
       ## fila = 'titulo: '+ self.titulo+ ' - ' + 'descripcion: '+ self.descripcion
        ##return fila
