from urllib import request, parse
import json

url = 'https://neutrinoapi.net/host-reputation'
params = {
    'user-id': 'yarin56567',
    'api-key': 'TFRCtbfvpy8MM6YR3tEpftpAiGyBX0cEYrw89LuNSbIp0lUf',
    'host': '87.68.112.117'
}

postdata = parse.urlencode(params).encode()
req = request.Request(url, data=postdata)
response = request.urlopen(req)
result = json.loads(response.read().decode("utf-8"))

print(result)