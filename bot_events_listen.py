##NEKOTOPIA ROLES AND CHANNELS IDssqlite3
MATROLE:int=1048218891467374622
ARISTOCATROLE:int=455516450753478668
NYANCATROLE:int=455515867254489088
KEYBOARDCATROLE:int=455455855660367885
ANCIENTCATROLE:int=1348061216148291624
YAPPERCATROLE:int=1336818058328801312
BONGOCATROLE:int=455515782705577985
TECHNOCATROLE:int=455515726019821588
LOLCATROLE:int=455515673859194892
KITTENROLE:int=455515632742694929
GRUMPYCATROLE:int=455515592338702336
ADMINCHANNEL=1018088445551325194
MICHAELCHANNEL=1373432540869955584
PROMOTIONSMICHAELCHANNEL = 1374014674336612463
STR_SEPARATOR:str = ";;;|||\n"

import discord
from discord import app_commands, Object
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import sqlite3
from discord.ext import commands as cmd
import sqlalchemy as sa
import logging
#from sqlalchemy import 
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, Session, DeclarativeBase, relationship
from datetime import date, timedelta, datetime, timezone
from discord.ext.commands import CommandInvokeError
import traceback
import typing
import math
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import select

from michael_utils import *
from alchemy_tables import *

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, CommandInvokeError):
#         traceback.print_exception(error.original)
        


# @bot.event
# async def on_ready():
#     logger = logging.getLogger('discord')
#     logger.setLevel(logging.INFO)
#     logger.addHandler(logging.StreamHandler())
#     print(F"Meowchael ready o7, {bot.user.name}")
#     channel=bot.get_channel(MICHAELCHANNEL)
#     await channel.send("Meowchael ready o7")
    

# @bot.listen('on_message')
# async def autoappend(message:discord.Message):
#     if message.author.bot :
#         return
#     if not (isinstance(message.author,discord.Member)):
#         return
#     length = len(message.content)
#     lengthaward=max(1,int(math.floor(length/150)))
#     with Session(engine) as session:
        
#         if not(user_exists_by_id(session,message.author.id)):
#             new_user = User(id=message.author.id, date_joined = message.author.joined_at, message_points=lengthaward)
#             session.add(new_user)
#         else :
#             append_message_points_by_id_and_lengthaward(session,message.author.id,lengthaward)
              
#         update_scores_by_id(session,message.author.id)

#         session.commit()
    
# @bot.listen('on_message')
# async def promotion_checks(message:discord.Message):
#     if message.author.bot :
#         return
#     if not (isinstance(message.author,discord.Member)):
#         return
#     with Session(engine) as session:
#         if ((session.get(User,message.author.id))!=None):
#             total=get_total_points_by_id(session,message.author.id)
#             await checkforpromotion(message.author,total)
        
        
    
        
# # @bot.listen('on_message')
# # async def reactions(message:discord.Message):
# #     pass

#     # if message.author.name == "mathieubibi":
#     #     with Session(engine) as session:
#     #         todisplay = "message points = "+str(session.get(User,message.author.id).message_points)
#     #     await message.reply (todisplay)

#     # if message.author.name == "formingcake1247":
#     #     await message.reply("get trolled <:trollface:1260219910928203879>")
#     # if message.author.name == "mathieubibi":
#     #     if (isinstance(message.author,discord.Member)):
#     #         await message.reply("True True yes Member indeed mhhhh")
#     #     else:
#     #         await message.reply("fuck off")        
#     # if message.author.name == "mathieubibi":
#     #     await message.reply ("you stink")
#     #     todisplay = "date joined = "+str(session.get(User,message.author.id).date_joined)
#     #     await message.reply (todisplay)

#     # if "!poop displaypoints" in message.content :
#     #     with Session(engine) as session:
#     #         todisplay = "date joined = "+str(session.get(User,message.author.id).date_joined)
#     #     await message.reply (todisplay)