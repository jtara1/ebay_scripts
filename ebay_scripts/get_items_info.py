from pprint import pprint
import click
import json
import os
from ebaysdk.trading import Connection as Trading
from ebay_test.config import *
# EBAY_API = os.path.abspath(os.environ.get('EBAY_API'))
EBAY_API = os.path.abspath('/home/hka/Documents/ebay_api.yaml')


def get_user():
    api = Trading(config_file=EBAY_API)
    response = api.execute('GetUser', {})
    print(response)


@click.command()
@click.option('--output', default='ebay items data.json', type=click.STRING)
@click.argument('ebay_item_ids_json_file')
def trading(ebay_item_ids_json_file, output):
    api = Trading(config_file=EBAY_API)
    ids = json.load(open(ebay_item_ids_json_file, 'r'))

    items_data = {}
    for item_id in ids:
        response = api.execute('GetItem', {'ItemID': item_id})
        # dont ask me why they put object in the name of the class
        response_data_object_object = response.reply.Item
        items_data.update({item_id: response_data_object_object.__dict__})
        print(item_id)

    pprint(items_data)
    json.dump(items_data, open(output, 'w'))

    # response = api.execute_request('https://api.ebay.com/buy/browse/v1/item/v1|282835903438|0')
    # response = api.execute('GetItem', {'item_id': 'v1|282835903438|0'})

    # response = api.execute('GetUser', {})