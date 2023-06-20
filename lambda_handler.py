import requests

url = 'https://j0dulj4ywh.execute-api.ap-southeast-2.amazonaws.com/default/MSyncForContenful';
headers = {
                    'X-Api-Key': '6bdxyzkVgKAj9jrBPO9e2PvR73qCg2t9zwtFMYH8',
                    'access-control-allow-origin': '*',
                    'origin': 'https://app.contentful.com',
                    'Content-Type': 'application/json'
                }
def lambda_handler(event, context):
  return requests.get(url, headers=headers);
