rootdir = "/your-path/" # directory where you've cloned the repo
docker_service = "" # (optional) docker service name that needs to be restarted (defaults to all)
bot_token = "" # Telegram bot token
chat_id = "" # Telegram chat ID


url = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/NostalgiaForInfinityX2.py"
file = rootdir + "/NostalgiaForInfinityX2.py"

url_blacklist = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/blacklist-kucoin.json"
file_blacklist = rootdir + "/configs/blacklist-kucoin.json"

url_pairlist = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/pairlist-volume-kucoin-usdt.json"
file_pairlist = rootdir + "/configs/pairlist-volume-kucoin-usdt.json"

command = "cd " + rootdir + " && /usr/bin/docker-compose restart " + docker_service
