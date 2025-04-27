import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import sqlite3
from discord.ext import commands as cmd

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True
##intents.all = True

bot = commands.Bot(command_prefix='!poop',intents=intents, help_command=commands.MinimalHelpCommand())
con=sqlite3.connect("MichaelBot.db")


@bot.event
async def on_ready():
    print(F"Meowchael ready o7, {bot.user.name}")

##@bot.event
async def on_message(message:discord.Message):

    ##if message.author.name in ["mathieubibi","tamercal"]:
    if "men" in message.content.lower():
        await message.reply("caca poop shit sheise")

    ## message.author.id
    cur = con.cursor()
    res = cur.execute("""
                      INSERT INTO USER_POINTS 
                      (userid, message_points) 
                      VALUES(?,1)
                      ON CONFLICT UPDATE SET message_points = message_points + 1
                      """,(message.author.id,))

@bot.command(with_app_command=True)
async def display_points(context:cmd.Context,user:discord.User):
  
    cur = con.cursor()
    res = cur.execute("""
                        SELECT 
                        (message_points, activity_points, contribution_points, bias_points) 
                        FROM USER_POINTS
                        WHERE user_id = ?                      
                        """,(user.id,))
    toto=(res.fetchone()[0])
    await context.reply(toto)
  



bot.run(token, log_handler=handler, log_level=logging.DEBUG)