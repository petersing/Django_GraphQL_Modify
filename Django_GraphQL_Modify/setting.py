from django.conf import settings
import importlib

#### Error Message
MUTATION_ERRORS_FLAG = "graphene_mutation_has_errors"


#### Django Setting (Graphene Function)
schema_path = settings.GRAPHENE['SCHEMA'].split('.')
Schema_Variable_Name = schema_path.pop(-1)
Schema_Module = importlib.import_module('.'.join(schema_path))
schema = getattr(Schema_Module, Schema_Variable_Name)