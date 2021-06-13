import discord

print("Welcome!")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="mit astolfo"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('cock and balls'):
        await message.channel.send('╰⋃╯')
        print("simdutz sent!")

    if message.content.startswith('femboy'):
        await message.channel.send('╰⋃╯')

client.run('ODUzNjgwNzIzMjgwOTIwNjI2.YMY6IQ.1bzKvplIhPTi25WgGKq5c3jBZ6E')
