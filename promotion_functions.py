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
#from bot_events_listen import *
from alchemy_tables import *


def initialize_NotifTrack_for_Nekotopia_byid(session:Session,the_user_id:int):
    kitten_object=session.get(NotifTrack,(the_user_id,KITTENROLE))
    if (kitten_object==None):
        kitten=NotifTrack(user_id=the_user_id,role_id=KITTENROLE,status=False)
        session.add(kitten)
    else:
        kitten_object.status=False
    
    lolcat_object=session.get(NotifTrack,(the_user_id,LOLCATROLE))
    if (lolcat_object==None):
        lolcat=NotifTrack(user_id=the_user_id,role_id=LOLCATROLE,status=False)
        session.add(lolcat)
    else:
        lolcat_object.status=False

    technocat_object=session.get(NotifTrack,(the_user_id,TECHNOCATROLE))
    if (technocat_object==None):
        technocat=NotifTrack(user_id=the_user_id,role_id=TECHNOCATROLE,status=False)
        session.add(technocat)
    else:
        technocat_object.status=False
    
    bongocat_object=session.get(NotifTrack,(the_user_id,BONGOCATROLE))
    if (bongocat_object==None):
        bongocat=NotifTrack(user_id=the_user_id,role_id=BONGOCATROLE,status=False)
        session.add(bongocat)
    else:
        bongocat_object.status=False
    
    yappercat_object=session.get(NotifTrack,(the_user_id,YAPPERCATROLE))
    if (yappercat_object==None):
        yappercat=NotifTrack(user_id=the_user_id,role_id=YAPPERCATROLE,status=False)
        session.add(yappercat)
    else:
        yappercat_object.status=False

    ancientcat_object=session.get(NotifTrack,(the_user_id,ANCIENTCATROLE))
    if (ancientcat_object==None):
        ancientcat=NotifTrack(user_id=the_user_id,role_id=ANCIENTCATROLE,status=False)
        session.add(ancientcat)
    else:
        ancientcat_object.status=False

