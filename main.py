import discord

print("Welcome!")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="with your cock"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('cock and balls'):
        await message.channel.send('8====D')
        print("simdutz sent!")

    if message.content.startswith('Cock and Balls'):
        await message.channel.send('8====D')

client.run('enter your token here')
