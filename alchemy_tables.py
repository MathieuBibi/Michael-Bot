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
    message_points:Mapped[int] = mapped_column(default=0)
    voice_points:Mapped[int] = mapped_column(default=0)
    participation_points:Mapped[int] = mapped_column(default=0)
    activity_score:Mapped[int] = mapped_column(default=0)
    contribution_points:Mapped[int] = mapped_column(default=0)
    contribution_notes:Mapped[str] = mapped_column(default = "")
    contribution_score:Mapped[int] = mapped_column(default=0)
    bias_points:Mapped[int] = mapped_column(default=0)
    penalty_score:Mapped[int] = mapped_column(default=0)

    notified_for_promotions_each_roles:Mapped[List["NotifTrack"]] = relationship(
        back_populates="user",cascade="all,delete-orphan"
    )
    # strikes_info: Mapped["Strikes"] = relationship(back_populates="user",cascade="all,delete-orphan")



    @classmethod
    def getbyid(cls,session,id) -> 'User':
        return session.get(cls,id)
    
# class ScanTrack(Base):
#     __tablename__ = 'scantrack'
#     guild:Mapped[int] = mapped_column(primary_key=True) 
#     currently_scanning:Mapped[bool] = mapped_column(default=False)
#     channel_scanning:Mapped[int] = mapped_column(default=0)
    


#     @classmethod
#     def getbyid(cls,session,id) -> 'ScanTrack':
#         return session.get(cls,id)

class NotifTrack(Base):
    __tablename__ = 'notiftrack'
    user_id:Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)
    role_id:Mapped[int] = mapped_column(primary_key=True)
    status:Mapped[bool] = mapped_column(default=False)
    user:Mapped["User"] = relationship(back_populates="notified_for_promotions_each_roles")

    @classmethod
    def getbyids_user_roles(cls,session,user_id,role_id) -> 'NotifTrack':
        smt = session.get(NotifTrack,(user_id,role_id))
        return smt
    
# class Strikes(Base):
#     __tablename__ = 'strikes'
#     user_id:Mapped[int] = mapped_column(ForeignKey("users.id"),primary_key=True)
#     #key:Mapped[int] = mapped_column()
#     time_until_next_clean:Mapped[datetime] = mapped_column(default=getepoch())
#     active_strikes:Mapped[int] = mapped_column(default=0)
#     dead_strikes:Mapped[int] = mapped_column(default=0)
#     active_strikes_notes:Mapped[str] = mapped_column(default = "") # will be parsed with a separator
#     dead_strikes_notes:Mapped[str] = mapped_column(default = "") # will be parsed with a separator
#     user:Mapped["User"] = relationship(back_populates="strikes_info")



    




Base.metadata.create_all(engine)