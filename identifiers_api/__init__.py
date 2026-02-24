from urllib.parse import urlparse, urlunparse

import mongoengine

from identifiers_api.shared import constants
from identifiers_api.services.identifiers import create_id
from identifiers_api.services.identifiers import get_identifiers
from identifiers_api.services.identifiers import update_id
from identifiers_api.services import regulondbmultigenomic
from identifiers_api.services import regulondbht
from identifiers_api.services import regulondbdatamarts


def _strip_db_from_mongo_uri(uri: str) -> str:
    """
    If the MongoDB URI contains a database path (e.g. /mydb), remove it.
    Keeps query params intact.
    """
    parsed = urlparse(uri)

    # If path is "/some_db_name" (not empty and not just "/"), that's a DB name.
    if parsed.path and parsed.path != "/":
        parsed = parsed._replace(path="")

    return urlunparse(parsed)

def connect(uri, database="regulondbidentifiers"):
    clean_uri = _strip_db_from_mongo_uri(uri)
    mongoengine.connect(database, alias='id_api', host=clean_uri)


def disconnect():
    mongoengine.disconnect(alias='id_api')
