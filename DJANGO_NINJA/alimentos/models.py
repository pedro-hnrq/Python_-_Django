from django.db import models

# Create your models here.
class Alimento(models.Model):
    titulo = models.CharField(max_length=10)
    quantidade = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo
    