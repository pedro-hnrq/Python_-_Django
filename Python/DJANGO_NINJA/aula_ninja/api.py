from ninja import NinjaAPI
from alimentos.api import alimentos_router
from pacientes.api import pacientes_router

api = NinjaAPI()

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)