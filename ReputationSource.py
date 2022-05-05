import requests
import json

import sys
import ReputationSource
from urllib import request, parse
import json

'& C:/Users/Yarin/AppData/Local/Programs/Python/Python310/python.exe c:/Users/Yarin/Downloads/repip/repip.py 8.8.8.8'


class ReputationSource():
    def __init__(self,):
        pass
    
    @classmethod
    def getReputation(forIp):
        '''
        return the reputation of an ip as a value of 0 to 10
        where 0 is malicous
        5 is neutral
        and 10 is clean
        '''
        raise Exception("abstract class: does not implement getReputation")
    
 #
 
class NeutrinoReuputationSource(ReputationSource):
    @classmethod
    def getReputation(self, forIp):
        return super().getReputation()
     
     
class YarinReuputationSource(ReputationSource):
    @classmethod
    def getReputation(self, forIp):
        return super().getReputation()
     
    
class VirusTotalReputationSource(ReputationSource):
    # curl --request GET --url https://www.virustotal.com/api/v3/ip_addresses/66.254.114.41  --header "x-apikey: 8494a16cdefab6cf9e119bdfa4cdb0676d10faa02f07d3b58639f7b47b0f5b21"
    
    @classmethod 
    def getReputation(self, forIp):
        
        #TODO: check validity of ip address
        
        header_with_apikey = {"x-apikey":"8494a16cdefab6cf9e119bdfa4cdb0676d10faa02f07d3b58639f7b47b0f5b21"}
        request = requests.get("https://www.virustotal.com/api/v3/ip_addresses/" + forIp, headers=header_with_apikey)
        
        #TODO handle error in getting reguest
        
        requestText = request.text
        
        parsedRequest = json.loads(requestText)
        
        #TODO delete this line
        
        
    
        rep = parsedRequest['data']['attributes']['reputation']

        """
        VirusTotal has developed its own file reputation system. 
        Whenever you submit a file or URL, you'll see a chart which
         shows the reputation of the file or URL and ranges from -100
          (fully malicious reputation) to 100 (fully harmless reputation).
        """
        fmreputation = -100
        fhreputation = 100
        normalization = ((rep-fmreputation)/(fhreputation-fmreputation))*10
        
        if rep>=100:
            return 10
        else :
            return normalization

class neutrinoReputationSource(ReputationSource):
    # curl --request GET --url https://www.virustotal.com/api/v3/ip_addresses/66.254.114.41  --header "x-apikey: 8494a16cdefab6cf9e119bdfa4cdb0676d10faa02f07d3b58639f7b47b0f5b21"
    
    @classmethod 
    def getReputation(self, forIp):
        
        #TODO: check validity of ip address
        
        header_with_apikey = {"x-apikey":"8494a16cdefab6cf9e119bdfa4cdb0676d10faa02f07d3b58639f7b47b0f5b21"}
        request = requests.get("https://www.virustotal.com/api/v3/ip_addresses/" + forIp, headers=header_with_apikey)
        
        #TODO handle error in getting reguest
        
        requestText = request.text
        
        parsedRequest = json.loads(requestText)
               
        rep = parsedRequest['data']['attributes']['reputation']
        fmreputation = -100
        fhreputation = 100
        normalization = ((rep-fmreputation)/(fhreputation-fmreputation))*10
        
        if rep>=100:
            return 10
        else :
            return normalization


         

reputationSources = [VirusTotalReputationSource, neutrinoReputationSource]
        