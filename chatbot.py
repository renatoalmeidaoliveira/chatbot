import discord
import dispacher
import questions
import security

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if not security.authorize(client, message):
        return

    content = message.content
    result = await dispacher.process(content)
    
    if result is not None:
        await message.reply(f'<@{message.author.id}>:\n{result}')


client.run('<discord token>')