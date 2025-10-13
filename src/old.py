# class ScanTrack(Base):
#     __tablename__ = 'scantrack'
#     guild:Mapped[int] = mapped_column(primary_key=True) 
#     currently_scanning:Mapped[bool] = mapped_column(default=False)
#     channel_scanning:Mapped[int] = mapped_column(default=0)
    


#     @classmethod
#     def getbyid(cls,session,id) -> 'ScanTrack':
#         return session.get(cls,id)

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

# @bot.hybrid_command(with_app_command=True)
# async def truetimejoined(context:cmd.Context,user:typing.Optional[discord.User]=None):
#     user.

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