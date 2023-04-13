# AutoUpdateNFIX2 : Strategy + Blacklist
# Author : crashzanders
# Version : 1.2

import requests, re, subprocess
from datetime import datetime

url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/NostalgiaForInfinityX2.py"
url_blacklist = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/blacklist-kucoin.json"   # Change with your exchange blacklist
file = "/your-path/NostalgiaForInfinityX2.py"   # Change with your strategy file path
file_blacklist = "/your-path/blacklist-kucoin.json"     # Change with your blacklist file path
command = "cd /bots/freqtrade && /usr/bin/docker-compose restart"   # Change with your docker-compose file path
bot_token = "your-telegram-bot-token"   # Change with your Telegram bot token
chat_id = "your-telegram-chat-id"   # Change with your Telegram chat ID
change = False

def check_version_online(url):
    file_path = url
    content = requests.get(file_path).text
    pattern = r"v\d+\.\d+\.\d+"
    match = re.search(pattern, content)
    version_online = match.group(0)
    print("Online version of the strategy : " +version_online)
    return version_online

def check_version_file(file):
    with open(file, "r") as file:
        content = file.read()
    pattern = r"v\d+\.\d+\.\d+"
    match = re.search(pattern, content)
    version = match.group(0)
    print("Local strategy version : " +version)
    return version

def update_file(url, file):
    response = requests.get(url)
    file_path = file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(response.text)

def send_notification(bot_token, chat_id, message):
    url_telegram = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url_telegram).json()

print("--- LAUNCHING THE STRATEGY UPDATE SCRIPT ---")
current_time = datetime.now().strftime("%Y/%m/%d - %H:%M")
print("--- "+current_time+" ---")

# Check and upgrade strategy file
version_online = str(check_version_online(url))
version_file= str(check_version_file(file))
if version_file != version_online:
    print("New strategy version detected: Update")
    send_notification(bot_token, chat_id, "New version of NostalgiaForInfinityX2 strategy detected. Upgrade in progress...")
    update_file(url, file)
    print("Updated strategy")
    change = True
else:
    print("Strategy : Updated version")

#Check and upgrade blacklist file
response = requests.get(url_blacklist)
remote_content = response.content.decode('utf-8')
with open(file_blacklist, 'r') as f:
    local_content = f.read()
if remote_content != local_content:
    print("New blacklist version detected: Update")
    send_notification(bot_token, chat_id, "New version of blacklist detected. Upgrade in progress...")
    with open(file_blacklist, 'w') as f:
        f.write(remote_content)
    print("Updated blacklist")
    change = True
else:
    print("Blacklist : Updated version")

#Restart process
if change == True:
    send_notification(bot_token, chat_id, "Upgrade completed. Restart services...")
    subprocess.run(command, shell=True)
    print("Restarted services")

print("--- END OF THE STRATEGY UPDATE SCRIPT ---\n")
