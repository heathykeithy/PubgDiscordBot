># PubgDiscordBot

Bot in python that retrieves the last Pubg match of the user and displays some basic stats as a reply message.

## Install

From PugbDiscordBot directory run
 ``pip install -r requirements.txt``
 
 *note: using python 3.8.0*

Create a Pubg developer account here ``https://developer.pubg.com/``
 
Add your Pubg Developer API token at ``apiKey`` in pubgDiscordbot.py script

Create discord bot via developer portal info here ``https://discordpy.readthedocs.io/en/latest/discord.html``
Give bot appropriate permissions (read messages, write messages etc.)  

Add you discord bot token at ``client.run`` in pubgDiscordbot.py script
## Run

``python discordStatsBot.py``

## Usage
In your Discord server type ``!last`` in a text channel to test 

*Note: Users name in discord MUST be exactly as it is in game name(IGN). Change discord nickname to match IGN.*
