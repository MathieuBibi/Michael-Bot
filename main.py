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
#from promotion_commands import *
from promotion_functions import *
# from common_functions import *
# from strikes_functions import *
from alchemy_tables import *



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
        ##
        #self.tree.copy_global_to(guild=MY_GUILD)
        ##
        await self.tree.sync(guild=MY_GUILD)
        await self.tree.sync()


bot = MichaelBot(command_prefix='m!',intents=intents, help_command=None)



########################################################
########################################################
########################################################
########################################################
# region events & listens


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
    channel=bot.get_channel(MICHAELCHANNEL)
    await channel.send("Meowchael ready o7")
    

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
            new_user = User(id=message.author.id, date_joined = message.author.joined_at, message_points=lengthaward)
            session.add(new_user)
        else :
            append_message_points_by_id_and_lengthaward(session,message.author.id,lengthaward)
              
        update_scores_by_id(session,message.author.id)

        session.commit()
    
@bot.listen('on_message')
async def promotion_checks(message:discord.Message):
    if message.author.bot :
        return
    if not (isinstance(message.author,discord.Member)):
        return
    with Session(engine) as session:
        if ((session.get(User,message.author.id))!=None):
            total=get_total_points_by_id(session,message.author.id)
            await checkforpromotion(message.author,total,bot)
        
        
    
        
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



# endregion
########################################################
########################################################
########################################################
########################################################
# region promotion commands

# @bot.hybrid_command(with_app_command=True)
# async def truetimejoined(context:cmd.Context,user:typing.Optional[discord.User]=None):
#     user.
    
@bot.hybrid_command(with_app_command=True)
async def resetnotiftrack(context:cmd.Context,user:typing.Optional[discord.Member]=None):
    if user is None :
        user = context.author
    ##print(user.id)
    with Session(engine) as session:
        ##initialize_NotifTrack_for_Nekotopia_byid(session,user.id)
        initialize_NotifTrack_for_Nekotopia_byid(session,user.id)
        update_NotifTrack_for_Nekotopia(session,user)
        session.commit()
    await context.reply(f"The notification tracker for promotions of {user.mention} has been reset.",silent=True)
    

