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
from datetime import date, timedelta, datetime, timezone#, relativedelta
from discord.ext.commands import CommandInvokeError
import traceback
import typing
import math
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import select
import re

def todayUTC():
    utc_aware_dt = datetime.now(timezone.utc)
    return utc_aware_dt.date()

def nowUTCnaive():
    timenow = datetime.now(timezone.utc)
    return timenow.replace(tzinfo=None)

def add_one_month(dt_object):
    return dt_object + relativedelta(months=1)

def add_three_months(dt_object):
    return dt_object + relativedelta(months=3)

def count_three_month_chunks(start_dt, end_dt):
    diff = relativedelta(end_dt, start_dt)
    total_months = (diff.years * 12) + diff.months
    return total_months // 3

def count_one_month_chunks(start_dt, end_dt):
    diff = relativedelta(end_dt, start_dt)
    total_months = (diff.years * 12) + diff.months
    return total_months // 1

def strcommas(number):
    return f"{number:,}"

def str_time_yyyymmdd(thedate:datetime):
    return f"{thedate:%Y/%m/%d}"

def is_yyyymmdd(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y/%m/%d")
        return True
    except:
        return False
    
def getepoch():
    return datetime.datetime(1970, 1, 1, 0, 0, 0)
    
def timestamp_from_datetime(thedatetime:datetime):
    return f"<t:{int(thedatetime.timestamp())}:R>"

def is_roles_list(input_string: str) -> bool:
    pattern = r"^<@&\d+>(\s*<@&\d+>)*$"
    return bool(re.match(pattern, input_string.strip()))

def parse_thresholds_str_to_intlist(input_string: str) -> list[int]:
    return [int(item.strip()) for item in input_string.split(',') if item.strip()]

def parse_str_True_False(input_string: str) -> str:
    true_pattern = r"Yes|True|Y|Ok"
    false_pattern = r"No|N|False"
    
    text = re.sub(true_pattern, "True", input_string, flags=re.IGNORECASE)
    text = re.sub(false_pattern, "False", text, flags=re.IGNORECASE)
    
    return text

def is_True_False_string(input_string: str) -> bool:
    pattern = r"^((True|False)(,(True|False))*)?$"
    return bool(re.match(pattern, input_string.strip()))

def parsed_str_True_False_to_Bool_list(input_str: str) -> list[bool]:
    return [item.strip() == "True" for item in input_str.split(",")]


def is_second_element_only(bool_list: list[bool]) -> bool:
    if len(bool_list) < 3: #Ensures the list has at least 3 elements
        return False
    if not bool_list[1]:
        return False
    others_are_false = all(not val for i, val in enumerate(bool_list) if i != 1)
    return others_are_false
