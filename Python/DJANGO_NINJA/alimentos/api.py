from ninja import Router
from django.http import JsonResponse
# from typing import List, Dict

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

@alimentos_router.get('/{int:alimento_id}/')
def get_alimento(request, alimento_id: int, preco_min: int =  10):
    return {'alimento_id': alimento_id, 'preco_min': preco_min}