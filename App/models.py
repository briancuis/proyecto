from django.db import models

class futbolista(models.Model):
    nombre = models.CharField(max_length=200)
    equipo = models.CharField(max_length=200)
    edad = models.IntegerField(null=0)



    def __str__(self):
        return f"{self.nombre},{self.equipo},{self.id}"