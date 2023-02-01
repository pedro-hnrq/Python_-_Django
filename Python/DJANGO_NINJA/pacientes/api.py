from ninja import Router
from django.http import JsonResponse

pacientes_router = Router()

@pacientes_router.get('teste2/')
def teste(request):
    return JsonResponse({'teste':2})