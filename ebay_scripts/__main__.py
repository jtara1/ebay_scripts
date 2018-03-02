import json
import click
import os
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from ebaysdk.shopping import Connection as Shopping
from ebay_test.config import *
EBAY_API = os.path.abspath(os.environ.get('EBAY_API'))
# EBAY_API = os.path.abspath('/home/hka/Documents/ebay_api.yaml')


def finding():
    try:
        api = Connection(config_file=EBAY_API)
        # api = Connection(appid=APP_ID, config_file=None)
        # response = api.build_request_url('https://api.ebay.com/buy/browse/v1/item/get_item_by_'
        #                       'legacy_id?legacy_item_id={legacy_item_id}'
        #                       .format(legacy_item_id=282857238025))
        response = api.execute('findItemsAdvanced', {'keywords': 'legos'})
        # response = api.execute('getItemByLegacyId', {'legacy_item_id': '282857238025'})
        print(response.dict())
        print(response.reply)

        assert(response.reply.ack == 'Success')
        assert(type(response.reply.timestamp) == datetime.datetime)
        assert(type(response.reply.searchResult.item) == list)

        item = response.reply.searchResult.item[0]
        assert(type(item.listingInfo.endTime) == datetime.datetime)
        assert(type(response.dict()) == dict)
        print('done')

    except ConnectionError as e:
        print(e)
        print(e.response.dict())


def shopping():
    try:
        api = Shopping(appid=APP_ID, config_file=None)
        response = api.execute('FindPopularItems',  {'QueryKeywords': 'clothes'})
        print(response.dict())
        print(response.reply)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())


if __name__ == '__main__':
    # finding()
    # shopping()