from lib.game import Game

"""
Initialises with list of ship_lengths and ships_placed
"""

def test_inititalises_with_list_of_ship_lengths():
    game = Game()
    assert game.ship_lengths == [2,3,3,4,5]
    assert game.ships_placed == []