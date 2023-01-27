from lib.ship import Ship

"""
Initialises with a given length, row, column
"""

def test_initialises_with_a_given_length():
    ship = Ship(length=5, row=2, column=3, orientation="vertical")
    assert ship.length == 5
    assert ship.row == 2
    assert ship.column == 3
    assert ship.orientation == "vertical"
