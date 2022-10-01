from django.apps import AppConfig
from django.conf import settings

import os

from loguru import logger
import pandas as pd
# import pickle as pkl
import dill


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    gbr_1_column_zero_celsius = 0
    with open(os.path.join(settings.MODELS_ROOT, 'ml1.pkl'), 'rb') as f:
        gbr_1_column_zero_celsius = dill.load(f)

    lr_2_column_twenty_five_celsius = 0
    with open(os.path.join(settings.MODELS_ROOT, 'ml2.pkl'), 'rb') as f:
        lr_2_column_twenty_five_celsius = dill.load(f)

    gbr_3_column_laxity = 0
    with open(os.path.join(settings.MODELS_ROOT, 'ml3.pkl'), 'rb') as f:
        gbr_3_column_laxity = dill.load(f)

    gbr_4_column_softering = 0
    with open(os.path.join(settings.MODELS_ROOT, 'ml4.pkl'), 'rb') as f:
        gbr_4_column_softering = dill.load(f)

    svr_5_column_elasticity = 0
    with open(os.path.join(settings.MODELS_ROOT, 'ml5.pkl'), 'rb') as f:
        svr_5_column_elasticity = dill.load(f)