# @bot.hybrid_command(with_app_command=True)
# async def showscore(context:cmd.Context,user:typing.Optional[discord.Member]=None,public:str="nah"):
#     isephemeral:bool=True
#     if(public in ["Yes","yes","True","true","public","Public","Y","y","ok","OK"]):
#         isephemeral=False
#     with Session(engine) as session:
#         db_user = session.get(User,user.id)
#         if db_user == None:
#             new_user = User(id=user.id, date_joined = user.joined_at, message_points=1)
#             session.add(new_user)
#             db_user = session.get(User,user.id)
#         update_scores_by_id(session,db_user.id)
#         useractivscore = db_user.activity_score
#         usercontribscore = db_user.contribution_score
#         userbias = db_user.bias_points
#         usertotal = useractivscore+usercontribscore+userbias
#         todisplay = f"> {user.mention}'s score breakdown :" f"\n> activity score = {useractivscore:,}"
#         if(usercontribscore!=0):
#             todisplay += f"\n> contribution score = {usercontribscore:,}"
#         if(userbias!=0):
#             todisplay += f"\n> bias <:trollface:1260219910928203879> score = {userbias:,}"
#         todisplay += f"\n> ## TOTAL SCORE = {usertotal:,}"
#         session.commit()
#     await context.reply(todisplay,silent=True,ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
async def showscore(context:cmd.Context,user:typing.Optional[discord.Member]=None,public:str="nah"):
    isephemeral:bool=True
    if(public in ["Yes","yes","True","true","public","Public","Y","y","ok","OK"]):
        isephemeral=False
    #if (isModOrHigher(context.author)):
    if user is None :
        user = context.author
    ##print(user.id)
    with Session(engine) as session:
        db_user = session.get(User,user.id)
        if db_user == None :
            new_user = User(id=user.id, date_joined = user.joined_at, message_points=1)
            session.add(new_user)
            db_user = session.get(User,user.id)
        update_scores_by_id(session,db_user.id)
        seniority = (date.today() - db_user.date_joined.date()).days
        x:int=seniority+1
        y:float

        ##THE CONTROVERSIAL FORMULA
        y=0.812154+0.488915*math.log(x) ##THE CONTROVERSIAL FORMULA
        ##THE CONTROVERSIAL FORMULA

        usernotes = db_user.contribution_notes
        seniority_multiplier:float = y
        useractivscore = db_user.activity_score
        usercontribscore = db_user.contribution_score
        userbias = db_user.bias_points         
        usertotal = useractivscore+usercontribscore+userbias
        todisplay:str = (
            f"> {user.mention}'s verbose score breakdown :"
            "\n> ## POINTS :"
            f"\n> message points = {db_user.message_points:,}"
            f"\n> voice points = {db_user.voice_points:,}"
            f"\n> participation points = {db_user.participation_points:,}"
            f"\n> contribution points = {db_user.contribution_points:,}")

        if(usernotes!=""):   
            todisplay += f"\n> list of contributions :{usernotes}"
        
        todisplay+= (
            f"\n> date joined (YYYY/MM/DD) = {db_user.date_joined:%Y/%m/%d}"
            f"\n> seniority_multiplier = x{seniority_multiplier:.3}"
            f"\n> ## SCORE :"
            f"\n> activity score = {useractivscore:,}"
            f"\n> contribution score = {usercontribscore:,}"
            f"\n> bias <:trollface:1260219910928203879> score = {userbias:,}"
            f"\n> ## TOTAL SCORE = {usertotal:,}"
        )
        session.commit()
    await context.reply(todisplay,silent=True,ephemeral=isephemeral)
    # else:
    #     await context.reply("fuck off, low rank",ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
async def help(context:cmd.context):
    await context.reply("## List of Michael commands :"
                        "\n## showscore\n> displays the score of a user :)"
                        "\n## showscorev\n> verbose version of /displayscore, avaliable for moderators and up"
                        "\n> it also shows more in-depth data, stats for in-between calculation steps"
                        "\n## awardcontrib\n> allows an admin to award someone with contribution points to reward them"
                        "\n> (for hosting giveaways, helping people, contributing to dojo decorations, writing guides etc...)"
                        "\n## forcemsgpts\n> debug tool that allows an admin to edit a user's message points ammount"
                        "\n> (used to repair false message count (Michael can already count messages automatically))"
                        "\n## awardmsg\n> debug tool that allows an admin to give someone exra message points"
                        "\n## awardvoice\n> allows admins to award someone with voice points\n> (to reward someone for VC activity (recomended 1min = 1point approximately))"
                        "\n## awardparticipation \n> allows admins to award someone with participation points\n> (to reward someone for participating in content with other members)"
                        "\n## awardbias\n> allows admins to award bias score to users for no reason through the power of admin abuse <:trollface:1260219910928203879>"
                        "\n## resetnotiftrack\n> debug tool that resets the tracker for promotion notifications for a specific user"
                        "\n\n The Bot is still in early developpement/prototype form, many more features and commands coming soon !",ephemeral=True)

@bot.hybrid_command(with_app_command=True)
async def forcemsgpts(context:cmd.Context,user:discord.Member, msg_value:int):
    if(context.author.guild_permissions.administrator):
        new_message_points:int
        with Session(engine) as session:
            
            db_user = session.get(User,user.id)
            db_user.message_points= msg_value            
            new_message_points= db_user.message_points ##to display later outside of the session
            update_scores_by_id(session,db_user.id)
            total = get_total_points_by_id(session,db_user.id)
            session.commit()
            await context.reply(f"{user.mention}'s message points have been repaired, they now have {new_message_points:,}"
                                '\n-# (keep in mind, "message points" are just a middle calculation step and NOT the same as activity score !)',silent=True,ephemeral=True)
            await checkforpromotion(user,total,bot)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command",ephemeral=True)


