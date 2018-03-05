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

for viewing docstring and CLI arguments, check `GetMyeBaySelling --help` 

## Example Output

```
[{  
      "Title":"Circuit Scribe Maker Kit: Draw Circuits Instantly - Conductive Ink Pen",
      "ItemID":"282835903735",
      "Quantity":"1",
      "ListingDuration":"Days_30",
      "SellerProfiles":{  
         "SellerReturnProfile":{  
            "ReturnProfileID":"73688270018",
            "ReturnProfileName":"No returns accepted"
         },
         "SellerPaymentProfile":{  
            "PaymentProfileID":"115899394018",
            "PaymentProfileName":"PayPal#0"
         },
         "SellerShippingProfile":{  
            "ShippingProfileID":"121434259018",
            "ShippingProfileName":"Calculated:UPS Ground,Same business day"
         }
      },
      "PictureDetails":{  
         "GalleryURL":"http://thumbs.ebaystatic.com/pict/2828359037356464_1.jpg"
      },
      "ListingDetails":{  
         "ViewItemURLForNaturalSearch":"http://cgi.ebay.com/Circuit-Scribe-Maker-Kit-Draw-Circuits-Instantly-Conductive-Ink-Pen?item=282835903735&category=28133&cmd=ViewItem",
         "StartTime":"2018-02-05 01:44:38",
         "ViewItemURL":"http://www.ebay.com/itm/Circuit-Scribe-Maker-Kit-Draw-Circuits-Instantly-Conductive-Ink-Pen-/282835903735"
      },
      "ClassifiedAdPayPerLeadFee":{  
         "value":"0.0",
         "_currencyID":"USD"
      },
      "ShippingDetails":{  
         "ShippingType":"Calculated",
         "GlobalShipping":"true",
         "ShippingServiceOptions":null
      },
      "BuyItNowPrice":{  
         "value":"85.0",
         "_currencyID":"USD"
      },
      "QuantityAvailable":"1",
      "ListingType":"FixedPriceItem",
      "TimeLeft":"P1DT23H55M18S",
      "SellingStatus":{  
         "CurrentPrice":{  
            "value":"85.0",
            "_currencyID":"USD"
         }
      }
   },
]
```