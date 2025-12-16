from pathlib import Path
import os.path
from split_settings.tools import include, optional


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing our own custom environment variables

ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(ENVVAR_SETTINGS_PREFIX + 'LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'
