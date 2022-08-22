from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    cep = models.CharField(max_length=8, blank=True)
    rua = models.CharField(max_length=100, blank=True)
    numero = models.IntegerField(blank=True, null=True)





# from django.db.models.fields import CharField
# from django.contrib.auth.models import User

# class EnderecoUsuario(models.Model):
#     rua = CharField(max_length=100, blank=True, null=True)
#     numero = CharField(max_length=100, blank=True, null=True)
#     cep = CharField(max_length=8)
#     usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)

#     def __str__(self) -> str:
        # return self.usuario.username