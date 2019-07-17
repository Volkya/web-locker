import time 
from datetime import datetime as dt

# Host Files
# Windows: c:\\windows\system32\drivers\etc
# Mac & Linux: /etc/hosts

# Dir hosts
hosts_path_windows = r"C:\Windows\System32\drivers\etc\hosts" # clean text
hosts_path_unix = "/etc/hosts" # run as SU, example: sudo python3 index.py

# Change your configuration
# host_dir = hosts_path_unix
host_temp = ('hosts_path_unix')
redirect = "127.0.0.1"

# list of websites to block
website_list = [
    "www.facebook.com"
    "facebook.com"
    "twitter.com"
    "mail.google.com"
    "google.com"
    "instagram.com"
    "vk.com"
    "youtube.com"
    ]

# Define working hours
from_hour = 9
to_hour = 13

# Main program
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, from_hour) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, to_hour):
        print('Working...')
        with open(host_temp, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print('fun...')
        with open(host_temp, 'r+') as file:
            content = file.readlines()
            file.seed('0')
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()                                                                                              )
    time.sleep(1) #seconds