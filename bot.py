import os
import discord
import random
import requests
from dotenv import load_dotenv

load_dotenv('shh.env')


response = requests.get("https://manan-api.herokuapp.com/bottle")
manan_bottle = response.json()

responseg = requests.get("https://manan-api.herokuapp.com/guitar")
manan_guitar = responseg.json()

responsew = requests.get("https://manan-api.herokuapp.com/waxing")
manan_wax = responsew.json()


TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    username= str(message.author).split('#')[0]
    user_message = (message.content)
    channel = str(message.channel.name)

    print(f'{username}: {user_message} in channel {channel}')

    if message.author == client.user:
        return 

    if message.channel.name == 'manan':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}, do you want manan pics? type pics')
            
        if user_message.lower() == 'pics':
            await message.channel.send("Categories:\n-Bottle (bottle pics)\n-Guitar (guitar pics)\n-Waxing (waxing pics)\n-Random (random pics)\n")
        if user_message.lower() == 'bottle pics':
            await message.channel.send(manan_bottle['message'])
            await message.channel.send(manan_bottle['img'])

        if user_message.lower() == 'guitar pics':
            range12 = random.randint(0,1)
            await message.channel.send(manan_guitar[range12]['message'])
            await message.channel.send(manan_guitar[range12]['img'])
        
        if user_message.lower() == 'waxing pics':
            range14 = random.randint(0,3)
            await message.channel.send(manan_wax[range14]['message'])
            await message.channel.send(manan_wax[range14]['img'])
        
client.run(TOKEN)