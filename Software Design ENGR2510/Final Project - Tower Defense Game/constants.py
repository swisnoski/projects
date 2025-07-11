"""
This file contains all the constants needed for tower defense game
"""

import pygame
from towerdefenseview import DrawButton

FPS = 60

# background for game map
LIGHT_GREEN = (152, 251, 152)

# width and height of view
WIDTH, HEIGHT = (1100, 800)

# coordinates for buying each tower
BUTTON_1_COORDS = (925, 285, 150, 70)
BUTTON_2_COORDS = (925, 365, 150, 70)
BUTTON_3_COORDS = (925, 445, 150, 70)
SELL_BUTTON_COORDS = (925, 525, 150, 70)
UPGRADE_BUTTON_COORDS = (925, 605, 150, 70)
BUTTON_COORDS = [
    BUTTON_1_COORDS,
    BUTTON_2_COORDS,
    BUTTON_3_COORDS,
    SELL_BUTTON_COORDS,
    UPGRADE_BUTTON_COORDS,
]

# available positions to place towers
TOWER_POSITIONS_THEORY = [
    (150, 200),
    (500, 160),
    (700, 300),
    (350, 260),
    (290, 440),
    (540, 470),
    (210, 690),
    (450, 600),
    (700, 580),
    (800, 750),
]

# start screen
START_SCREEN_COLOR = (0, 153, 153)
START_BUTTON_COLOR = (255, 233, 91)
START_BUTTON_COORDS = (
    WIDTH * 0.5 - 3 * WIDTH // 16,
    HEIGHT * 0.5 - 2 * HEIGHT // 14,
    3 * WIDTH // 8,
    2 * HEIGHT // 7,
)

# lose screen
LOSE_SCREEN_COLOR = (255, 120, 91)
LOSE_BUTTON_COLOR = (80, 159, 253)

# win screen
WIN_SCREEN_COLOR = (94, 216, 75)
WIN_BUTTON_COLOR = (250, 199, 46)


# all end screen buttons
END_BUTTON_COORDS_1 = (
    WIDTH * 0.5 - 3 * WIDTH // 16,
    HEIGHT * 0.5 - 2 * HEIGHT // 7,
    3 * WIDTH // 8,
    HEIGHT // 7,
)
END_BUTTON_COORDS_2 = (
    WIDTH * 0.5 - 3 * WIDTH // 16,
    HEIGHT * 0.5 - HEIGHT // 14,
    3 * WIDTH // 8,
    HEIGHT // 7,
)
END_BUTTON_COORDS_3 = (
    WIDTH * 0.5 - 3 * WIDTH // 16,
    HEIGHT * 0.5 + HEIGHT // 7,
    3 * WIDTH // 8,
    HEIGHT // 7,
)


# player starting health and currency and enemy data
STARTING_HEALTH = 100
STARTING_MONEY = 200
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
    {
        # 3
        "barbs": 20,
        "goblins": 10,
        "giants": 8,
    },
    {
        # 4
        "barbs": 0,
        "goblins": 50,
        "giants": 0,
    },
    {
        # 5
        "barbs": 24,
        "goblins": 10,
        "giants": 20,
    },
]

# value player gets per kill


# load and scale image sizes
ARCHER_IMAGES = [
    pygame.image.load("assets/archer1.png"),
    pygame.image.load("assets/archer2.png"),
    pygame.image.load("assets/archer3.png"),
]
WIZARD_IMAGES = [
    pygame.image.load("assets/wizard1.png"),
    pygame.image.load("assets/wizard2.png"),
    pygame.image.load("assets/wizard3.png"),
]
INFERNO_IMAGES = [
    pygame.image.load("assets/inferno1.png"),
    pygame.image.load("assets/inferno2.png"),
    pygame.image.load("assets/inferno3.png"),
]
INFERNO_PROJECTILE = pygame.image.load("assets/inferno_projectile.png")
WIZARD_PROJECTILE = pygame.image.load("assets/wizard_projectile.png")
ARCHER_PROJECTILES = [
    pygame.image.load("assets/archer_projectile_1.png"),
    pygame.image.load("assets/archer_projectile_2.png"),
    pygame.image.load("assets/archer_projectile_3.png"),
    pygame.image.load("assets/archer_projectile_4.png"),
    pygame.image.load("assets/archer_projectile_5.png"),
    pygame.image.load("assets/archer_projectile_blank.png"),
]

TOWER_BASE_IMAGE = pygame.image.load("assets/dirt_mound.png")
TOWER_BASE = pygame.transform.scale(TOWER_BASE_IMAGE, (100, 40))

BARB_IMAGE = pygame.image.load("assets/barb.png")
GIANT_IMAGE = pygame.image.load("assets/giant.png")
GOBLIN_IMAGE = pygame.image.load("assets/goblin.png")
BARB = pygame.transform.scale(BARB_IMAGE, (70, 70))
GIANT = pygame.transform.scale(GIANT_IMAGE, (70, 70))
GOBLIN = pygame.transform.scale(GOBLIN_IMAGE, (70, 70))

# button colors
TOWER_BUTTON_COLOR = {
    "normal": "#DBE2E9",
    "hover": "#8C92AC",
    "pressed": "#63666A",
}

START_PRESS_BUTTON_COLORS = {
    "normal": "#FFE95B",
    "hover": "#FFF19B",
    "pressed": "#FFDC00",
}

LOSE_PRESS_BUTTON_COLORS = {
    "normal": "#509FFD",
    "hover": "#94C4FD",
    "pressed": "#0074FF",
}

WIN_PRESS_BUTTON_COLORS = {
    "normal": "#FAC72E",
    "hover": "#FADF8D",
    "pressed": "#D39F00",
}


START_BUTTON = DrawButton(
    START_BUTTON_COORDS, "Start", START_PRESS_BUTTON_COLORS
)
ARCHER_BUTTON = DrawButton(
    BUTTON_1_COORDS, "Archer Tower (50 G)", TOWER_BUTTON_COLOR
)
WIZARD_BUTTON = DrawButton(
    BUTTON_2_COORDS, "Wizard Tower (75 G)", TOWER_BUTTON_COLOR
)
INFERNO_BUTTON = DrawButton(
    BUTTON_3_COORDS, "Inferno Tower (75 G)", TOWER_BUTTON_COLOR
)
SELL_BUTTON = DrawButton(SELL_BUTTON_COORDS, "Sell Tower", TOWER_BUTTON_COLOR)
UPGRADE_BUTTON = DrawButton(
    UPGRADE_BUTTON_COORDS, "Upgrade Tower (100 G)", TOWER_BUTTON_COLOR
)
LOSE_QUIT_BUTTON = DrawButton(
    END_BUTTON_COORDS_2, "QUIT", LOSE_PRESS_BUTTON_COLORS
)
LOSE_RESTART_BUTTON = DrawButton(
    END_BUTTON_COORDS_3, "RESTART", LOSE_PRESS_BUTTON_COLORS
)
WIN_QUIT_BUTTON = DrawButton(
    END_BUTTON_COORDS_2, "QUIT", WIN_PRESS_BUTTON_COLORS
)
WIN_RESTART_BUTTON = DrawButton(
    END_BUTTON_COORDS_3, "RESTART", WIN_PRESS_BUTTON_COLORS
)
