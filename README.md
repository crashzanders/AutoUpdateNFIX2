# AutoUpdateNFIX2
Python script that automates the update of the freqtrade strategy of NostalgiaForInfinityX2 (https://github.com/iterativv/NostalgiaForInfinity) and/or the blacklist and/or pairlist associated with your exchange.

## How does it work?
The script checks the online and local version of the strategy and/or blacklist and/or pairlist.
There are 4 files available:
- update_strategy: update only the strategy
- update_strategy_blacklist: update of strategy and blacklist
- update_strategy_pairlist: update of strategy and pairlist
- update_strategy_blacklist_pairlist: update of the strategy, the blacklist and the pairlist

If there is a difference, it updates the local version, restarts the docker, and notifies the user on Telegram of the update.

![upgrade screen telegram](https://i.imgur.com/66s1rgV.png)

## Adapt the script
You have to modify the following variables with the path of your strategy, your blacklist/pairlist and your docker-compose.yml :
```
file = "/your-path/NostalgiaForInfinityX2.py"
file_blacklist = "/your-path/blacklist-kucoin.json"
file_pairlist = "/your-path/pairlist-volume-kucoin-usdt.json"
command = "cd your-docker-compose-path && /usr/bin/docker-compose restart"
```
You must also adapt the URL of the blacklist with the one adapted to your exchange :
```
url_blacklist = "https://raw.githubusercontent.com/iterativv/NostalgiaForInfinity/main/configs/blacklist-kucoin.json"
```
You must also enter your Telegram token and chat-id to receive notifications when updates are made:
```
bot_token = "6XXXXXXXXXXXXXXXXXXXXXXXX8U"
chat_id = "12XXXXX35"
```

## Automatically run the script :
Personally I want the script to be executed every hour to be updated as often as possible. To do this I run the following command on my server:
```
sudo crontab -e
```
And I add the following line:
```
15 * * * * /usr/bin/python3 /your-path/update_strategie.py >> /var/log/logs_update_strategie.log 2>&1
```

## Next developments:
- ~~Update the blacklist associated with his exchange and his crypto currency at the same time~~
- Automatic execution of the script at each commit of the NFI repo.