@bot.hybrid_command(with_app_command=True)
async def awardvoice(context:cmd.Context, user:discord.Member, award_value:int, hidden:str="nah"):
    isephemeral:bool=False
    if(hidden in ["Yes","yes","True","true","Hidden","hidden","Y","y","ok","OK"]):
        isephemeral=True
    if(context.author.guild_permissions.administrator):
        new_voice_points:int
        with Session(engine) as session:
            
            db_user = session.get(User,user.id)
            db_user.voice_points= db_user.voice_points + award_value     
            new_voice_points= db_user.voice_points ##to display later outside of the session
            update_scores_by_id(session,db_user.id)
            total = get_total_points_by_id(session,db_user.id)
            session.commit()
            await context.reply(f"{user.mention} have been granted {award_value:,} voice points and now has {new_voice_points:,}"
                                '\n-# (keep in mind, "voice points" are just a middle calculation step and NOT the same as activity score !)',silent=True,ephemeral=isephemeral)
            await checkforpromotion(user,total,bot)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command",ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
async def awardparticipation(context:cmd.Context, user:discord.Member, award_value:int,hidden:str="nah"):
    isephemeral:bool=False
    if(hidden in ["Yes","yes","True","true","Hidden","hidden","Y","y","ok","OK"]):
        isephemeral=True
    if(context.author.guild_permissions.administrator):
        new_participation_points:int
        with Session(engine) as session:
            
            db_user = session.get(User,user.id)
            db_user.participation_points= db_user.participation_points + award_value     
            new_participation_points= db_user.participation_points ##to display later outside of the session
            update_scores_by_id(session,db_user.id)
            total = get_total_points_by_id(session,db_user.id)
            session.commit()
            await context.reply(f"{user.mention} have been granted {award_value:,} participation points and now has {new_participation_points:,}"
                                '\n-# (keep in mind, "voice points" are just a middle calculation step and NOT the same as activity score !)',silent=True)
            await checkforpromotion(user,total,bot)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command",ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
#async def awardcontrib(context:cmd.Context, award_value:int,user:discord.User):
async def awardcontrib(context:cmd.Context, user:discord.Member, award_value:int,note:str=None,hidden:str="nah"):
    isephemeral:bool=False
    if(hidden in ["Yes","yes","True","true","Hidden","hidden","Y","y","ok","OK"]):
        isephemeral=True
    if(context.author.guild_permissions.administrator):
        new_contrib_points:int
        with Session(engine) as session:
            
            db_user = session.get(User,user.id)
            db_user.contribution_points = db_user.contribution_points + award_value
            if(note!=None):
                # if(db_user.contribution_notes!=""):
                db_user.contribution_notes += f"\n> {award_value:,} for : {note}"
                # else:
                #     db_user.contribution_notes= "\n> "+ strcommas(award_value) + " for : " + note
            new_contrib_points = db_user.contribution_points ##to display later outside of the session
            update_scores_by_id(session,db_user.id)
            total = get_total_points_by_id(session,db_user.id)
            session.commit()
            todisplay = f"{user.mention} have been granted {award_value:,} contribution points and now has {new_contrib_points:,}"
            if(note !=None):
                todisplay += f"\nas a reward for : {note}"
            todisplay += '\n-# (keep in mind, "contribution points" are just a middle calculation step and NOT the same as contribution score !)'
            await context.reply(todisplay,silent=True,ephemeral=isephemeral)
            await checkforpromotion(user,total,bot)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command",ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
async def nukecontribnotes(context:cmd.Context, user:discord.Member):
    if(context.author.guild_permissions.administrator):
        with Session(engine) as session:
            db_user = session.get(User,user.id)
            db_user.contribution_notes=""
            session.commit()
        await context.reply(f"successfully nuked the contribution notes of {user.mention}>",silent=True,ephemeral=True)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command",ephemeral=True)


