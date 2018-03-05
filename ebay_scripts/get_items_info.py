from pprint import pprint
import json

import click
from ebaysdk.trading import Connection as Trading

from ebay_scripts import EBAY_API


def get_user():
    api = Trading(config_file=EBAY_API)
    response = api.execute('GetUser', {})
    print(response)


@click.command()
@click.option('--output', '-o',
              default='eBay Items Info (from IDs).json', type=click.STRING)
@click.argument('ebay_item_ids_json_file')
def get_item_info_from_item_ids(ebay_item_ids_json_file, output):
    """Takes a JSON file containing a list of ebay item IDs, uses ebay api
    to get information on each one

    :param ebay_item_ids_json_file: JSON files containing a list of ebay \n
        item IDs
    :param output: output file that contains info on all ebay items
    :return:
    """
    api = Trading(config_file=EBAY_API)
    ids = json.load(open(ebay_item_ids_json_file, 'r'))

    items_data = {}
    for item_id in ids:
        response = api.execute('GetItem', {'ItemID': item_id})
        response_data_object_object = response.reply.Item
        items_data.update({item_id: response_data_object_object.__dict__})
        print(item_id)

    pprint(items_data)
    json.dump(items_data, open(output, 'w'))
