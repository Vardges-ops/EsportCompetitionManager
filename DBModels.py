from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()
engine = create_engine("sqlite:///tournaments.db", echo=True)


class GameType(Base):
    __tablename__ = 'gametype'

    Id = Column(Integer, primary_key=True)
    game_type = Column(String)
    platform = Column(String)

    games = relationship('Game', back_populates='game_type')


class Game(Base):
    __tablename__ = 'game'

    Id = Column(Integer, primary_key=True)
    name = Column(String)
    type_id = Column(Integer, ForeignKey('gametype.Id'))

    tournaments = relationship("Tournament", back_populates='game')


class Tournament(Base):
    __tablename__ = 'tournament'

    Id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(DateTime)
    end = Column(DateTime)

    game_id = Column(Integer, ForeignKey('game.Id'))
    game = relationship("Game", back_populates='tournaments')

    places = relationship("TournamentPlace", back_populates='tournament')


class Player(Base):
    __tablename__ = 'player'

    Id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    nickname = Column(String)
    rating = Column(Integer)
    clan = Column(String)
    email = Column(String)

    place = relationship("TournamentPlace", back_populates="player")


class TournamentPlace(Base):
    __tablename__ = 'tournamentplace'

    Id = Column(Integer, primary_key=True)
    position = Column(Integer)
    place_price = Column(String)

    tournament_id = Column(Integer, ForeignKey('tournament.Id'))
    tournament = relationship("Tournament", back_populates="places")

    player_id = Column(Integer, ForeignKey('player.Id'))
    player = relationship("Player", back_populates="tournaments")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
