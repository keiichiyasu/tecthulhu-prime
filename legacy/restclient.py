#!/usr/bin/env python3
#
# Title:      REST client
# Author:     Martin Brenner
#

import json, requests
import time


class restclient:

    def __init__(self):
	#self.BASEURL="http://tecthulhu.boop.blue"
	self.BASEURL="http://tecthulhuff.local/portals/Tecthulhu01.json"
	# Placeholder URL - User needs to configure this in installation.md
	#self.BASEURL="http://localhost:8080/module/status/json"


    def getjson(self):
        #reqstr = self.BASEURL + "/module/status/json"
        reqstr = self.BASEURL
        print(reqstr)
        try:
            r = requests.get(reqstr, timeout=5)
            #print("Status: ", r.status_code)
            if r.status_code == requests.codes.ok:
                return r.json()
            else:
                return 0
        except requests.exceptions.RequestException as e:
            print(f"Connection Error: {e}")
            return 0

    def main(self):
        json_data = self.getjson() # renamed json to json_data to avoid masking import
        if json_data != 0:
            print("JSON: ", json_data)
            if 0:
                print("Faction:", json_data['externalApiPortal']['controllingFaction'])
                print("Level:", json_data['externalApiPortal']['level'])
                print("Health:", json_data['externalApiPortal']['health'])
                print("Title:", json_data['externalApiPortal']['title'])
                print("Resonators:", len(json_data['externalApiPortal']['resonators']))
                for i in range(0, len(json_data['externalApiPortal']['resonators'])):
                    print(json_data['externalApiPortal']['resonators'][i]['position'])
            else:
                # Basic check for structure before printing to avoid crashes in main test
                if 'status' in json_data:
                    print("Faction:", json_data['status'].get('controllingFaction'))
                    print("Level:", json_data['status'].get('level'))
                    print("Health:", json_data['status'].get('health'))
                    print("Title:", json_data['status'].get('title'))
                    res_len = len(json_data['status'].get('resonators', []))
                    print("Resonators:", res_len)
                    for i in range(0, res_len):
                        print(json_data['status']['resonators'][i]['position'])
                else:
                    print("Unknown JSON structure")

        else:
            print("Error")

if __name__ =='__main__':
        rclient = restclient()
        rclient.main()



