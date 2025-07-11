"""
This file manages the game environment and user interface.
"""

import math
import pygame
import numpy as np
import constants as c

pygame.init()
font_really_small = pygame.font.SysFont("Arial", 14)
font_small = pygame.font.SysFont("Arial", 18)
font_big = pygame.font.SysFont("Arial", 30)
font_really_big = pygame.font.SysFont("Arial", 60)


class Environment:
    """
    This class manages the game environment.

    Attributes:
        screen (pygame.Surface): The game screen.
        path_coords (list): List of coordinates representing the game path.
        flashing_text (str): Text to be displayed when flashing.
        flash_time (int): Timestamp for flashing text.
    """

    range = np.linspace(-2.1, 5.4, 750)
    path_coords = []
    for i in range:
        path_coords.append(
            (
                ((i + 5 * math.cos(i) + 4.0) * 90),
                ((-i - math.sin(2 * i) - 2.6) * -90),
            )
        )
    flashing_text = "Hi"
    flash_time = -3000

    def __init__(self, screen):
        """
        Initializes the Environment.

        Args:
            screen (pygame.Surface): The game screen.
        """
        self._screen = screen
        self.flashing_text = "Hi"
        self.flash_time = -3000

    def draw_path(self):
        """
        Draws the game path.

        Args:
            self: instance

        Returns:
            None
        """
        for coord in self.path_coords:
            pygame.draw.circle(self._screen, "BLACK", coord, 50)

    def draw_positions(self, base_image, positions):
        """
        Draws positions on the screen.

        Args:
            base_image (pygame.Surface): The base image to draw.
            positions (list): List of positions to draw.
        """
        for position in positions:
            x = position[0] - 50
            y = position[1] - 20
            self._screen.blit(base_image, (x, y))

    def make_text(self, text, rect_coords, color, font):
        """
        Creates text on the screen.

        Args:
            text (str): The text to display.
            rect_coords (tuple): Coordinates of the text rectangle.
            color (tuple): Text color.
            font (pygame.font.Font): Font to use for the text.
        """
        rect = pygame.Rect(rect_coords)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        self._screen.blit(text_surface, text_rect)

    def draw_sidebar(self, currency, health, wave_number):
        """
        Draws the sidebar containing game information.

        Args:
            currency (int): The currency value.
            health (int): The health value.
            wave_number (int): The wave number.
        """
        menu_rect = pygame.Rect((900, 0), (200, 800))
        pygame.draw.rect(self._screen, pygame.Color(75, 54, 33), menu_rect)

        wave_rect = pygame.Rect((925, 10), (150, 50))
        pygame.draw.rect(self._screen, pygame.Color(209, 203, 193), wave_rect)
        self.make_text(
            f"WAVE {wave_number}", ((925, 10), (150, 50)), "BLACK", font_small
        )

        money_rect = pygame.Rect((925, 70), (150, 50))
        pygame.draw.rect(self._screen, pygame.Color(209, 203, 193), money_rect)
        self.make_text(
            f"MONEY: {currency} G",
            ((925, 70), (150, 50)),
            "BLACK",
            font_small,
        )

        health_rect = pygame.Rect((925, 130), (150, 50))
        pygame.draw.rect(self._screen, pygame.Color(209, 203, 193), health_rect)
        self.make_text(
            f"HEALTH: {health}", ((925, 130), (150, 50)), "BLACK", font_small
        )

    def draw_start_screen(self):
        """
        Draws the start screen.

        Args:
            self: instance

        Returns:
            None
        """
        self._screen.fill(c.START_SCREEN_COLOR)
        start_button_rect = pygame.Rect(c.START_BUTTON_COORDS)
        pygame.draw.rect(
            self._screen, pygame.Color(c.START_BUTTON_COLOR), start_button_rect
        )
        self.make_text("Start", (c.START_BUTTON_COORDS), "WHITE", font_big)

    def draw_lose_screen(self):
        """
        Draw the lose screen

        Args:
            self: instance

        Returns:
            None
        """

        # Screen color
        self._screen.fill(c.LOSE_SCREEN_COLOR)

        # Game over button
        game_over_button_rect = pygame.Rect(c.END_BUTTON_COORDS_1)
        pygame.draw.rect(
            self._screen,
            pygame.Color(c.LOSE_SCREEN_COLOR),
            game_over_button_rect,
        )
        self.make_text("GAME OVER", (c.END_BUTTON_COORDS_1), "WHITE", font_big)

        # Quit Button
        quit_button_rect = pygame.Rect(c.END_BUTTON_COORDS_2)
        pygame.draw.rect(
            self._screen, pygame.Color(c.LOSE_BUTTON_COLOR), quit_button_rect
        )
        self.make_text(
            "QUIT", (c.END_BUTTON_COORDS_2), "WHITE", font_really_big
        )

        # Restart Button
        restart_button_rect = pygame.Rect(c.END_BUTTON_COORDS_3)
        pygame.draw.rect(
            self._screen,
            pygame.Color(c.LOSE_BUTTON_COLOR),
            restart_button_rect,
        )
        self.make_text(
            "RESTART", (c.END_BUTTON_COORDS_3), "WHITE", font_really_big
        )

    def draw_win_screen(self):
        """
        Draw the win screen

        Args:
            self: instance

        Returns:
            None
        """

        # Screen color
        self._screen.fill(c.WIN_SCREEN_COLOR)

        # Game over button
        game_over_button_rect = pygame.Rect(c.END_BUTTON_COORDS_1)
        pygame.draw.rect(
            self._screen,
            pygame.Color(c.WIN_SCREEN_COLOR),
            game_over_button_rect,
        )
        self.make_text("YOU WIN!", (c.END_BUTTON_COORDS_1), "WHITE", font_big)

        # Quit Button
        quit_button_rect = pygame.Rect(c.END_BUTTON_COORDS_2)
        pygame.draw.rect(
            self._screen, pygame.Color(c.WIN_BUTTON_COLOR), quit_button_rect
        )

        # Restart Button
        restart_button_rect = pygame.Rect(c.END_BUTTON_COORDS_3)
        pygame.draw.rect(
            self._screen,
            pygame.Color(c.WIN_BUTTON_COLOR),
            restart_button_rect,
        )

    def flash_text(self):
        """
        Flashes text on the screen.

        Args:
            self: instance

        Returns:
            None
        """
        if pygame.time.get_ticks() - self.flash_time < 2000:
            text = font_really_big.render(self.flashing_text, True, (255, 0, 0))
            text_rect = text.get_rect(
                center=((c.WIDTH - 200) // 2, c.HEIGHT // 2)
            )
            self._screen.blit(text, text_rect)

    def draw_tower(self, window, click_coords, image, radius):
        """
        Draws a tower on the screen.

        Args:
            window (pygame.Surface): The game window.
        """
        scale_factor = (80, 100)
        image = pygame.transform.scale(image, scale_factor)
        centered_coords = (
            click_coords[0] - scale_factor[0] / 2,
            click_coords[1] - scale_factor[1] / 2,
        )
        circle = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(circle, (255, 0, 0, 50), (radius, radius), radius)
        window.blit(
            circle,
            (click_coords[0] - radius, click_coords[1] - radius + 30),
        )
        window.blit(image, (centered_coords))

    def draw_healthbar(self, enemy):
        """
        Display healthbar under each enemy

        Args:
            screen: a pygame display representing the game screen
        """
        full_health = pygame.Rect((enemy.rect.x, enemy.rect.y + 70), (70, 10))
        pygame.draw.rect(self._screen, "WHITE", full_health)
        full_health = pygame.Rect(
            (enemy.rect.x, enemy.rect.y + 70),
            ((enemy.health / enemy.max_health) * 70, 10),
        )
        pygame.draw.rect(self._screen, "RED", full_health)


class DrawButton:
    """
    This class represents a button that can be drawn on the screen.
    """

    def __init__(self, button_coords, text, color):
        """
        Initializes the DrawButton.

        Args:
            button_coords (tuple): The coordinates and dimensions of the button
                                    (x, y, width, height).
            text (str): The text to display on the button.
            color (dict): A dictionary containing color values for different
                         button states
                          (normal, hover, pressed).
        """
        self.x = button_coords[0]
        self.y = button_coords[1]
        self.width = button_coords[2]
        self.height = button_coords[3]

        self.button_surface = pygame.Surface((self.width, self.height))
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.button_text = font_really_small.render(text, True, (20, 20, 20))
        self.fill_colors = color

    def press_button(self, window):
        """
        Draws the button and handles button press events.

        Args:
            window (pygame.Surface): The game window.
        """
        mouse_coords = pygame.mouse.get_pos()
        self.button_surface.fill(self.fill_colors["normal"])
        if self.button_rect.collidepoint(mouse_coords):
            self.button_surface.fill(self.fill_colors["hover"])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.button_surface.fill(self.fill_colors["pressed"])

        self.button_surface.blit(
            self.button_text,
            [
                self.button_rect.width / 2
                - self.button_text.get_rect().width / 2,
                self.button_rect.height / 2
                - self.button_text.get_rect().height / 2,
            ],
        )
        window.blit(self.button_surface, self.button_rect)
