from config.settings.base import env
from django.core.exceptions import ImproperlyConfigured

ENV_NAME = env('ENV_NAME')

if ENV_NAME == 'PRODUCTION':
    from .production import *
elif ENV_NAME == 'STAGING':
    from .staging import *
elif ENV_NAME == 'DEVELOPMENT':
    from .development import *
elif ENV_NAME == 'LOCAL':
    from .local import *
else:
    raise ImproperlyConfigured('Plz set proper values to ENV_NAME environment variable.')

###############################################
# ############ Import Sub-settings ########## #
###############################################
try:
    from ._sub_settings._env_variables import *
    from ._sub_settings._rest_framework import *
    from ._sub_settings._security import *
    from ._sub_settings._logger import *
except Exception as ex:
    import sys

    error_type, error_value, traceback = sys.exc_info()
    filename = traceback.tb_frame.f_globals.get("__file__")
    error_message = f"ImportError: {ex}, File: {filename}"
    print(error_message)
    raise ImportError(error_message)