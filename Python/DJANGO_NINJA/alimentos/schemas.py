from typing import List, Dict
from ninja import Schema, ModelSchema
from .models import Alimento as ModelAlimento


# --> schemas
class Alimento(ModelSchema):
    # titulo: str
    # quantidade: int
    # # variedades: list[str]
    novo_campo : List[int] = []
    class Config:
        model = ModelAlimento
        model_fields = "__all__"