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

def test_is_playable():
    assert callable(u.is_playable)
    assert isinstance(u.is_playable('skip', 'r1'), bool)
    assert(u.is_playable('+2', 'r1') == True)
    assert(u.is_playable('r1', '+2') == True)
    assert(u.is_playable('r1', 'r1') == True)
    assert(u.is_playable('b1', 'r1') == True)
    assert(u.is_playable('r1', 'b6') == False)
