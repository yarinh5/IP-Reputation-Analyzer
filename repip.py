import sys
import ReputationSource
from urllib import request, parse
import json


repSources = []


def main(argv):
    print("The reputation from Neutrino & VirusTotal")
    sum = 0
    for i in range(1, len(argv)):
        for repuSource in ReputationSource.reputationSources:
            print(repuSource.getReputation(argv[i]))
            sum += repuSource.getReputation(argv[i])
    sum = sum/2
    if sum >= 0 and sum <= 4:
            print("The IP is clean.")
    elif sum >= 5 and sum <= 7:
        print("The IP is suspicious.")
    else:
        print("The IP is malicious.")
    choice = int(input("\nYou Need More info?\nPress 1 else 0\n"))
    if choice == 1:
        moreInfo()
    else:
        print("Goodbye")
    
def moreInfo():
    url = 'https://neutrinoapi.net/ip-info'
    params = {
    'user-id': 'yarin56567',
    'api-key': 'TFRCtbfvpy8MM6YR3tEpftpAiGyBX0cEYrw89LuNSbIp0lUf',
    'ip': '87.68.112.117'
    }

    postdata = parse.urlencode(params).encode()
    req = request.Request(url, data=postdata)
    response = request.urlopen(req)
    result = json.loads(response.read().decode("utf-8"))

    print(result)


              
        
if __name__ == '__main__':
    main(sys.argv)