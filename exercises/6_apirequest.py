import requests
import json

params = {
'q':'Python programming language',
'apiKey': '0a1abe2418f94efe83b73f43037805b9',
'pageSize': 5
}

url = f"https://newsapi.org/v2/everything?q={params['q']}&apiKey={params['apiKey']}&pageSize={params['pageSize']}"

resp = requests.get(url)
json_resp = json.loads(resp.text)
for article in json_resp['articles']:
    print(article['title'])
    print(article['author'])
    print(article['url'])
    print()