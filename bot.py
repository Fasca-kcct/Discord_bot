import discord
import datetime
import Weather
import os

TOKEN = os.environ['DISCORD_TOKEN'] # TOKENを貼り付け
# CHANNELID = 971737310393667594 # チャンネルIDを貼り付け

client = discord.Client()

@client.event
async def on_ready():
    print('起動しました')

@client.event
async def on_message(message):
    if not message.author.bot:
        # channel = client.get_channel(CHANNELID)
        time_command = '$time'
        date_command = '$date'
        weather_command = '$weather'
        weather_text = Weather.rs_text
        time = datetime.datetime.now()
        time_text = time.strftime('%H:%M:%S')
        date_text = time.strftime('%Y/%m/%d')
        if message.content == time_command:
            await message.channel.send(time_text)
            print(time_text)
        if message.content == date_command:
            await message.channel.send(date_text)
            print(date_text)
        if message.content == weather_command:
            await message.channel.send(weather_text)
            print(weather_text)




client.run(TOKEN)




