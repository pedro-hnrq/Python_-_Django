from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pessoa, Historico

@receiver(post_save, sender=Pessoa)
def envia_sinal(sender, instance, created, **kwargs):
    x = Historico ( nome=instance.nome,
                    email=instance.email,
                    telefone=instance.telefone,
                    pessoa=instance)
    x.save()
    print('Histório cadastrado')
    if created:
        print('Fui criada')
    else:
        print('Fui alterada')
    print(f'{instance.nome} | {instance.email} | {instance.telefone}')

# post_save.connect(envia_sinal, sender=Pessoa)