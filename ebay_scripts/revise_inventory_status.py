# std library
import json
from pprint import pprint, pformat

# installed modules
from ebaysdk.trading import Connection as Trading
import click

# local module
from ebay_scripts import EBAY_API, LOGGER
from ebay_scripts.utility import convert_rdo_to_dict
from ebay_scripts.exception import EbayScriptsException


def revise_inventory_status(item_id, price=None, quantity=None, sku=None):
    """Revise the price or quantity or SKU of an item you own on ebay given
    its item id. A price or quantity must be provided at the very least.

    :param item_id: ebay item id
    :param price: change item price to this
    :param quantity: change item quantity to this
    :param sku: change item SKU to this
    :return: the response from ebay api call
    """
    if price is None and quantity is None:
        raise EbayScriptsException('price or quantity needs to be specified')

    api = Trading(config_file=EBAY_API)

    new_status = {'ItemID': item_id}
    if quantity is not None:
        new_status.update({'Quantity': quantity})
    if price is not None:
        new_status.update({'StartPrice': price})
    if sku is not None:
        new_status.update({'SKU': sku})

    response = api.execute(
        'ReviseInventoryStatus',
        {'InventoryStatus': new_status})

    pretty_reply = pformat(convert_rdo_to_dict(response.reply))
    print(pretty_reply)
    LOGGER.info(pretty_reply)

    return response


@click.command()
@click.argument('item_id')
@click.option('--price', '-p',
              type=click.FLOAT,
              help='Change item StartPrice to this price')
@click.option('--quantity', '-q',
              type=click.STRING, help='Change item quantity to this')
@click.option('--sku', '-s',
              type=click.STRING, help='Change item SKU to this')
def cli_wrapper(item_id, price, quantity, sku):
    return revise_inventory_status(item_id, price, quantity, sku)


if __name__ == '__main__':
    cli_wrapper()