@bot.hybrid_command(with_app_command=True)
async def awardbias(context:cmd.Context,user:discord.Member, award_value:int,hidden:str="nah"):
    isephemeral:bool=False
    if(hidden in ["Yes","yes","True","true","Hidden","hidden","Y","y","ok","OK"]):
        isephemeral=True
    if(context.author.guild_permissions.administrator):
        new_bias_points:int
        with Session(engine) as session:
            
            db_user = session.get(User,user.id)
            db_user.bias_points = db_user.bias_points + award_value            
            new_bias_points = db_user.bias_points ##to display later outside of the session
            update_scores_by_id(session,db_user.id)
            total = get_total_points_by_id(session,db_user.id)
            session.commit()
        await context.reply(f"Through the power of admin abuse <:trollface:1260219910928203879> {user.mention} have been granted {award_value:,} bias score and now has {new_bias_points:,}",silent=True,ephemeral=isephemeral)
        await checkforpromotion(user,total,bot)
    else:
        await context.reply("fuck off, low rank, no admin abuse for you <:trollface:1260219910928203879>",ephemeral=isephemeral)

@bot.hybrid_command(with_app_command=True)
async def forcedatejoined(context:cmd.Context, user:discord.Member, date_yyyymmdd:str):
    if(context.author.guild_permissions.administrator):
        if (is_yyyymmdd(date_yyyymmdd)):
            with Session(engine) as session:
                db_user =session.get(User,user.id)
                dt_object = datetime.strptime(date_yyyymmdd, "%Y/%m/%d")
                db_user.date_joined=dt_object
                session.commit()
            await context.reply(f"{user.mention}'s date joined has been repaired and set to {dt_object:%Y/%m/%d} (YYYY/MM/DD format).",silent=True,ephemeral=True)
        else:
            await context.reply("You must input the date in a YYYY/MM/DD format !",ephemeral=True)
    else:
        await context.reply("fuck off, you're not admin, you're not elligible to use this command")
# endregion
########################################################
########################################################
########################################################
########################################################
#region strikes commands


# @bot.hybrid_command(with_app_command=True)
# async def strike(context:cmd.Context, user:discord.Member, nb_strikes:int, note:str):
#     if(context.author.guild_permissions.administrator):

#         with Session(engine) as session:
#             db_strikes_user = session.get(Strikes,user.key)
#             if not(user_strikes_exists_by_key(db_strikes_user)):
#                 new_strikes_user = Strikes(user_id=user.id,key=user.id,time_until_next_clean=datetime.now(timezone.utc),active_strikes=nb_strikes, active_strikes_notes=note)
#                 session.add(new_strikes_user)
#             else :
#                 ## TODO call method to check for strike cleaning
                
#                 if db_strikes_user.active_strikes==0:
#                     db_strikes_user.time_until_next_clean=datetime.now(timezone.utc)

#                 db_strikes_user.active_strikes = db_strikes_user.active_strikes+nb_strikes

#                 for c in range (nb_strikes):
#                     db_strikes_user.active_strikes_notes = db_strikes_user.active_strikes_notes + STR_SEPARATOR + note

            
            ## TODO call punishment method



#     else :
#         await context.reply("fuck off, you're not admin, you're not elligible to use this command")

# @bot.hybrid_command(with_app_command=True)
# async def showstrikes(context:cmd.Context, user:discord.Member):
#     if (isModOrHigher(context.author)):
#         if user is None :
#             user = context.author
#         with Session(engine) as session:
#             db_strikes_user = session.get(Strikes,user.key)



#             if not(user_strikes_exists_by_key(db_strikes_user)):
#                 await context.reply("{user.mention} never recieved a strike before !")
            
#             #else : TODO REAL DISPLAY


#     else:
#         await context.reply("fuck off, you're not moderator, you're not elligible to use this command")



# endregion
########################################################
########################################################
########################################################
########################################################
    
   
    

bot.run(token, log_handler=handler, log_level=logging.DEBUG)