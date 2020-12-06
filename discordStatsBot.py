import requests
import json
import discord
from discord.ext import commands

apiKey = 'REPLACE WITH PUBG API TOKEN HERE'

headers = {
    'Authorization': f"Bearer {apiKey}",
    'Accept': 'application/vnd.api+json',
}

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Secret Nerd')
    print('Online')
    game = discord.Game("!last")
    await client.change_presence(status=discord.Status.online, activity=game)
    
@client.command()
async def last(ctx):
    global playerName
    playerName = ctx.message.author.display_name
    getPlayerName(playerName)
    recentMatch()
    lmInfo()
    stats = selfStats()
    kills = stats['attributes']['stats']['kills']
    damage = stats['attributes']['stats']['damageDealt']
    winPlace = stats['attributes']['stats']['winPlace']
    revives = stats['attributes']['stats']['revives']
    await ctx.send(f'Hi {playerName}. Your last match was in: {mapName} playing {gameMode}.Your position was #{winPlace} with {kills} kills, {round(damage)} damage and {revives} revives')

def getPlayerName(playerName):
    
    response = requests.get(f'https://api.pubg.com/shards/steam/players?filter[playerNames]={playerName}', headers=headers)
        
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def lmInfo():
    global gameMode
    global mapName
    global gameTime
    global lastMatch
    lastMatch = recentMatch()
    gameMode = lastMatch['data']['attributes']['gameMode']
    mapName = lastMatch['data']['attributes']['mapName']
    
    if mapName == "Baltic_Main":
        mapName = "Erangel"
            

    if mapName == "Summerland_Main":
        mapName = "Karakin"
            

    if mapName == "Savage_Main":
        mapName = "Sanhok"
            

    if mapName == "Chimera_Main":
        mapName = "Paramo"

        
    if mapName == "Desert_Main":
        mapName = "Miramar"    

    gameTime = lastMatch['data']['attributes']['duration']

def recentMatch():
    
    name = getPlayerName(playerName)

    #playerId= name['data'][0]['id']
    
    lastMatchId= name['data'][0]['relationships']['matches']['data'][0]['id']
    
    response = requests.get(f'https://api.pubg.com/shards/steam/matches/{lastMatchId}', headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None


def selfStats():
    inclued = lastMatch['included']
    for i in inclued:
        try:
            if i['attributes']['stats']['name'] == playerName:
                return i

        except:
            pass
        



client.run('REPLACE WITH DISCORD BOT TOKEN HERE')


