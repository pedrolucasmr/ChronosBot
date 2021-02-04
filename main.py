import discord
from time import gmtime, strftime
from datetime import datetime
import pytz
import os

client = discord.Client()

@client.event
async def on_ready():
    print("WE ARE MOTHERFUCKING READY! I'M {0.user}".format(client))

@client.event
async def on_message(message):
    #if message.content.startswith("!Horas"):        
    #    await message.channel.send(MensagesServ)
    if message.content.startswith("!Ana"):
        await message.channel.send("Ana Júlia é uma sulista fedida, porém gente boa")

    elif message.content.startswith("!Pedro"):
        await message.channel.send("Um amorzinho, porém um belissímo de um babaca")

    elif message.content.startswith("!Juh"):
        await message.channel.send("Fofa, linda, inteligente, engraçada e chata pra caralho. Combina bastante com o namorado")

    elif message.channel.send("!Igor"):
        await message.channel.send("Baixista, porém bonitão")
        
    elif message.channel.send("!Vitor"):
        await message.channel.send("Muito maneiro, pena que não dá pra entender metade do que ele fala.")

    elif message.channel.send("!Lucas"):
        await message.channel.send("Inteligentissímo, mas quando ele começa a falar tu acaba dormindos")

client.run(os.getenv("TOKEN"))
