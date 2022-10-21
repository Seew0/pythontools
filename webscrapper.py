#!/usr/bin/env python3

import argparse
import requests
from requests.models import Response
import selenium
from bs4 import BeautifulSoup as bs 

parser = argparse.ArgumentParser(description='Web Scrapping Tool v1.0')
parser.add_argument('url',type=str,help="Put the url with the scheme")
parser.add_argument('-v','--version',action='version',version='Web Scrapping Tool v1.0')
args=parser.parse_args()

url=args.url

if url.startswith("www"):
    url = "https://" + url;

Response = requests.get(url)
soup=bs(Response.content,'html.parser')
if(Response.status_code==200):
    while(1):
        print("0.To Parse the text")
        print("1.To Parse all href")
        print("2.To Parse all image")
        print("3.To Parse html")
        print("4.exit")
        choice=int(input("(0/1/2/3/4) "))
        print(choice)
        if(choice==0):
            print(Response.content)
        if(choice==1):
            for link in soup.find_all('a'):
                print(link.get('href'))
        if(choice==2):
            images_list=[]
            images=soup.select('img')
            for image in images:
                src=image.get('src')
                alt=image.get('alt')
                images_list.append({"src": src,"alt": alt})

            for image in images_list:
                print(image)
        if(choice==3):
            print(soup.prettify())
        if(choice==4):
            exit(1)
        

        
