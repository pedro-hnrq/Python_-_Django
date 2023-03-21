from ninja import NinjaAPI
from alimentos.api import alimentos_router
from pacientes.api import pacientes_router
from ninja.parser import Parser
import yaml
from django.http import HttpRequest
from ninja.security import HttpBearer, HttpBasicAuth
from django.contrib import auth
# class YamlParser(Parser):
#     def parse_body(self, request: HttpRequest):
#         return yaml.safe_load(request.body)

# api = NinjaAPI(parser=YamlParser())
class BasicAuth(HttpBasicAuth):
    def authenticate(self, request, username, password):
       user = auth.authenticate(username=username, password=password)

       if user: 
           return user.id

api = NinjaAPI(auth=BasicAuth())

api.add_router('/alimentos', alimentos_router)
api.add_router('/pacientes', pacientes_router)