"""Test for my functions."""

import unobot as u

def test_draw_num():
    assert callable(u.draw_num)
    assert u.draw_num(4, 'player') == 4
    assert u.draw_num(2, 'computer') == 2

def test_win():
    assert callable(u.win)
    assert u.win(True, 'player') == False
    assert u.win(True, 'computer') == False

def test_freeplay():
    assert callable(u.freeplay)
    assert isinstance(u.freeplay('skip'), bool)
    assert(u.freeplay('+2') == True)
