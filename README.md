# AutoUpdateNFIX2
Python script that automates the update of the freqtrade strategy of NostalgiaForInfinityX2 (https://github.com/iterativv/NostalgiaForInfinity).

## How does it work?
The script checks the online and local version of the strategy.
If there is a difference, it updates the local version, restarts the docker, and notifies the user on Telegram of the update.

![upgrade screen telegram](https://i.imgur.com/66s1rgV.png)

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

## Next developments:
- Mise à jour de la blacklist associé à son exchange et sa crypto monnaie en même temps
- Execution automatique du script à chaque commit du repo NFI.
