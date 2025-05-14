import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import sqlite3
from discord.ext import commands as cmd
import sqlalchemy as sa
import logging
#from sqlalchemy import 
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, Session
from datetime import date, timedelta, datetime
from discord.ext.commands import CommandInvokeError
import traceback
import typing





load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True
##intents.all = True

bot = commands.Bot(command_prefix='m',intents=intents, help_command=commands.MinimalHelpCommand())
#con=sqlite3.connect("MichaelBot.db")
engine = sa.create_engine("sqlite:///MichaelBot.db", echo=False)
#engine = sa.create_engine("sqlite:///:memory:", echo=True)
session = sessionmaker(bind=engine)
Base = declarative_base()
##connection = engine.connect()

metadata = sa.MetaData()


class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True) 
    date_joined:Mapped[datetime] = mapped_column()
    message_points:Mapped[int] = mapped_column()
    activity_points:Mapped[int] = mapped_column()
    contribution_points:Mapped[int] = mapped_column()
    bias_points:Mapped[int] = mapped_column()


    @classmethod
    def getbyid(cls,session,id) -> 'User':
        return session.get(cls,id)

Base.metadata.create_all(engine)


def user_exists_by_id(session:Session,id: int) -> bool:
    existing_user = session.get(User, id)
    return existing_user is not None

def append_message_points_by_id(session:Session,id: int):
    user_to_update = session.get(User, id)
    user_to_update.message_points = user_to_update.message_points+1

def update_activity_points_by_id(session,id):
    user_to_update = session.get(User,id)
    


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandInvokeError):
        traceback.print_exception(error.original)
        


@bot.event
async def on_ready():
    logger = logging.getLogger('discord')
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())
    print(F"Meowchael ready o7, {bot.user.name}")
    

@bot.listen('on_message')
async def autoappend(message:discord.Message):
    if message.author.bot :
        return
    if not (isinstance(message.author,discord.Member)):
        return

    with Session(engine) as session:
        if not(user_exists_by_id(session,message.author.id)):
            new_user = User(id=message.author.id, date_joined = message.author.joined_at, message_points=1, activity_points=0, contribution_points=0,bias_points=0)
            session.add(new_user)
        else :
            append_message_points_by_id(session,message.author.id)
        
        seniority = (date.today() - User.getbyid(session,message.author.id).date_joined.date()).days

        ##TODO ACTIVITY POINTS based on seniority & message points

        session.commit()
    


@bot.listen('on_message')
async def reactions(message:discord.Message):
    # if message.author.name == "mathieubibi":
    #     with Session(engine) as session:
    #         todisplay = "message points = "+str(session.get(User,message.author.id).message_points)
    #     await message.reply (todisplay)

    if message.author.name == "formingcake1247":
        await message.reply("get trolled <:trollface:1260219910928203879>")
    # if message.author.name == "mathieubibi":
    #     if (isinstance(message.author,discord.Member)):
    #         await message.reply("True True yes Member indeed mhhhh")
    #     else:
    #         await message.reply("fuck off")        
    # if message.author.name == "mathieubibi":
    #     await message.reply ("you stink")
    #     todisplay = "date joined = "+str(session.get(User,message.author.id).date_joined)
    #     await message.reply (todisplay)

    # if "!poop displaypoints" in message.content :
    #     with Session(engine) as session:
    #         todisplay = "date joined = "+str(session.get(User,message.author.id).date_joined)
    #     await message.reply (todisplay)
    

@bot.command(with_app_command=True)
async def displaypoints(context:cmd.Context,user:typing.Optional[discord.User]=None):
    if user is None :
        user = context.author
    ##print(user.id)
    with Session(engine) as session:
        the_user = session.get(User,user.id)
        usermention:str = "<@"+ str(user.id) +">"
        todisplay = usermention + "'s points :" + "\nmessage points = "+str(the_user.message_points) + "\nactivity points = " + str(the_user.activity_points) + "\ndate joined (DD/MM/YYYY) = " + str(the_user.date_joined.day) + "/" + str(the_user.date_joined.month) + "/" + str(the_user.date_joined.year)
    await context.reply(todisplay)

@bot.command(with_app_command=True)
async def ismember(context:cmd.Context,user:typing.Optional[discord.User]=None):
    if user is None :
        user = context.author
    if (isinstance(context.author,discord.Member)):
        await context.reply("True True yes Member indeed mhhhh")
    else:
        await context.reply("fuck off")

@bot.command(with_app_command=True)
async def forcemessagepoints(context:cmd.Context, message_value:int,user:discord.User):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :
    # await context.reply("test")

    # await context.reply(message_value)

    usermention:str = "<@"+ str(user.id) +">"
    await context.reply(usermention)

    if(context.author.guild_permissions.administrator):
        usermention:str = "<@"+ str(user.id) +">"
        await context.reply(usermention)
        with Session(engine) as session:
            
            the_guy = session.get(User,user.id)
            the_guy.message_points= message_value            
            the_guys_message_points:int= the_guy.message_points ##to display later outside of the session
            session.commit()
            usermention:str = "<@"+ str(user.id) +">"
            await context.reply(usermention + " now has "+ the_guys_message_points +" activity points")
    else:
        await context.reply("fuck off, you're not a mod/admin, you're not elligible to use this command")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)