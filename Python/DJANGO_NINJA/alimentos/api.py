from ninja import Router
# from django.http import JsonResponse
from .schemas import Alimento
from .models import Alimento as ModelAlimento
from django.shortcuts import get_list_or_404

alimentos_router = Router()

# alimentos = [
#     {'Nome': 'Banana', 'Quandade': 5, 'id':1},
#     {'Nome': 'Carne', 'Quandade': 15, 'id':2},
#     {'Nome': 'Maca', 'Quandade': 8, 'id':3},
# ]

# @alimentos_router.get('/{int:alimento_id}/', response=List[Dict])
# def get_alimento(request, alimento_id: int) -> List[Dict]:
#     alimento = list(filter(lambda x : x['id'] == alimento_id, alimentos))
#     return alimento

# @alimentos_router.get('/{int:alimento_id}/')
# def get_alimento(request, alimento_id: int, preco_min: int =  10):
#     return {'alimento_id': alimento_id, 'preco_min': preco_min}



# @alimentos_router.get('/{alimento_id}', response=Alimento)
# def get_alimento(request, alimento_id: int) -> Alimento:
#     # print(alimento.titulo)
#     # print(alimento.quantidade)
#     # return {'variedade': alimento.variedades, 'alimento': alimento.titulo, 'QTA': alimento.quantidade}
#     # alimento = get_list_or_404(ModelAlimento, id=alimento_id)
#     alimento = ModelAlimento.objects.get(id=alimento_id)
#     print(alimento)
#     return alimento

@alimentos_router.post('/')
def get_alimento(request, alimento: Alimento):
    
    print(alimento.quantidade   )
    return alimento