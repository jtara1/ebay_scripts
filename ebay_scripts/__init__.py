import os

# global constants
JSON_ACCEPTED_TYPES = (int, float, str, dict, list, bool, type(None))
EBAY_API = os.path.expanduser(os.environ['EBAY'])
