import json

from requests import request

url = "https://poetrydb.org/title/Ozymandias/lines.json"
res = request(url=url, method="GET").json()
print(json.dumps(res))
