import discord
import random

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)
@clien.event
    anync def on_message(messege):
    if messege.author == client.user:
        return
    if message.content.startwith("$random1-10")
        await message.channel.send(random.randit(1,10))

client.run("MTI0OTAwMTM5MzgyMjM3MTkxMA.GlSINk.tEb_cZp8CFlf-7iAReVJiavYr7X0w6s4JVy6XU")