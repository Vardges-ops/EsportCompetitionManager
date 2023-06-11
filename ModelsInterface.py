from DBModels import *


class GameInterface:

    def __init__(self):
        self.games_list = None
        self.game_match = None

    def get_game_by_id(self, game_id: int):
        with Session(bind=engine) as session:
            self.game_match = session.query(Game).get(game_id)

    def get_game_by_name(self, game_name: str):
        with Session(bind=engine) as session:
            self.game_match = session.query(Game).filter(Game.name==game_name).one_or_none()

    def get_all_games(self):
        with Session(bind=engine) as session:
            self.games_list = session.query(Game).all()

    def get_games_by_type(self, game_type: str):
        pass

    def update_matched_game_name(self, new_name: str):
        if self.game_match is None:
            raise Exception("First get game then change")
        else:
            self.game_match.update({'name': new_name})

    def update_matched_game_type(self, new_type_id: str):
        if self.game_match is None:
            raise Exception("First get game then change")
        else:
            self.game_match.update({'type_id': new_type_id})


class TournamentInterface:
    pass
