from lib.ship_placement import ShipPlacement

"""
Initialises with a given length, row, column
"""

def test_initialises_with_a_given_length_as_well():
    placement = ShipPlacement(length=5, row=2, column=3, orientation="vertical")
    assert placement.length == 5
    assert placement.row == 2
    assert placement.column == 3
    assert placement.orientation == "vertical"
