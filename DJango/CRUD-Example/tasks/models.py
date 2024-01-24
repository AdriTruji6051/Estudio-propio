from django.db import models

# Create your models here.

class Tasks(models.Model):
    tittle = models.CharField(max_length = 200) #Creando un campo de tipo string, equivalente en SQL
    description = models.TextField(blank = True) #Con blank = True definimos que nuestra variable pueda estar vacia :)
    done = models.BooleanField(default = False) #Con default definimos el valor que tendra cualquier regustro de manera por defecto al crearlo
    
    def __str__(self):
        return self.tittle