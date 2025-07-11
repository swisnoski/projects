"""
test file for towerdefensecontroler
"""

import pygame
import constants as c
from towerdefensemodel import Game, Tower
from towerdefensecontroller import Controller

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
test_game_controller = Game()
test_controller = Controller(screen, test_game_controller)
coords = (151, 201)
test_tower = Tower(coords, test_game_controller)


def test_button_input_no_mouse():
    """
    check that nothing happens if the mouse is not clicked
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [False]
    click_coords = (1, 1)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    )


def test_button_input_no_press():
    """
    check that nothing happens if the mouse is not clicked on a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (1, 1)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    )


def test_button_input_button_1():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (926, 286)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    )


def test_button_input_button_2():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (926, 366)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
    )


def test_button_input_button_3():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (926, 446)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
        ]
    )


def test_button_input_button_4():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (926, 526)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            False,
            False,
            True,
            False,
            False,
            False,
        ]
    )


def test_button_input_button_5():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (926, 606)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            False,
        ]
    )


def test_button_input_button_6():
    """
    check that button press is tracked if mouse clicks a button
    """
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
    ]
    mouse_presses = [True]
    click_coords = (151, 201)
    tower_positons = c.TOWER_POSITIONS_THEORY
    button_coords = c.BUTTON_COORDS
    tower_positions_taken = []
    test_controller.button_input(
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    )
    assert (
        test_controller._valid_placement  # pylint: disable=protected-access
        == [
            False,
            False,
            True,
            True,
            False,
            False,
            False,
            False,
        ]
    )


def test_return_tower_positions():
    """
    check that return tower_position correctly returns a tower
    """
    click_coords = (151, 201)
    tower_positions_possible = c.TOWER_POSITIONS_THEORY
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
    ]
    result = [
        test_controller.return_tower_positions(
            click_coords, tower_positions_possible
        )
    ]
    assert len(result) == 1


def test_control_towers():
    """
    check that control_towers correctly adds a tower to tower_positions
    """
    mouse_presses = [True]
    click_coords = (151, 201)
    tower_positions = []
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        False,
    ]
    tower_positions = test_controller.control_towers(
        mouse_presses, click_coords, tower_positions
    )
    assert len(tower_positions) == 1


def test_sell_tower():
    """
    Check that sell_tower correctly removes a tower from tower_positions
    """
    click_coords = (151, 201)
    tower_group = []
    test_controller._valid_placement = [  # pylint: disable=protected-access
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]
    tower_positions = test_controller.sell_tower(click_coords, tower_group)
    assert len(tower_group) == 0


@property
def test_upgrade_tower():
    """
    Check that upgrade_tower correctly upgrades a tower
    """
    mouse_presses = [True]
    click_coords = (151, 201)
    tower_group = [test_tower]
    tower_positions = []
    test_controller._valid_placement = [  # pylint: disable=protected-access
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        False,
    ]
    tower_positions = test_controller.control_towers(
        mouse_presses, click_coords, tower_positions
    )
    test_controller.upgrade_tower(click_coords, tower_group)
    assert test_tower._level == 1


def test_control_end_screen():
    """
    Check that control_end_screen correctly ends game when quit is pressed
    """
    click_coords = (c.WIDTH * 0.5, c.HEIGHT * 0.5)
    [x, y] = test_controller.control_end_screen(click_coords)
    assert not x, not y


def test_control_start_screen():
    """
    Check that the control_start_screen correctly starts the game when start is
    pressed
    """
    click_coords = (c.WIDTH * 0.5, c.HEIGHT * 0.5)

    mouse_button_down_event = pygame.event.Event(
        pygame.MOUSEBUTTONDOWN, pos=click_coords
    )

    pygame.event.post(mouse_button_down_event)

    x, y = test_controller.control_start_screen(
        mouse_button_down_event, False, False
    )

    assert not x, not y
