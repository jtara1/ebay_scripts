import os
from jtara1_util import setup_logger

# global constants
JSON_ACCEPTED_TYPES = (int, float, str, dict, list, bool, type(None))
EBAY_API = os.path.expanduser(os.environ['EBAY'])
LOGGER = setup_logger('ebay_scripts')
