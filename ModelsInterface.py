from typing import Optional

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
            self.game_match = session.query(Game).filter(Game.name == game_name).one_or_none()

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


class TournamentInterface:
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

    def update_name(self, new_name: str):
        self.name = new_name

    def update_game_start(self, start: datetime):
        self.start = start

    def update_game_end(self, end: datetime):
        self.end = end

    def set_game_id(self, game_id: int):
        self.game_id = game_id
