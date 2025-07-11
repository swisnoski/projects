"""
test file for towerdefensemodel
"""

import pygame
import constants as c
from towerdefensemodel import (
    Game,
    Enemy,
    Tower,
    ArcherTower,
    WizardTower,
    InfernoTower,
)
from towerdefensecontroller import Controller
from towerdefenseview import Environment

pygame.init()
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
test_game = Game()
test_view = Environment(screen)
test_controller = Controller(screen, test_game)
test_enemy = Enemy(c.BARB_IMAGE)
test_tower = Tower((150, 200), test_game)
test_tower_in_range = Tower((0, 200), test_game)
test_archer = ArcherTower((150, 200), test_game)
test_wizard = WizardTower((0, 200), test_game)
test_inferno = InfernoTower((0, 200), test_game)
enemy_group = pygame.sprite.Group()

SPAWN_DELAY = 600
ENEMY_WAVE_DATA = [
    {
        # 1
        "barbs": 8,
        "goblins": 0,
        "giants": 0,
    },
    {
        # 2
        "barbs": 15,
        "goblins": 15,
        "giants": 3,
    },
]

# vv Game tests vv


def test_create_waves_barbs():
    """
    check that create_waves creates the right amount of barbs
    """
    test_game.create_waves()

    assert (
        test_game._enemy_list.count("barbs")  # pylint: disable=protected-access
        == 8
    )


def test_create_waves_goblins():
    """
    check that create_waves creates the right amount of goblins
    """
    test_game.create_waves()

    assert (
        test_game._enemy_list.count(  # pylint: disable=protected-access
            "goblins"
        )
        == 0
    )


def test_create_waves_giants():
    """
    check that create_waves creates the right amount of giants
    """
    test_game.create_waves()

    assert (
        test_game._enemy_list.count(  # pylint: disable=protected-access
            "giants"
        )
        == 0
    )


def test_check_wave_eliminated_true():
    """
    check that expected true case is true
    """
    test_game._killed_enemies = 2  # pylint: disable=protected-access
    test_game._missed_enemies = 2  # pylint: disable=protected-access
    test_game._enemy_list = [  # pylint: disable=protected-access
        "barb",
        "barb",
        "barb",
        "barb",
    ]
    assert test_game.check_wave_eliminated() is True


def test_check_wave_eliminated_false():
    """
    check that expected true case is true
    """
    test_game._killed_enemies = 1  # pylint: disable=protected-access
    test_game._missed_enemies = 2  # pylint: disable=protected-access
    test_game._enemy_list = [  # pylint: disable=protected-access
        "barb",
        "barb",
        "barb",
        "barb",
    ]
    assert test_game.check_wave_eliminated() is False


def test_reset_for_next_wave():
    """
    check that the instance variables are reset for the next wave
    """
    test_game.reset_for_next_wave()
    assert test_game._wave == 2  # pylint: disable=protected-access
    assert test_game._spawned_enemies == 0  # pylint: disable=protected-access
    assert test_game._killed_enemies == 0  # pylint: disable=protected-access
    assert test_game._missed_enemies == 0  # pylint: disable=protected-access
    assert not test_game._enemy_list  # pylint: disable=protected-access


def test_level_finished_true():
    """
    check that the game level/game is finished when waves are over
    """
    test_game._wave = 6  # pylint: disable=protected-access
    assert test_game.level_finished() is True


def test_level_finished_false():
    """
    check that the game level/game is not finished until waves are over
    """
    test_game._wave = 5  # pylint: disable=protected-access
    assert test_game.level_finished() is False


def test_update_wave():
    """
    check that update wave triggers when wave is finished but level isn't
    """
    test_game._killed_enemies = 2  # pylint: disable=protected-access
    test_game._missed_enemies = 2  # pylint: disable=protected-access
    test_game._enemy_list = [  # pylint: disable=protected-access
        "barb",
        "barb",
        "barb",
        "barb",
    ]
    test_game._wave = 5  # pylint: disable=protected-access
    assert test_game.level_finished() is False


def test_spawn_enemies():
    """
    check that all enemies are spawned
    """
    test_game.create_waves()
    test_game.spawn_enemies(enemy_group)
    assert test_game._spawned_enemies == 0  # pylint: disable=protected-access


def test_update_money():
    """
    check that money is increased by given amount
    """
    test_game.update_money(10)
    assert test_game.money == 210


def test_update_health():
    """
    check that money is increased by given amount
    """
    test_game.update_health(10)
    assert test_game.health == 90


def test_killed_enemies():
    """
    check that money is increased by given amount
    """
    test_game._killed_enemies = 0  # pylint: disable=protected-access
    test_game.update_killed_enemies()
    assert test_game._killed_enemies == 1  # pylint: disable=protected-access


def test_missed_enemies():
    """
    check that money is increased by given amount
    """
    test_game._missed_enemies = 0  # pylint: disable=protected-access
    test_game.update_missed_enemies()
    assert test_game._missed_enemies == 1  # pylint: disable=protected-access


def test_game_over():
    """
    test that game over doesn't alter game state without input
    this is further tested when testing controller/buttons
    """
    event = None
    running = True
    restart = False
    running, restart = test_game.check_game_over(
        event, running, restart, test_controller
    )
    assert running
    assert not restart


# ^^ Game tests ^^
# vv Tower Tests vv


def test_tower_attack():
    """
    test that the tower doesn't attack enemies not in range
    """
    test_game.create_waves()
    test_enemy_group = test_tower.tower_attack(enemy_group, screen)
    for enemy in enemy_group:
        for updated_enemy in test_enemy_group:
            assert enemy.health == updated_enemy.health


