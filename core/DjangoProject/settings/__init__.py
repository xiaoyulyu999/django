from pathlib import Path
import os
from split_settings.tools import include, optional


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Namespacing our own custom environment variables

ENVVAR_SETTINGS_PREFIX = 'CORESETTINGS_'

LOCAL_SETTINGS_PATH = os.getenv(ENVVAR_SETTINGS_PREFIX + 'LOCAL_SETTINGS_PATH')

if not LOCAL_SETTINGS_PATH:
    """
    If it is no env given. go for local settings
    """
    LOCAL_SETTINGS_PATH = 'local/settings.dev.py'

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = os.path.join(BASE_DIR, LOCAL_SETTINGS_PATH)

include(
    'base.py',
    'custom.py',
    optional(LOCAL_SETTINGS_PATH),
    'envvars.py',
    'docker.py',
)

"""
What happening in here:
1. When Django starts, load the settings file at base.py
2. Loading the custom.py settings file [this file only for this app settings only, and this is the reason why we
split the settings]
3. Then check if there is local settings file and environment variables.
"""
