import datetime
# import click
import json
import os
from ebaysdk.trading import Connection as Trading
from ebaysdk.response import ResponseDataObject
EBAY_API = os.path.abspath('/home/j/Documents/ebay.yaml')
JSON_ACCEPTED_TYPES = (int, float, str, dict, list, bool, type(None))


def convert_to_dict(rdo_list):
    def convert_rdo(rdo):
        rdo_dict = rdo.__dict__
        for key in rdo_dict.keys():
            if isinstance(rdo_dict[key], ResponseDataObject):
                value_dict = convert_rdo(rdo_dict[key])
                rdo_dict[key] = value_dict
            elif isinstance(rdo_dict[key], datetime.datetime):
                rdo_dict[key] = str(rdo_dict[key])
            elif not isinstance(rdo_dict[key], JSON_ACCEPTED_TYPES):
                raise Exception('{} is unaccepted type for converting to dict'
                                ' for JSON'.format(type(rdo_dict[key])))
        return rdo_dict

    converted_list = []
    for rdo in rdo_list:
        converted_list.append(convert_rdo(rdo))
    return converted_list


def get_my_ebay_selling():
    api = Trading(config_file=EBAY_API)
    response = api.execute('GetMyeBaySelling', {'ActiveList': {'Include': True}})

    active_list = response.reply.ActiveList
    print(active_list.PaginationResult)

    items_list = convert_to_dict(active_list.ItemArray.Item)
    json.dump(items_list, open('out.json', 'w'))


if __name__ == '__main__':
    get_my_ebay_selling()