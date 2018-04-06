# std library
import json
from pprint import pprint

# installed modules
from ebaysdk.trading import Connection as Trading
import click

# local module
from ebay_scripts import EBAY_API
from ebay_scripts.utility import convert_rdo_list_to_dict


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

    items_list = convert_rdo_list_to_dict(active_list.ItemArray.Item)
    pprint(items_list)

    json.dump(items_list, open(output, 'w'))


if __name__ == '__main__':
    get_my_ebay_selling()
