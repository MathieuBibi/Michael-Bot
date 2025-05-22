##NEKOTOPIA ROLES AND CHANNELS IDs
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
from datetime import date, timedelta, datetime
from discord.ext.commands import CommandInvokeError
import traceback
import typing
import math
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import select





load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding='utf-8',mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True
##intents.all = True

class MichaelBot(commands.Bot):
    async def setup_hook(self):
        MY_GUILD = discord.Object(id=455428492171935757)
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)
        ##await self.tree.sync()


bot = MichaelBot(command_prefix='m!',intents=intents, help_command=None)




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
    activity_points:Mapped[int] = mapped_column(default=0)
    contribution_points:Mapped[int] = mapped_column(default=0)
    bias_points:Mapped[int] = mapped_column(default=0)

    notified_for_promotions_each_roles:Mapped[List["NotifTrack"]] = relationship(
        back_populates="user",cascade="all,delete-orphan"
    )


    @classmethod
    def getbyid(cls,session,id) -> 'User':
        return session.get(cls,id)

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

Base.metadata.create_all(engine)



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



def strcommas(number):
    number_str = str(number)
    if number < 0:
        sign = "-"
        number_str = number_str[1:]
    else:
        sign = ""

    n = len(number_str)
    if n <= 3:
        return sign + number_str
    else:
        parts = []
        for i in range(n - 1, -1, -3):
            parts.append(number_str[max(0, i - 2):i + 1])
        return sign + ','.join(reversed(parts))

def user_exists_by_id(session:Session,id: int) -> bool:
    existing_user = session.get(User, id)
    return existing_user is not None

def append_message_points_by_id_and_lengthaward(session:Session,id: int, lengthaward:int):
    
    user_to_update = session.get(User, id)
    user_to_update.message_points = user_to_update.message_points+lengthaward
    

def update_activity_points_by_id(session,id):
    user_to_update = session.get(User,id)
    seniority = (date.today() - user_to_update.date_joined.date()).days
    x:int=seniority+1
    y:float

    ##THE CONTROVERSIAL FORMULA
    y=0.812154+0.488915*math.log(x) ##THE CONTROVERSIAL FORMULA
    ##THE CONTROVERSIAL FORMULA

    seniority_multiplier:float = y
    new_activity_points = int(user_to_update.message_points * seniority_multiplier)
    user_to_update.activity_points = new_activity_points

def get_total_points_by_id(session,id):
    usertocheck = session.get(User,id)
    return usertocheck.activity_points+usertocheck.contribution_points+usertocheck.bias_points

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
    return (isMat(user) or isAristoCat(user) or isNyanCat(User) or isKeyboardCat(User))

