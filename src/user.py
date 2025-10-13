from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base, Session, DeclarativeBase, relationship

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

    notified_for_promotions_each_roles:Mapped[List["NotifTrack"]] = relationship(
        back_populates="user",cascade="all,delete-orphan"
    )


    @classmethod
    def getbyid(cls,session,id) -> 'User':
        return session.get(cls,id)
