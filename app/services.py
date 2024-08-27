import random
from app.database.requests import *


lang = {'russian' : 'Русский',
        'english' : 'Английский',
        'korean' : 'Корейский'}

async def get_translations(orig, transl):
    orig_value, transl_value = await get_orig_transl(orig, transl)
    translation = await get_random_values(transl)

    translation.append(transl_value)

    random.shuffle(translation)

    return orig_value, transl_value, translation
