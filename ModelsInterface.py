from typing import Optional, List
from datetime import datetime
from DBModels import *


class GameTypeInterface:

    @staticmethod
    def get_all_gametypes():
        with Session(bind=engine) as session:
            return session.query(GameType).all()

    @staticmethod
    def add_gametype(game_type: str, platform: str):
        with Session(bind=engine) as session:
            session.add(GameType(game_type=game_type, platform=platform))

    @staticmethod
    def change_gametype(gametype_id: int, new_type: str):
        with Session(bind=engine) as session:
            session.query(GameType).get(gametype_id).update({'game_type': new_type})

    @staticmethod
    def delete_gametype(gametype_id):
        with Session(bind=engine) as session:
            session.query(GameType).get(gametype_id).delete()


class GameInterface:

    def __init__(self):
        self.games_list = None
        self.game_match = None

    def get_game_by_id(self, game_id: int):
        with Session(bind=engine) as session:
            self.game_match = session.query(Game).get(game_id)

    def get_game_by_name(self, game_name: str):
        with Session(bind=engine) as session:
            self.game_match = session.query(Game).filter(Game.name == game_name).first()

    def get_all_games(self):
        with Session(bind=engine) as session:
            self.games_list = session.query(Game).all()

    def update_matched_game_name(self, new_name: str):
        self.update_matched_game_attribute('name', new_name)

    def update_matched_game_type(self, new_type_id: str):
        self.update_matched_game_attribute('type_id', new_type_id)

    def update_matched_game_attribute(self, attr_name: str, new_attr_id: str):
        if self.game_match is None:
            raise ValueError("First get game then change")
        else:
            self.game_match.update({attr_name: new_attr_id})


class TournamentType:
    def __init__(self,
                 name: str,
                 start: Optional[datetime] = None,
                 end: Optional[datetime] = None,
                 game_id: Optional[int] = None
                 ):
        self.name = name
        self.start = start
        self.end = end
        self.game_id = game_id

    def insert_tournament(self):
        if all(self.__dict__.values()):
            with Session(bind=engine) as session:
                session.add(Tournament(*self.__dict__))
        else:
            print("TournamentType object has None values")


class TournamentFinder:

    def __init__(self):
        self.obj_holder = None

    def get_tournament_by_name(self, name: str):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Tournament).filter(Tournament.name == name).first()

    def get_tournament_by_id(self, tourn_id: int):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Tournament).get(tourn_id)

    def get_tournament_by_game_id(self, game_id: int):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Tournament).filter(Tournament.game_id == game_id).first()

    @staticmethod
    def get_upcoming_tournaments():
        now = datetime.now()
        with Session(bind=engine) as session:
            print("Tournament upcoming objects")
            return session.query(Tournament).filter(Tournament.start < now).all()

    @staticmethod
    def get_passed_tournaments():
        now = datetime.now()
        with Session(bind=engine) as session:
            print("Tournament passed objects")
            return session.query(Tournament).filter(Tournament.end > now).all()

    @staticmethod
    def get_ongoing_tournaments():
        now = datetime.now()
        with Session(bind=engine) as session:
            print("Tournament ongoing objects")
            return session.query(Tournament).filter(Tournament.start > now, Tournament.end < now).all()


class TournamentUpdater:

    @staticmethod
    def update_tournament_attribute(tourn_id, **kwargs):
        with Session(bind=engine) as session:
            session.query(Tournament).get(tourn_id).update(kwargs)


class TournamentDeleter:

    @staticmethod
    def delete_tournament_by_id(tourn_id):
        with Session(bind=engine) as session:
            session.query(Tournament).get(tourn_id).delete()


class PlayerType:
    def __init__(self,
                 name: Optional[str],
                 surname: Optional[str],
                 nickname: Optional[str],
                 rating: Optional[str],
                 clan: Optional[str],
                 email: Optional[str]):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.rating = rating
        self.clan = clan
        self.email = email

    def insert_player(self):
        with Session(bind=engine) as session:
            session.add(Player(**self.__dict__))


class PlayerFinder:

    def __init__(self):
        self.obj_holder = None

    def find_player_by_id(self, player_id: int):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Player).get(player_id)

    def find_player_by_email(self, email: str):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Player).filter(Player.email == email).first()

    def find_tournament_player_by_nickname(self, nickname: str):
        with Session(bind=engine) as session:
            self.obj_holder = session.query(Player).filter(Player.nickname == nickname).first()

    @staticmethod
    def find_players_by_equal_higher_rank(rank: float):
        with Session(bind=engine) as session:
            return session.query(Player).filter(Player.rating >= rank).all()


class TournamentPlaceInterface:

    @staticmethod
    def give_tournament_players(tournament_id: int) -> List[Player]:
        with Session(bind=engine) as session:
            tourn_objs = session.query(TournamentPlace).filter(TournamentPlace.tournament_id == tournament_id).all()
            return [obj.player for obj in tourn_objs if tourn_objs]

    @staticmethod
    def give_tournamentplace_objects(tournament_id: int):
        with Session(bind=engine) as session:
            tourn_objs = session.query(TournamentPlace).filter(TournamentPlace.tournament_id == tournament_id).all()
            return tourn_objs

    @staticmethod
    def give_tournament_place_price_pairs(tournament_id: int):
        tourn_objs = TournamentPlaceInterface.give_tournamentplace_objects(tournament_id)
        return {tourn_obj.position: tourn_obj.place_price for tourn_obj in tourn_objs}

    @staticmethod
    def swap_two_players(tournament_id: int, higher_player_id: int, lower_player_id: int):
        with Session(bind=engine) as session:
            higher_player_obj = session.query(TournamentPlace).filter(
                TournamentPlace.tournament_id == tournament_id,
                TournamentPlace.player_id == higher_player_id).first()
            lower_player_obj = session.query(TournamentPlace).filter(
                TournamentPlace.tournament_id == tournament_id,
                TournamentPlace.player_id == lower_player_id).first()

            higher_player_obj.player_id = lower_player_id
            lower_player_obj.player_id = higher_player_id
