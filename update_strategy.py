import requests, re, subprocess
from datetime import datetime

url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/NostalgiaForInfinityX2.py"
file = "/bots/freqtrade/user_data/strategies/NostalgiaForInfinityX2.py"
command = "cd /bots/freqtrade && /usr/bin/docker-compose restart"
bot_token = "your-telegram-bot-token"
chat_id = "your-telegram-chat-id"


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
version_online = str(check_version_online(url))
version_file= str(check_version_file(file))

if version_file != version_online:
    print("New version detected: Update")
    send_notification(bot_token, chat_id, "New version of NostalgiaForInfinityX2 strategy detected. Upgrade in progress...")
    update_file(url, file)
    print("Updated strategy")
    send_notification(bot_token, chat_id, "Upgrade completed. Restart of services...")
    subprocess.run(command, shell=True)
    print("Restarted services")
else:
    print("Updated version")
print("--- END OF THE STRATEGY UPDATE SCRIPT ---\n")