def test_tower_attack_in_range():
    """
    test that the tower attacks enemies in range
    """
    test_game.create_waves()
    test_enemy_group = test_tower_in_range.tower_attack(enemy_group, screen)
    for enemy in enemy_group:
        for updated_enemy in test_enemy_group:
            assert enemy.health == (updated_enemy.health + 10)


def test_tower_upgrade():
    """
    tests that upgrade tower upgrades a low level tower properly
    """
    test_tower._level = 0  # pylint: disable=protected-access
    test_tower._damage = 50  # pylint: disable=protected-access
    test_tower._attack_range = 150  # pylint: disable=protected-access
    test_tower._radius = 150  # pylint: disable=protected-access
    test_tower.upgrade()
    assert test_tower.level == 1
    assert test_tower.damage == 60
    assert test_tower.radius == 165
    assert test_tower.attack_range == 165


def test_tower_upgrade_max():
    """
    tests that upgrade tower won't upgrade a max level tower
    """
    test_tower._level = 2  # pylint: disable=protected-access
    test_tower._damage = 50  # pylint: disable=protected-access
    test_tower._attack_range = 150  # pylint: disable=protected-access
    test_tower._radius = 150  # pylint: disable=protected-access
    test_tower.upgrade()
    assert test_tower.level == 2
    assert test_tower.damage == 50
    assert test_tower.radius == 150
    assert test_tower.attack_range == 150


def test_cooldown_true():
    """
    assert that when enough time has passed cooldown is true
    """
    test_tower.last_shot = -3000
    test_tower._cooldown_time = 2500  # pylint: disable=protected-access
    assert test_tower.cooldown() is True


def test_cooldown_false():
    """
    assert that when not enough time has passed cooldown is false
    """
    test_tower.last_shot = -3000
    test_tower._cooldown_time = 3500  # pylint: disable=protected-access
    assert test_tower.cooldown() is False


def test_cooldown_2_true():
    """
    assert that when enough time has passed cooldown_2 is true
    """
    test_tower.tick_2 = -3000
    test_tower._cooldown_2_time = 2500  # pylint: disable=protected-access
    assert test_tower.cooldown_2() is True


def test_cooldown_2_false():
    """
    assert that when not enough time has passed cooldown_2 is false
    """
    test_tower.tick_2 = -3000
    test_tower._cooldown_2_time = 3500  # pylint: disable=protected-access
    assert test_tower.cooldown_2() is False


def test_wizard_attack_in_range():
    """
    test that the wizard tower attacks enemies in range
    """
    test_game.create_waves()
    test_enemy_group = test_wizard.tower_attack(enemy_group, screen)
    for enemy in enemy_group:
        for updated_enemy in test_enemy_group:
            assert enemy.health == (updated_enemy.health + 10)


def test_wizard_cooldown_true():
    """
    assert that when enough time has passed wizard cooldown is true
    """
    test_wizard.last_shot = -3000
    test_wizard._cooldown_time = 2500  # pylint: disable=protected-access
    assert test_wizard.cooldown() is True


def test_wizard_cooldown_false():
    """
    assert that when not enough time has passed wizard cooldown is false
    """
    test_wizard.last_shot = -3000
    test_wizard._cooldown_time = 3500  # pylint: disable=protected-access
    assert test_wizard.cooldown() is False


def test_inferno_attack_in_range():
    """
    test that the wizard tower attacks enemies in range
    """
    test_game.create_waves()
    test_enemy_group = test_inferno.tower_attack(enemy_group, screen)
    for enemy in enemy_group:
        for updated_enemy in test_enemy_group:
            assert enemy.health == (updated_enemy.health + 10)


def test_inferno_tower_upgrade():
    """
    tests that upgrade inferno tower upgrades a low level tower properly
    """
    test_inferno._level = 0  # pylint: disable=protected-access
    test_inferno._damage = 2.5  # pylint: disable=protected-access
    test_inferno._attack_range = 150  # pylint: disable=protected-access
    test_inferno._radius = 150  # pylint: disable=protected-access
    test_inferno.upgrade()
    assert test_inferno.level == 1
    assert test_inferno.damage == 3
    assert test_inferno.radius == 175
    assert test_inferno.attack_range == 175


def test_inferno_tower_upgrade_max():
    """
    tests that upgrade inferno tower won't upgrade a max level tower
    """
    test_inferno._level = 2  # pylint: disable=protected-access
    test_inferno._damage = 50  # pylint: disable=protected-access
    test_inferno._attack_range = 150  # pylint: disable=protected-access
    test_inferno._radius = 150  # pylint: disable=protected-access
    test_inferno.upgrade()
    assert test_inferno.level == 2
    assert test_inferno.damage == 50
    assert test_inferno.radius == 150
    assert test_inferno.attack_range == 150


# ^^ Tower Tests ^^
# vv Enemy Tests vv


def test_move():
    """
    test that the enemy moves on the path
    """
    assert test_enemy.move() == (-99, 78)


def test_is_dead_false():
    """
    test that the enemy is not dead if health is > 0
    """
    test_enemy._health = 10  # pylint: disable=protected-access
    assert test_enemy.is_dead(test_game) is False


def test_is_dead_true():
    """
    test that the enemy is dead if health is <= 0
    """
    test_enemy._health = -10  # pylint: disable=protected-access
    assert test_enemy.is_dead(test_game) is True


def test_reach_end():
    """
    test that an enemy is deleted when reached the end of a map
    """
    test_enemy.rect.x = 1200  # pylint: disable=protected-access
    assert test_enemy.reach_end(test_game, enemy_group) is True


def test_decrement_health():
    """
    test that health is removed when calling decrement_health
    """
    test_enemy._health = 100  # pylint: disable=protected-access
    assert test_enemy.decrement_health(10) == 90
