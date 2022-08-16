import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.startswith('$hello'):
        await channel.send('Hello!')

@client.event
async def on_message(message):
    channel = message.channel
    members = channel.guild.members

    if message.content.startswith('!pingpong'):
        for member in members:
            if member != message.author:
                if message.content.startswith('!pingpong ' + member.mention):
                    await channel.send('{}, вы начали игру в Пинг Понг с пользователем {}!'
                                       .format(message.author.mention, member.mention))
                    break

client.run('MTAwODQzMDE0NzcyMjAyNzAwOA.G5lphK.nU5ETEbRY4AxnwiCWIegBfCCzQiHYJVmTCh6Lk')