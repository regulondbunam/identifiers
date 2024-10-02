import mongoengine

from identifiers_api.shared import constants
from identifiers_api.services.identifiers import create_id
from identifiers_api.services.identifiers import get_identifiers
from identifiers_api.services.identifiers import update_id
from identifiers_api.services import regulondbmultigenomic
from identifiers_api.services import regulondbht
from identifiers_api.services import regulondbdatamarts


def connect(uri, database="regulondbidentifiers"):
    mongoengine.connect(database, alias='id_api', host=uri)


def disconnect():
    mongoengine.disconnect(alias='id_api')
