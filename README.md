# Griefbot

## Description
This is a simple python bot to destroy an entire server, send a message to alert everyone and then ban everyone. It's not very fancy, but it does the trick.

## How to use?
1. Download the zip-file and unzip it.
2. Install [python 3](https://www.python.org/downloads/).
3. Go to your browser, go to [discord.com/developers](discord.com/developers), in the top right, click 'New Application'. Give it a name and proceed.
4. On the left of your screen go to 'Bot', press add bot. Copy the token.
5. Go to the griefbot.py file, open it in vscode, notepad, whatever, paste the token into the "token here", leave the quotes.

### Configuration
The bot is customizable, make sure to pay attention to every single thing you enter in the configuration part of the bot.
1. **Authorized:** Paste your own discord id here (or anyone you want to be able to run commands.) ([how to get your discord id?](https://hatebin.com/tuqbtgqmbe))
2. **Channels:** When nuking the server the bot creates 3 channels, 1 announcement channel where the bot and administrators can talk, 1 general channel, and one voice channel. Here you can customize their names.
3. **Embeds:** After creating the channels, the bot sends 2 messages, here you can elaborate why you nuked the server or just have some fun.
4. **server name and icon:** The bot also changes the server icon and name. Make sure you put an image with the name 'image0.png' in the directory where the bot is ran from.
5. **ban reason and sleep time:** There is a time between nuking and banning everyone, put this interval in seconds in the sleep_time variable. the ban_reason variable contains the reasoning the bot uses for banning people.
6. **Finalize:** Try the bot out in a private server to make sure everything works. Invite the bot into the server you want to grief ([how to invite your bot?](https://hatebin.com/baofvavspl)), there are 2 commands, **nuke**, this command nukes the whole server, creates the new channels etc. Perfect if you want to create a commotion. **banall**, this command silently bans everyone, perfect if you don't want people to notice. Before running the commands obviously open the configured python file on your computer.

## Disclaimer
This bot is only made to have fun with friends or experiment. Not to cause harm to other people.
