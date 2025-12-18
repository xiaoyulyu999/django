from core.core.utils.collections import deep_update
from core.core.utils.settings import get_settings_from_environment

"""
For instance:
export CORESETTINGS_IN_DOCKER=true (Environment variables)
Could then be referenced as a global variable as:

IN_DOCKER (where the value would be True)
"""
# globals() - dictionary of global variables

deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
