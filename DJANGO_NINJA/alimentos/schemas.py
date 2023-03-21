from typing import List, Dict
from ninja import Schema, ModelSchema
from .models import Alimento as ModelAlimento


# --> schemas
class Alimento(ModelSchema):
    # titulo: str
    # quantidade: int
    # # variedades: list[str]
    novo_campo : List[int] = []
    class Config(Schema.Config):
        model = ModelAlimento
        # anystr_lower = True
        # anystr_strip_whitespace = True
        # allow_mutation = False
        model_fields = "__all__"