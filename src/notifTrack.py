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
    