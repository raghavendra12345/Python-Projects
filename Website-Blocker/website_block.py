import time
from datetime import datetime as dt

#host_temp="hosts"
host_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

website_block=["www.facebook.com","facebook.com","www.instagram.com","instagram.com"]

while True:
    if dt(dt.now().year, dt.now().month,dt.now().day,8)< dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,20):
        print("Working Hours...! Do not Disturb")
        with open(host_path,'r+') as file:
            content=file.read()
            #print(content)
            for website in website_block:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")

    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_block):
                    file.write(line)
            file.truncate()            
        print("Enjoy Time")
