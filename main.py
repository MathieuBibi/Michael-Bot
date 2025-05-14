import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import sqlite3
from discord.ext import commands as cmd
import sqlalchemy as sa
from sqlalchemy import Mapped, mapped_column, sessionmaker, declarative_base
from datetime import date


def today_date() -> str:
    today = date.today()
    return today.strftime("%Y-%m-%d")

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True
##intents.all = True

bot = commands.Bot(command_prefix='!poop',intents=intents, help_command=commands.MinimalHelpCommand())
con=sqlite3.connect("MichaelBot.db")


engine = sa.create_engine("sqlite:///:memory:")
session = sessionmaker(bind=db)
Base = declarative_base()
##connection = engine.connect()

metadata = sa.MetaData()


class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True) 
    date_joined:Mapped[str] = mapped_column()
    message_points:Mapped[int] = mapped_column()
    contribution_points:Mapped[int] = mapped_column()
    bias_points:Mapped[int] = mapped_column()

    # @classmethod
    # def get_user_by_id(cls,id):
    # return session.get(cls, id)


def user_exists_by_id(id: int) -> bool:
    existing_user = session.get(User, id)
    return existing_user is not None

def append_message_points_by_id(id: int):
    user_to_update = session.get(User, id)
    user_to_update.message_points = user_to_update.message_points+1


@bot.event
async def on_ready():
    print(F"Meowchael ready o7, {bot.user.name}")

##@bot.event
async def on_message(message:discord.Message):

    if (user_exists_by_id(message.author.id)):
        new_user = User(id=message.author.id, date_joined = today_date(), message_points=1,contribution_points=0,bias_points=0)
    else :
        append_message_points_by_id(message.author.id)

    todisplay = "message points = "+str(session.get(User,id).message_points)

    if (message.author.name == "mathieubibi"):
        await message.reply (todisplay)
       
        

    ##OLD SQLite
    
    # ##if message.author.name in ["mathieubibi","tamercal"]:
    # if "men" in message.content.lower():
    #     await message.reply("caca poop shit sheise")

    # ## message.author.id
    # cur = con.cursor()
    # res = cur.execute("""
    #                   INSERT INTO USER_POINTS 
    #                   (user_id, message_points, date_joined) 
    #                   VALUES(?,1,?)
    #                   ON CONFLICT UPDATE SET message_points = message_points + 1
    #                   """,(message.author.id,message.author.joined_at))

# @bot.command(with_app_command=True)
# async def display_points(context:cmd.Context,user:discord.User):
  
#     cur = con.cursor()
#     res = cur.execute("""
#                         SELECT 
#                         (message_points, activity_points, contribution_points, bias_points) 
#                         FROM USER_POINTS
#                         WHERE user_id = ?                      
#                         """,(user.id,))
#     toto=(res.fetchone()[0])
#     await context.reply(toto)
  



bot.run(token, log_handler=handler, log_level=logging.DEBUG)