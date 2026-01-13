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
from common_functions import *
from alchemy_tables import *


def user_strikes_exists_by_id(session:Session,id: int) -> bool:
    existing_user = session.get(Strikes, id)
    return existing_user is not None


async def check_for_strike_clean (user:discord.Member,session:Session):
    db_strikes_user = session.get(Strikes,user.id)
    if not user_strikes_exists_by_id(session,user.id):
        return 0
    else :
        if (nowUTCnaive() > db_strikes_user.time_until_next_clean):
            time_chuncks = count_one_month_chunks(db_strikes_user.time_until_next_clean,nowUTCnaive())
            strikes_to_clean = (time_chuncks+1)
            for i in range(strikes_to_clean) :
                clean_strike()
        else :
            return 0
            

def move_strikes_notes(db_strikes_user:Strikes,session:Session):
    temp = db_strikes_user.active_strikes_notes.split(STR_SEPARATOR,1)
    if (db_strikes_user.dead_strikes_notes=="") :
        db_strikes_user.dead_strikes_notes=temp[0]
        if (len(temp)>0):
            db_strikes_user.active_strikes_notes=temp[1]
        else :
            db_strikes_user.active_strikes_notes=""
    else :
        db_strikes_user.dead_strikes_notes=db_strikes_user.dead_strikes_notes+STR_SEPARATOR+temp[0]
        if (len(temp)>0):
            db_strikes_user.active_strikes_notes=temp[1]
        else :
            db_strikes_user.active_strikes_notes=""


def clean_strike (db_strikes_user:Strikes,session:Session):
    move_strikes_notes(db_strikes_user, session)
    if (db_strikes_user.active_strikes>1):
        db_strikes_user.time_until_next_clean=add_one_month(db_strikes_user.time_until_next_clean)
    else :
        db_strikes_user.time_until_next_clean=getepoch()
    db_strikes_user.active_strikes=db_strikes_user.active_strikes-1
    db_strikes_user.dead_strikes=db_strikes_user.dead_strikes+1

async def display_strikes(user:discord.Member,db_strikes_user:Strikes,session:Session,context:cmd.Context):

    temp_dead = db_strikes_user.dead_strikes_notes.split(STR_SEPARATOR)
    deadnotes = ""
    for i in range (len(temp_dead)):
        deadnotes = deadnotes + temp_dead[i] + "\n"
    
    temp_active = db_strikes_user.active_strikes_notes.split(STR_SEPARATOR)
    activenotes = ""
    for i in range (len(temp_active)):
        activenotes = activenotes + temp_active[i] + "\n"
    
    timestamp=timestamp_from_datetime(db_strikes_user.time_until_next_clean)

    
    await context.reply(f"## {user.mention}'s Strikes❌ breakdown :\nCurrent Strikes :{db_strikes_user.active_strikes}\n## Notes on Current Strikes :\n{activenotes}## Time until next strike cleared :{timestamp}\nPrevious Strikes :{db_strikes_user.dead_strikes}\n## Notes on Previous Strikes :\n{deadnotes}")


    
            