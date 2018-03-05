# std library
import datetime
import json
from pprint import pprint, pformat

# installed modules
from ebaysdk.trading import Connection as Trading
from ebaysdk.response import ResponseDataObject
import click

# local module
from ebay_scripts import EBAY_API, JSON_ACCEPTED_TYPES


def convert_to_dict(rdo_list):
    """Convert a list of objects of type
    :class:`ebaysdk.response.ResponseDataObject` to a list of dictionaries

    :returns: list of dictionaries with the same data defined as attributes \n
        each of the :class:`ebaysdk.response.ResponseDataObject` objects
    """
    def convert_rdo(rdo):
        """Convert a :class:`ebaysdk.response.ResponseDataObject` to dict"""
        # the only attributes it has describes the data
        rdo_dict = rdo.__dict__
        for key, value in rdo_dict.items():
            # value is of type ResponseDataObject
            if isinstance(value, ResponseDataObject):
                value_dict = convert_rdo(value)
                rdo_dict[key] = value_dict

            # value is of type datetime.datetime
            elif isinstance(value, datetime.datetime):
                rdo_dict[key] = str(value)

            # value is another type that isn't JSON serializable
            elif not isinstance(value, JSON_ACCEPTED_TYPES):
                raise Exception('{} is unaccepted type for converting to dict'
                                ' for JSON'.format(type(value)))
        return rdo_dict

    return [convert_rdo(rdo) for rdo in rdo_list]


@click.command()
@click.option('--output', '-o',
              type=click.STRING, default='eBay Active Selling Items Info.json')
def get_my_ebay_selling(output):
    """Get info on active selling items from ebay. Print results and serialize
    in file path, output, as JSON

    :param output: the file path which contains the items info, JSON formatted
    """
    api = Trading(config_file=EBAY_API)
    response = api.execute(
        'GetMyeBaySelling',
        {'ActiveList': {'Include': True}})

    active_list = response.reply.ActiveList
    print(active_list.PaginationResult)

    items_list = convert_to_dict(active_list.ItemArray.Item)
    json.dump(items_list, open(output, 'w'))

    pprint(items_list)


if __name__ == '__main__':
    get_my_ebay_selling()
