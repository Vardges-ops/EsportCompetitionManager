from .ModelsInterface import *


DEFAULT_GAMETYPES = [{'game_type': 'Shooter', 'platform': 'PC'}, {'game_type': 'MMORPG', 'platform': 'PC'}]
for gtype in DEFAULT_GAMETYPES:
    GameTypeInterface.add_gametype(**gtype)
GameInterface.insert_game('Counter Strike', GameTypeInterface.get_gametype_by_name('Shooter').Id)
GameInterface.insert_game('DOTA 2', GameTypeInterface.get_gametype_by_name('MMORPG'))


class GameInsertionConsole(GameTypeInterface, GameInterface):

    def insert_new_game(self, game_name, game_type_name):
        gametype = self.get_gametype_by_name('Shooter')
        if gametype is None:
            raise ValueError('Game type not found, insert it first')
        self.insert_game(game_name, self.get_gametype_by_name(game_type_name).Id)



class TournamentInsertionConsole:
    pass


class TournamentPlaceInsertionConsole:
    pass


class InsertionConsole:
    pass

DEFAULT_PLAYER = dict(name='EMPTY', surname='EMPTY', nickname='EMPTY', rating=None, clan='EMPTY', email='EMPTY')
players = [PlayerType(**DEFAULT_PLAYER).insert_player() for _ in range(5)]
games = []