def update_NotifTrack_for_Nekotopia(session:Session,the_user:discord.Member):
    if (notiftrackexistsbyid(session,the_user.id)==False):
        initialize_NotifTrack_for_Nekotopia_byid(session,the_user.id)
    if has_role_byid(the_user,ANCIENTCATROLE) :
        session.get(NotifTrack,(the_user.id,ANCIENTCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,YAPPERCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,BONGOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,TECHNOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,LOLCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True
    elif has_role_byid(the_user,YAPPERCATROLE) :
        session.get(NotifTrack,(the_user.id,YAPPERCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,BONGOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,TECHNOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,LOLCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True
    elif has_role_byid(the_user,BONGOCATROLE) :
        session.get(NotifTrack,(the_user.id,BONGOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,TECHNOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,LOLCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True
    elif has_role_byid(the_user,TECHNOCATROLE) :
        session.get(NotifTrack,(the_user.id,TECHNOCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,LOLCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True
    elif has_role_byid(the_user,LOLCATROLE) :
        session.get(NotifTrack,(the_user.id,LOLCATROLE)).status=True
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True
    elif has_role_byid(the_user,KITTENROLE) :
        session.get(NotifTrack,(the_user.id,KITTENROLE)).status=True

def notiftrackexistsbyid(session:Session,userid:int):
    return ( 
        
        ((session.get(NotifTrack,(userid,ANCIENTCATROLE)))!=None) 
        
        and ((session.get(NotifTrack,(userid,YAPPERCATROLE)))!=None) 
        
        and ((session.get(NotifTrack,(userid,BONGOCATROLE)))!=None) 
        
        and ((session.get(NotifTrack,(userid,TECHNOCATROLE)))!=None) 
        
        and ((session.get(NotifTrack,(userid,LOLCATROLE)))!=None) 
        
        and ((session.get(NotifTrack,(userid,KITTENROLE)))!=None)
    
    )

def user_exists_by_id(session:Session,id: int) -> bool:
    existing_user = session.get(User, id)
    return existing_user is not None

def append_message_points_by_id_and_lengthaward(session:Session,id: int, lengthaward:int):
    
    user_to_update = session.get(User, id)
    user_to_update.message_points = user_to_update.message_points+lengthaward
    

def update_scores_by_id(session:Session,id:int):
    user_to_update = session.get(User,id)
    seniority = (todayUTC() - user_to_update.date_joined.date()).days
    x:int=seniority+1
    y:float

    ##THE CONTROVERSIAL FORMULA
    y=0.812154+0.488915*math.log(x) ##THE CONTROVERSIAL FORMULA
    ##THE CONTROVERSIAL FORMULA

    seniority_multiplier:float = y
    new_activity_score = int((user_to_update.message_points+user_to_update.voice_points+user_to_update.participation_points) * seniority_multiplier)
    user_to_update.activity_score = new_activity_score
    new_contribution_score = int(user_to_update.contribution_points * seniority_multiplier)
    user_to_update.contribution_score = new_contribution_score

def get_total_points_by_id(session,id):
    usertocheck = session.get(User,id)
    return usertocheck.activity_score+usertocheck.contribution_score+usertocheck.bias_points

# def isroleinroles_byuserandroleid(user:discord.Member,roleid:int):
#     for i in user.roles :
#         if (i.id == roleid):
#             return True
#     return False

def has_role_byid(user:discord.Member,roleid:int):
    role = user.guild.get_role(roleid)
    if role in user.roles:
        return True
    return False


#region old rolecheck functions
def isMat(user:discord.Member):
    return has_role_byid(user,1048218891467374622)

def isAristoCat(user:discord.Member):
    return has_role_byid(user,455516450753478668)

def isNyanCat(user:discord.Member):
    return has_role_byid(user,455515867254489088)

def isKeyboardCat(user:discord.Member):
    return has_role_byid(user,455455855660367885)

def isAncientCat(user:discord.Member):
    return has_role_byid(user,1348061216148291624)

def isYapperCat(user:discord.Member):
    return has_role_byid(user,1336818058328801312)

def isBongocat(user:discord.Member):
    return has_role_byid(user,455515782705577985)

def isTechnocat(user:discord.Member):
    return has_role_byid(user,455515726019821588)

def isLolCat(user:discord.Member):
    return has_role_byid(user,455515673859194892)

def isKitten(user:discord.Member):
    return has_role_byid(user,455515632742694929)

def isGrumpyCat(user:discord.Member):
    return has_role_byid(user,455515592338702336)
    # role = user.guild.get_role(455515592338702336)
    # if role in user.roles:
    #     return True
    # return False
    ##return isroleinroles_byuserandroleid(user,455515592338702336)

#endregion


def isModOrHigher(user:discord.Member):
    return (has_role_byid(user,MATROLE) or has_role_byid(user,ARISTOCATROLE) or has_role_byid(user,NYANCATROLE) or has_role_byid(user,KEYBOARDCATROLE))


async def checkforpromotion(user:discord.Member,total:int,bot):
    with Session(engine) as session:
        if(notiftrackexistsbyid(session,user.id)==False):
            update_NotifTrack_for_Nekotopia(session,user)
        if(notiftrackexistsbyid(session,user.id)==False):
            update_NotifTrack_for_Nekotopia(session,user)
        channeltoping=bot.get_channel(PROMOTIONSMICHAELCHANNEL)
        pingmodsandadmins="<@&1373274471288541194>"
        if ((has_role_byid(user,ANCIENTCATROLE))==False)and(total>=332000)and((session.get(NotifTrack,(user.id,ANCIENTCATROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} deserves a promotion to <@&1348061216148291624>\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,ANCIENTCATROLE)).status=True

        elif ((has_role_byid(user,YAPPERCATROLE))==False)and(total>=50000)and((session.get(NotifTrack,(user.id,YAPPERCATROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} deserves a promotion to <@&1336818058328801312>\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,YAPPERCATROLE)).status=True

        elif ((has_role_byid(user,BONGOCATROLE))==False)and(total>=11000)and((session.get(NotifTrack,(user.id,BONGOCATROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} deserves a promotion to <@&455515782705577985>\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,BONGOCATROLE)).status=True

        elif ((has_role_byid(user,TECHNOCATROLE))==False)and(total>=2050)and((session.get(NotifTrack,(user.id,TECHNOCATROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} deserves a promotion to <@&455515726019821588>\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,TECHNOCATROLE)).status=True

        elif ((has_role_byid(user,LOLCATROLE))==False)and(total>=170)and((session.get(NotifTrack,(user.id,LOLCATROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} deserves a promotion to <@&455515673859194892>\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,LOLCATROLE)).status=True

        elif (has_role_byid(user,GRUMPYCATROLE))and(total>=0)and((session.get(NotifTrack,(user.id,KITTENROLE)).status==False)):
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} climbed from the depths and deserves to be <@&455515632742694929> again.\nIf you agree, dfdon't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,KITTENROLE)).status=True
            
        session.commit()
