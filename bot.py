from setup import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    def check(m):
        return m.content.startswith('-r') and m.channel == channel
    if message.content.startswith('-o random'):
        channel = message.channel
        parameters = message.content.split(' ')
        chat = RandomChat()
        chat.start()
        while True:
                event, argument = chat.get_event()
                if event == ChatEvent.CHAT_READY:
                    await message.channel.send('**Connected.**')
                    break
                elif event == ChatEvent.CHAT_WAITING:
                    await message.channel.send('**Looking for a partner...**')
        while True:
                event, argument = chat.get_event()
                if event == ChatEvent.GOT_MESSAGE:
                    reply = argument
                    await message.channel.send(f'``{reply}``')
                    answer = await client.wait_for('message', check=check)
                    chat.send(answer.content[3:])
                elif event == ChatEvent.CHAT_ENDED:
                    await message.channel.send("**The chat has ended.**")
                    break
    if message.content.startswith('-o interest'):
        channel = message.channel
        parameters = message.content.split(' ')
        interest = parameters[2]
        chat = InterestsChat([interest, interest])
        chat.start()
        while True:
                event, argument = chat.get_event()
                if event == ChatEvent.CHAT_READY:
                    await message.channel.send('**Connected.**')
                    break
                elif event == ChatEvent.CHAT_WAITING:
                    await message.channel.send('**Looking for a partner...**')
        while True:
                event, argument = chat.get_event()
                if event == ChatEvent.GOT_MESSAGE:
                    reply = argument
                    await message.channel.send(f'``{reply}``')
                    answer = await client.wait_for('message', check=check)
                    if answer.content[3:] == "disconnect":
                        chat.disconnect()
                    else:
                        chat.send(answer.content[3:])
                elif event == ChatEvent.CHAT_ENDED:
                    await message.channel.send("**The chat has ended.**")
                    break

client.run('XXXXXXXXXXXXXXXXXXXXXXXXX')


