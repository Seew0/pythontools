#!/usr/bin/env python3

import argparse
import requests

p=argparse.ArgumentParser(description='vulnerability check')
p.add_argument('-v','--version',action='version',version='v1.0',help='version of tool')
p.add_argument('url',type=str,help='enter your url with scheme')
args=p.parse_args()

url=args.url

try :
    response = requests.get(url)
except:
    print("Use correct URL scheme")
    exit(1)


if(response.status_code==200):
    response= requests.get(url+ '/wp-admin')
    
    if(response.status_code==404):
        print('Admin page do not exist or hidden for this site(not a vulnerable site)')
    elif(response.status_code==200):
        print('Vulnerable site')
    else:

        print('not a vulnerable site')
else:
    print('request failure')
