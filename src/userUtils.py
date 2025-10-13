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

async def checkforpromotion(user:discord.Member,total:int):
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
            await channeltoping.send(f"{pingmodsandadmins} I think {user.mention} climbed from the depths and deserves to be <@&455515632742694929> again.\nIf you agree, don't forget to promote them IN GAME first!",silent=True )
            session.get(NotifTrack,(user.id,KITTENROLE)).status=True
            
        session.commit()
