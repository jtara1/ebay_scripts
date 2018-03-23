import json
from pprint import pprint

import click
from ebaysdk.trading import Connection

from ebay_scripts import EBAY_API
from ebay_scripts.utility import convert_rdo_to_dict


@click.command()
@click.argument('username')
@click.option('--output', '-o',
              type=click.STRING, default='eBay User Info.json')
def get_user(username, output):
    """Get info on a user from eBay

    :param username: user name / id of user we get info on
    :param output: the file path which contains the info, JSON formatted
    """
    api = Connection(config_file=EBAY_API)
    response = api.execute(
        'GetUser',
        {'UserID': username})

    user_response_data_object = response.reply.User

    items_list = convert_rdo_to_dict(user_response_data_object)
    json.dump(items_list, open(output, 'w'))

    pprint(items_list)


if __name__ == '__main__':
    get_user()
