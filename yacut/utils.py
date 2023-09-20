from random import choice

from .models import URLMap

ARRAY = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def get_unique_short_id(count_char=6):
    short_url = []
    for _ in range(count_char):
        short_url.append(choice(ARRAY))
    short_url = ''.join(short_url)
    if URLMap.query.filter_by(short=short_url).first() is not None:
        get_unique_short_id()
    return short_url
