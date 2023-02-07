from ninja import Router
from django.http import JsonResponse
from django.contrib.auth.models import User
pacientes_router = Router()

@pacientes_router.post('teste/')
def teste(request):
    User.objects.get(id=request.auth)
    return JsonResponse({'teste':2, 'user': request.auth})