async def checkforpromotion(the_guy:discord.Member,total):
    with Session(engine) as session:
        
        update_NotifTrack_for_Nekotopia(session,the_guy)
        channeltoping=bot.get_channel(MICHAELCHANNEL)
        usermention:str = "<@"+ str(the_guy.id) +">"
        pingmodsandadmins="<@&1373274471288541194>"
        if ((has_role_byid(the_guy,ANCIENTCATROLE))==False)and(total>=332000)and((session.get(NotifTrack,(the_guy.id,ANCIENTCATROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" deserves a promotion to <@&1348061216148291624>" )
            session.get(NotifTrack,(the_guy.id,ANCIENTCATROLE)).status=True

        elif ((has_role_byid(the_guy,YAPPERCATROLE))==False)and(total>=50000)and((session.get(NotifTrack,(the_guy.id,YAPPERCATROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" deserves a promotion to <@&1336818058328801312>" )
            session.get(NotifTrack,(the_guy.id,YAPPERCATROLE)).status=True

        elif ((has_role_byid(the_guy,BONGOCATROLE))==False)and(total>=11000)and((session.get(NotifTrack,(the_guy.id,BONGOCATROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" deserves a promotion to <@&455515782705577985>" )
            session.get(NotifTrack,(the_guy.id,BONGOCATROLE)).status=True

        elif ((has_role_byid(the_guy,TECHNOCATROLE))==False)and(total>=2050)and((session.get(NotifTrack,(the_guy.id,TECHNOCATROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" deserves a promotion to <@&455515726019821588>" )
            session.get(NotifTrack,(the_guy.id,TECHNOCATROLE)).status=True

        elif ((has_role_byid(the_guy,LOLCATROLE))==False)and(total>=170)and((session.get(NotifTrack,(the_guy.id,LOLCATROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" deserves a promotion to <@&455515673859194892>" )
            session.get(NotifTrack,(the_guy.id,LOLCATROLE)).status=True

        elif (has_role_byid(the_guy,GRUMPYCATROLE))and(total>=170)and((session.get(NotifTrack,(the_guy.id,KITTENROLE)).status==False)):
            await channeltoping.send(pingmodsandadmins+" I think "+usermention+" climbed from the depths and deserves to be <@&455515632742694929> again")
            session.get(NotifTrack,(the_guy.id,KITTENROLE)).status=True
            
        session.commit()


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
    length = len(message.content)
    lengthaward=max(1,int(math.floor(length/150)))
    with Session(engine) as session:
        
        if not(user_exists_by_id(session,message.author.id)):
            new_user = User(id=message.author.id, date_joined = message.author.joined_at, message_points=lengthaward, activity_points=0, contribution_points=0,bias_points=0)## ,notified_admins=False (last arg)
            session.add(new_user)
        else :
            append_message_points_by_id_and_lengthaward(session,message.author.id,lengthaward)
              
        update_activity_points_by_id(session,message.author.id)

        session.commit()
    
@bot.listen('on_message')
async def promotion_checks(message:discord.Message):
    if message.author.bot :
        return
    if not (isinstance(message.author,discord.Member)):
        return
    with Session(engine) as session:
        author = session.get(User,message.author.id)
        total=get_total_points_by_id(session,author.id)
    await checkforpromotion(message.author,total)
        
        
    
        

    

# @bot.listen('on_message')
# async def reactions(message:discord.Message):
#     pass

    # if message.author.name == "mathieubibi":
    #     with Session(engine) as session:
    #         todisplay = "message points = "+str(session.get(User,message.author.id).message_points)
    #     await message.reply (todisplay)

    # if message.author.name == "formingcake1247":
    #     await message.reply("get trolled <:trollface:1260219910928203879>")
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
    

@bot.hybrid_command(with_app_command=True)
async def displaypts(context:cmd.Context,user:typing.Optional[discord.User]=None):
    if user is None :
        user = context.author
    ##print(user.id)
    with Session(engine) as session:
        the_user = session.get(User,user.id)
        update_activity_points_by_id(session,the_user.id)
        usermention:str = "<@"+ str(user.id) +">"
        useractiv = the_user.activity_points
        usercontrib = the_user.contribution_points
        userbias = the_user.bias_points
        todisplay = "> " + usermention + "'s points :" + "\n> activity points = " + strcommas(useractiv)
        if(usercontrib!=0):
            todisplay=todisplay+ "\n> contribution points = " + strcommas(usercontrib)
        if(userbias!=0):
            todisplay=todisplay+ "\n> bias <:trollface:1260219910928203879> points = " +strcommas(userbias)
        usertotal = useractiv+usercontrib+userbias
        todisplay= todisplay + "\n> ## TOTAL POINTS = " + strcommas(usertotal)
        session.commit()
    await context.reply(todisplay)

@bot.hybrid_command(with_app_command=True)
async def displayptsv(context:cmd.Context,user:typing.Optional[discord.User]=None):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :    
    ##if(context.author.guild_permissions.administrator):
    if (isModOrHigher(context.author)):
        if user is None :
            user = context.author
        ##print(user.id)
        with Session(engine) as session:
            the_user = session.get(User,user.id)
            update_activity_points_by_id(session,the_user.id)
            seniority = (date.today() - the_user.date_joined.date()).days
            x:int=seniority+1
            y:float

            ##THE CONTROVERSIAL FORMULA
            y=0.812154+0.488915*math.log(x) ##THE CONTROVERSIAL FORMULA
            ##THE CONTROVERSIAL FORMULA

            usermention:str = "<@"+ str(user.id) +">"
            usermess = the_user.message_points
            usercontrib = the_user.contribution_points
            datetodisplay:str = str(the_user.date_joined.year) + "/" + str(the_user.date_joined.month) + "/" + str(the_user.date_joined.day)
            seniority_multiplier:float = y
            ##notified:bool=False##the_user.notified_admins
            useractiv = the_user.activity_points
            userbias = the_user.bias_points
            usertotal = useractiv+usercontrib+userbias            
            todisplay = "> " + usermention + "'s points :" + "\n> message points = "+ strcommas(usermess)+ "\n> date joined (YYYY/MM/DD) = " + datetodisplay + "\n> seniority_multiplier = x" + str(math.ceil(seniority_multiplier*1000)/1000)  + "\n> activity points = " + strcommas(useractiv) + "\n> contribution points = " + strcommas(usercontrib) + "\n> bias <:trollface:1260219910928203879> points = " + strcommas(userbias) + "\n> ## TOTAL POINTS = " + strcommas(usertotal) ## "\n> notified admins = " + str(notified) + (at some points)
            session.commit()
        await context.reply(todisplay)
    else:
        await context.reply("fuck off, low rank")

@bot.hybrid_command(with_app_command=True)
async def help(context:cmd.context):
    await context.reply("## List of Michael commands :\ndisplaypts\n> displays the points of a user :)\ndisplayptsv\n> verbose version of /displaypts, avaliable for moderators and up\n> it also shows more in-depth data, stats for in-between calculation steps\nnawardcontrib\n> allows an admin to award someone with contribution points to reward them\n> (for hosting giveaways, helping people, contributing to dojo decorations, writing guides etc...)\nforcemsgpts\n> allows an admin to edit a user's message points ammount\n> (used to repair false message point count)\nawardmsg\n> allows an admin to give someone exra message points \n> (for exemple, to reward someone for VC activity (recomended 1min = 1point approximately))\nawardbias\n> allows admins to award biassed points to users for no reason through the power of admin abuse <:trollface:1260219910928203879>\n The Bot is still in early developpement/prototype form, many more features and commands coming soon !")

@bot.hybrid_command(with_app_command=True)
async def forcemsgpts(context:cmd.Context, message_value:int,user:discord.User):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :
    if(context.author.guild_permissions.administrator):
        usermention:str = "<@"+ str(user.id) +">"
        the_guys_message_points:int
        with Session(engine) as session:
            
            the_guy = session.get(User,user.id)
            the_guy.message_points= message_value            
            the_guys_message_points= the_guy.message_points ##to display later outside of the session
            session.commit()
            await context.reply(usermention + " now has "+ strcommas(the_guys_message_points) +' message points \n-# (keep in mind, "message points" are just a middle calculation step and NOT the same as activity points !)')
    else:
        await context.reply("fuck off, you're not a mod/admin, you're not elligible to use this command")

@bot.hybrid_command(with_app_command=True)
async def awardmsg(context:cmd.Context, award_value:int,user:discord.User):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :
    if(context.author.guild_permissions.administrator):
        usermention:str = "<@"+ str(user.id) +">"
        the_guys_message_points:int
        with Session(engine) as session:
            
            the_guy = session.get(User,user.id)
            the_guy.message_points= the_guy.message_points + award_value     
            the_guys_message_points= the_guy.message_points ##to display later outside of the session
            session.commit()
            await context.reply(usermention + " now has "+ strcommas(the_guys_message_points) +' message points\n-# (keep in mind, "message points" are just a middle calculation step and NOT the same as activity points !)')
    else:
        await context.reply("fuck off, you're not a mod/admin, you're not elligible to use this command")

@bot.hybrid_command(with_app_command=True)
async def awardcontrib(context:cmd.Context, award_value:int,user:discord.User):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :
    if(context.author.guild_permissions.administrator):
        usermention:str = "<@"+ str(user.id) +">"
        the_guys_contrib_points:int
        with Session(engine) as session:
            
            the_guy = session.get(User,user.id)
            the_guy.contribution_points = the_guy.contribution_points + award_value            
            the_guys_contrib_points= the_guy.contribution_points ##to display later outside of the session
            session.commit()
            await context.reply(usermention + " now has "+ strcommas(the_guys_contrib_points) +" contribution points")
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command")


@bot.hybrid_command(with_app_command=True)
async def awardbias(context:cmd.Context, award_value:int,user:discord.User):
    ##if ((1048218891467374622 in context.author.roles) or (455516450753478668 in context.author.roles) or (455515867254489088 in context.author.roles) or (455455855660367885 in context.author.roles)) :
    if(context.author.guild_permissions.administrator):
        usermention:str = "<@"+ str(user.id) +">"
        the_guys_bias_points:int
        with Session(engine) as session:
            
            the_guy = session.get(User,user.id)
            the_guy.bias_points = the_guy.bias_points + award_value            
            the_guys_bias_points= the_guy.bias_points ##to display later outside of the session
            session.commit()
        await context.reply("Through the power of admin abuse <:trollface:1260219910928203879> " + usermention + " now has "+ strcommas(the_guys_bias_points) +" bias points")
    else:
        await context.reply("fuck off, low rank, no admin abuse for you <:trollface:1260219910928203879>")

    
    

bot.run(token, log_handler=handler, log_level=logging.DEBUG)