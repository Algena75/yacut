import string
from random import choices

from .models import URLMap

ARRAY = string.ascii_letters + string.digits


def get_unique_short_id(count_char=6):
    short_url = ''.join(choices(ARRAY, k=count_char))
    if URLMap.query.filter_by(short=short_url).first() is not None:
        get_unique_short_id()
    return short_url
