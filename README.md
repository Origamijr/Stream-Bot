## Installation
The following libraries are used

- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- requests
- toml

You may install these dependencies manually, or use the command

```
pip install -r requirements.txt
```

## Configuration
The following configurations can be set in the config.toml file:

- __prefix__: the prefix used to indicate a bot command
- **Discord**
    - __streamer__: the username of the streamer you want to track
    - __loop__: how many seconds are elapsed between each check
    - __channel_id__: the id of the channel twitch live notifications should be sent to (right click on channel in discord and select "CopyID")

Tokens are stored in a file named "tokens.toml". This file is not included in the github and should be created. It should have the following layout at bare minimum with the corresponding entries filled in:

```
[Discord]
token = ...

[Twitch]
client_id = ...
client_secret = ...
```

### Discord Token Acquisition and Bot Setup
To get a discord bot token, go to https://discord.com/developers/applications, create a bot application, and fill in the necessary data (permissions shouldn't matter).

To get the secret token, in the left panel go to Bot -> TOKEN -> "Click to Reveal Token". Do NOT make this token public, as it will allow anyone to use your bot.

To invite the bot to a server, find the bot's client id (also called application id), and paste it into the following link 
```
https://discord.com/api/oauth2/authorize?client_id=**ID_GOES_HERE**&scope=bot&permissions=**PERMISSIONS_GO_HERE**
```

For more information on how to invite a bot go [here](https://discord.com/developers/docs/topics/oauth2#bots)

### Twitch Token Acquisition
Go to the [Twitch Developer Console](https://dev.twitch.tv/console) and register a new application (you'll be required to set up two-factor authentication for your twitch account).

Name the application whatever you want, enter "http://localhost" as the OAuth Redirect URL, and set the category to "Application Integration".

Copy the generated "Client ID" and "Client Secret" into the tokens.toml file.

## Usage
To run, run main.py
```
python main.py
```

Test if the bot is online with "/ping". Hopefully it'll work.