# AutoUpdateNFIX2
Python script that automates the update of the freqtrade strategy of NostalgiaForInfinityX2 (https://github.com/iterativv/NostalgiaForInfinity) 

## Adapt the script
You have to modify the following variables with the path of your strategy and the path of your docker-compose.yml :
```
file = "/your-path/NostalgiaForInfinityX2.py"
command = "cd your-docker-compose-path && /usr/bin/docker-compose restart"
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
