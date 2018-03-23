# ebay_scripts

`ebay_scripts.get_my_ebay_selling.get_my_ebay_selling` function saves info
on the active selling items of the account tied to the token from the file
`$EBAY`

## Install

Install this module
```
pip3 install git+https://github.com/jtara1/ebay_scripts
```

## Setup for eBay API Usage

Prepare your eBay Developer Application Key 
https://developer.ebay.com/DevZone/account/ for production

Get your token for the ebay account you wish to pull information from 
https://developer.ebay.com/my/auth?env=production&index=0 (**Trading API 
requires Auth'n'Auth not OAuth token**)

Configure your eBay Developer IDs for eBay API to approve of your requests
(paste in information for Trading Production API usage)
```
cd ~/Documents
wget https://raw.githubusercontent.com/timotheus/ebaysdk-python/master/ebay.yaml
nano ebay.yaml
```

Add `EBAY` to environment variables via editing your `.bashrc`
```
nano ~/.bashrc
export EBAY=~/Documents/ebay.yaml
# remainder of .bashrc contents below
```

## Usage

```
GetMyeBaySelling
```

```
GetUser my_user_name
```

Check https://github.com/jtara1/ebay_scripts/blob/master/setup.py#L117
 for updated list of the console entry points that do something
 with this module.

for viewing docstring and CLI arguments, check `GetMyeBaySelling --help` 

## Example Usage with Inputs and Outputs

Note: the response data is pretty printed to std out in console and 
 saved as JSON in $PWD

GetMyeBaySelling
```
(venv) user@hka-OptiPlex-790:~/scripts/ebay_scripts$ GetMyeBaySelling 
{'TotalNumberOfPages': '1', 'TotalNumberOfEntries': '7'}
[{'BuyItNowPrice': {'_currencyID': 'USD', 'value': '69.99'},
  'ClassifiedAdPayPerLeadFee': {'_currencyID': 'USD', 'value': '0.0'},
  'ItemID': '282857237693',
  'ListingDetails': {'StartTime': '2018-02-22 00:37:40',
                     'ViewItemURL': 'http://www.ebay.com/itm/Canon-EOS-Rebel-G-film-camera-28-90mm-zoom-lens-/282857237693',
                     'ViewItemURLForNaturalSearch': 'http://cgi.ebay.com/Canon-EOS-Rebel-G-film-camera-with-28-90mm-zoom-lens?item=282857237693&category=15230&cmd=ViewItem'},
  'ListingDuration': 'Days_30',
  'ListingType': 'FixedPriceItem',
  'PictureDetails': {'GalleryURL': 'http://thumbs.ebaystatic.com/pict/2828572376936464_1.jpg'},
  'Quantity': '1',
  'QuantityAvailable': '1',
  'SellerProfiles': {'SellerPaymentProfile': {'PaymentProfileID': '123',
                                              'PaymentProfileName': 'PayPal#0'},
                     'SellerReturnProfile': {'ReturnProfileID': '123',
                                             'ReturnProfileName': 'No returns '
                                                                  'accepted'},
                     'SellerShippingProfile': {'ShippingProfileID': '123',
                                               'ShippingProfileName': 'Calculated:UPS '
                                                                      'Ground,Same '
                                                                      'business '
                                                                      'day'}},
  'SellingStatus': {'CurrentPrice': {'_currencyID': 'USD', 'value': '69.99'}},
  'ShippingDetails': {'GlobalShipping': 'true',
                      'ShippingServiceOptions': None,
                      'ShippingType': 'Calculated'},
  'TimeLeft': 'PT6H33M42S',
  'Title': 'Canon EOS Rebel G film camera with 28-90mm zoom lens'},

```

GetUser
```
(venv) user@hka-OptiPlex-790:~/scripts/ebay_scripts$ GetUser dere_vigi
{'AboutMePage': 'false',
 'BusinessRole': 'FullMarketPlaceParticipant',
 'EIASToken': 'nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6AGl4SmDJSEow6dj6x9nY+seQ==',
 'Email': 'Invalid Request',
 'EnterpriseSeller': 'false',
 'FeedbackPrivate': 'false',
 'FeedbackRatingStar': 'Yellow',
 'FeedbackScore': '11',
 'IDVerified': 'false',
 'MotorsDealer': 'false',
 'NewUser': 'false',
 'PositiveFeedbackPercent': '100.0',
 'RegistrationDate': '2014-08-25 19:34:18',
 'SellerInfo': {'AllowPaymentEdit': 'true',
                'CIPBankAccountStored': 'false',
                'CharityRegistered': 'false',
                'CheckoutEnabled': 'true',
                'DomesticRateTable': 'false',
                'GoodStanding': 'true',
                'InternationalRateTable': 'false',
                'LiveAuctionAuthorized': 'false',
                'MerchandizingPref': 'OptIn',
                'QualifiesForB2BVAT': 'false',
                'RecoupmentPolicyConsent': None,
                'SafePaymentExempt': 'false',
                'SchedulingInfo': {'MaxScheduledItems': '3000',
                                   'MaxScheduledMinutes': '30240',
                                   'MinScheduledMinutes': '0'},
                'SellerBusinessType': 'Private',
                'SellerGuaranteeLevel': 'NotEligible',
                'StoreOwner': 'false',
                'TransactionPercent': '0.0'},
 'Site': 'US',
 'Status': 'Confirmed',
 'UniqueNegativeFeedbackCount': '0',
 'UniqueNeutralFeedbackCount': '0',
 'UniquePositiveFeedbackCount': '8',
 'UserID': 'dere_vigi',
 'UserIDChanged': 'false',
 'VATStatus': 'NoVATTax',
 'eBayGoodStanding': 'true',
 'eBayWikiReadOnly': 'false'}

```