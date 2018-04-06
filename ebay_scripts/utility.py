import datetime
from ebaysdk.response import ResponseDataObject

from ebay_scripts import JSON_ACCEPTED_TYPES


def convert_rdo_list_to_dict(rdo_list):
    """Convert a list of objects of type
    :class:`ebaysdk.response.ResponseDataObject` to a list of dictionaries

    :returns: list of dictionaries with the same data defined as attributes \n
        each of the :class:`ebaysdk.response.ResponseDataObject` objects
    """
    return [convert_rdo_to_dict(rdo) for rdo in rdo_list]


def convert_rdo_to_dict(rdo):
    """Convert a :class:`ebaysdk.response.ResponseDataObject` to dict"""
    # the only attributes it has describes the data
    rdo_dict = rdo.__dict__
    for key, value in rdo_dict.items():
        # value is of type ResponseDataObject
        if isinstance(value, ResponseDataObject):
            value_dict = convert_rdo_to_dict(value)
            rdo_dict[key] = value_dict

        # if at least one item is a ResponseDataObject in this list, convert
        # all items in the list to JSON serializeable type
        elif isinstance(value, list) and list_contains_rdo(value):
            rdo_dict[key] = convert_rdo_list_to_dict(value)

        # value is of type datetime.datetime
        elif isinstance(value, datetime.datetime):
            rdo_dict[key] = str(value)

        # value is another type that isn't JSON serializable
        elif not isinstance(value, JSON_ACCEPTED_TYPES):
            raise Exception('{} is unaccepted type for converting to dict'
                            ' for JSON'.format(type(value)))
    return rdo_dict


def list_contains_rdo(sequence):
    return any([isinstance(value, ResponseDataObject) for value in sequence])
