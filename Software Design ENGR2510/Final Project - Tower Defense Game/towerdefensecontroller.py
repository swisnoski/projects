"""
This file contains the controller component of our MVC architecture
The controller class handles all inputs for the game
"""

import pygame
import constants as c
import towerdefensemodel

pygame.init()


class Controller:
    """
    The controller class manages the interaction between the game environment
    and user input.

    This class handles user input events and controls the placement, selling,
    and upgrading of towers within the game environment. It also manages actions
    on the start and end screens.

    Attributes:
        environment (object): The instance of the game environment.
        game (object): The instance of the game.
        _valid_placement (list): A list of boolean values indicating valid tower
                                 placements.
    """

    def __init__(self, enviornment, game):
        """
        Initialize Controller with environment and game instances.

        Args:
            environment (object): Environment instance.
            game (object): Game instance.
        """
        self.enviornment = enviornment
        self.game = game
        self._valid_placement = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]

    def button_input(
        self,
        mouse_presses,
        click_coords,
        tower_positons,
        button_coords,
        tower_positions_taken,
    ):
        """
        Process button input.

        Args:
            mouse_presses (list): List of mouse button presses.
            click_coords (tuple): Coordinates of the mouse click (x, y).
            tower_positions (list): Positions of existing towers.
            button_coords (list): Coordinates of buttons.
            tower_positions_taken (list): Positions occupied by existing towers.

        Returns:
            no returns
        """
        if mouse_presses[0]:
            if (
                button_coords[0][0]
                <= click_coords[0]
                <= (button_coords[0][0] + button_coords[0][2])
            ):
                if (
                    button_coords[0][1]
                    <= click_coords[1]
                    <= (button_coords[0][1] + button_coords[0][3])
                ):
                    self._valid_placement[0] = True
                    self._valid_placement[1] = False
                    self._valid_placement[2] = False
                    self._valid_placement[4] = False
                    self._valid_placement[6] = False
                elif (
                    button_coords[1][1]
                    <= click_coords[1]
                    <= (button_coords[1][1] + button_coords[1][3])
                ):
                    self._valid_placement[0] = False
                    self._valid_placement[1] = True
                    self._valid_placement[2] = False
                    self._valid_placement[4] = False
                    self._valid_placement[6] = False
                elif (
                    button_coords[2][1]
                    <= click_coords[1]
                    <= (button_coords[2][1] + button_coords[2][3])
                ):
                    self._valid_placement[0] = False
                    self._valid_placement[1] = False
                    self._valid_placement[2] = True
                    self._valid_placement[4] = False
                    self._valid_placement[6] = False

                elif (
                    button_coords[3][1]
                    <= click_coords[1]
                    <= (button_coords[3][1] + button_coords[3][3])
                ):
                    self._valid_placement[0] = False
                    self._valid_placement[1] = False
                    self._valid_placement[2] = False
                    self._valid_placement[4] = True
                    self._valid_placement[6] = False

                elif (
                    button_coords[4][1]
                    <= click_coords[1]
                    <= (button_coords[4][1] + button_coords[4][3])
                ):
                    self._valid_placement[0] = False
                    self._valid_placement[1] = False
                    self._valid_placement[2] = False
                    self._valid_placement[4] = False
                    self._valid_placement[6] = True

        if (
            self._valid_placement[0]
            or self._valid_placement[1]
            or self._valid_placement[2]
        ):
            for coords in tower_positons:
                if (
                    coords[0] - 25 <= click_coords[0] <= coords[0] + 25
                    and coords[1] - 25 <= click_coords[1] <= coords[1] + 25
                ):
                    click_coords = (coords[0], coords[1] - 30)
                    self._valid_placement[3] = True
                    for tower_instance in tower_positions_taken:
                        if click_coords == (tower_instance.x, tower_instance.y):
                            self._valid_placement[3] = False
        if self._valid_placement[4]:
            for coords in tower_positons:
                if (
                    coords[0] - 25 <= click_coords[0] <= coords[0] + 25
                    and coords[1] - 25 <= click_coords[1] <= coords[1] + 25
                ):
                    click_coords = (coords[0], coords[1] - 30)
                    for tower_instance in tower_positions_taken:
                        if click_coords == (tower_instance.x, tower_instance.y):
                            self._valid_placement[5] = True
        if self._valid_placement[6]:
            for coords in tower_positons:
                if (
                    coords[0] - 25 <= click_coords[0] <= coords[0] + 25
                    and coords[1] - 25 <= click_coords[1] <= coords[1] + 25
                ):
                    click_coords = (coords[0], coords[1] - 30)
                    for tower_instance in tower_positions_taken:
                        if click_coords == (tower_instance.x, tower_instance.y):
                            self._valid_placement[7] = True

    def return_tower_positions(self, click_coords, tower_pos_possible):
        """
        Return tower positions.

        Args:
            click_coords (tuple): Coordinates of the mouse click (x, y).
            tower_pos_possible (list): Possible tower positions.

        Returns:
            object: Tower instance if placement is valid, else None.
        """
        for coords in tower_pos_possible:
            if (
                coords[0] - 25 <= click_coords[0] <= coords[0] + 25
                and coords[1] - 25 <= click_coords[1] <= coords[1] + 25
            ):
                click_coords = (coords[0], coords[1] - 30)
        if self._valid_placement[0]:
            self.game.update_money(-50)
            return towerdefensemodel.ArcherTower(click_coords, self.game)

        elif self._valid_placement[1]:
            self.game.update_money(-75)
            return towerdefensemodel.WizardTower(click_coords, self.game)

        elif self._valid_placement[2]:
            self.game.update_money(-75)
            return towerdefensemodel.InfernoTower(click_coords, self.game)
        return None

    def control_towers(self, mouse_presses, click_coords, tower_positions):
        """
        Control tower placement, selling, and upgrading.

        Args:
            mouse_presses (list): List of mouse button presses.
            click_coords (tuple): Coordinates of the mouse click (x, y).
            tower_positions (list): Positions of existing towers.

        Returns:
            tower_positions (list): Updated tower positions.
        """

        self.button_input(
            mouse_presses,
            click_coords,
            c.TOWER_POSITIONS_THEORY,
            c.BUTTON_COORDS,
            tower_positions,
        )

        if self._valid_placement[3]:
            if self._valid_placement[0] and self.game.money - 50 < 0:
                self.enviornment.flashing_text = "Not Enough Money!"
                self.enviornment.flash_time = pygame.time.get_ticks()
            elif self._valid_placement[1] and self.game.money - 75 < 0:
                self.enviornment.flashing_text = "Not Enough Money!"
                self.enviornment.flash_time = pygame.time.get_ticks()
            elif self._valid_placement[2] and self.game.money - 75 < 0:
                self.enviornment.flashing_text = "Not Enough Money!"
                self.enviornment.flash_time = pygame.time.get_ticks()
            else:
                tower_positions.append(
                    self.return_tower_positions(
                        click_coords,
                        c.TOWER_POSITIONS_THEORY,
                    )
                )
            self._valid_placement = [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ]
            return tower_positions

        elif self._valid_placement[5]:
            tower_positions = self.sell_tower(click_coords, tower_positions)
            self._valid_placement = [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ]
            return tower_positions

        elif self._valid_placement[7]:
            self.upgrade_tower(click_coords, tower_positions)
            self._valid_placement = [
                False,
                False,
                False,
                False,
                False,
                False,
                False,
                False,
            ]
            return tower_positions

        return tower_positions

    def sell_tower(self, click_coords, tower_group):
        """
        Sell a tower.

        Args:
            click_coords (tuple): Coordinates of the mouse click (x, y).
            tower_group (list): Group of towers.

        Returns:
            tower_group (list): Updated tower group after selling a tower.
        """
        for tower_instance in tower_group:
            x = tower_instance.x
            y = tower_instance.y + 30
            if (
                x - 25 <= click_coords[0] <= x + 25
                and y - 25 <= click_coords[1] <= y + 25
            ):
                tower_group.remove(tower_instance)
                sell_value = (
                    tower_instance.tower_value + tower_instance.level * 100
                ) // 2
                self.game.update_money(sell_value)
                return tower_group

    def upgrade_tower(self, click_coords, tower_group):
        """
        Upgrade a tower.

        Args:
            click_coords (tuple): Coordinates of the mouse click (x, y).
            tower_group (list): Group of towers.

        Returns:
            Runs tower upgrade function, no returns
        """
        for tower_instance in tower_group:
            x = tower_instance.x
            y = tower_instance.y + 30
            if (
                x - 25 <= click_coords[0] <= x + 25
                and y - 25 <= click_coords[1] <= y + 25
            ):
                tower_instance.upgrade()

    def control_end_screen(self, click_coords):
        """
        Control actions on the end screen.

        Args:
            click_coords (tuple): Coordinates of the mouse click (x, y).

        Returns:
            tuple: Tuple indicating whether to exit the game and whether to
                   restart.
        """
        if (
            click_coords[0] >= c.END_BUTTON_COORDS_2[0]
            and click_coords[0]
            <= c.END_BUTTON_COORDS_2[0] + c.END_BUTTON_COORDS_2[2]
            and click_coords[1] >= c.END_BUTTON_COORDS_2[1]
            and click_coords[1]
            <= c.END_BUTTON_COORDS_2[1] + c.END_BUTTON_COORDS_2[3]
        ):
            return False, False
        if (
            click_coords[0] >= c.END_BUTTON_COORDS_3[0]
            and click_coords[0]
            <= c.END_BUTTON_COORDS_3[0] + c.END_BUTTON_COORDS_3[2]
            and click_coords[1] >= c.END_BUTTON_COORDS_3[1]
            and click_coords[1]
            <= c.END_BUTTON_COORDS_3[1] + c.END_BUTTON_COORDS_3[3]
        ):
            return False, True
        else:
            return True, False

    def control_start_screen(self, event, start, running):
        """
        Control actions on the start screen.

        Args:
            event (object): Event object.
            start (bool): Boolean indicating start state.
            running (bool): Boolean indicating running state.

        Returns:
            tuple: Tuple indicating updated start and running states.
        """

        if event.type == pygame.QUIT:
            start = False
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_coords = pygame.mouse.get_pos()
            if (
                click_coords[0] >= c.START_BUTTON_COORDS[0]
                and click_coords[0]
                <= c.START_BUTTON_COORDS[0] + c.START_BUTTON_COORDS[2]
                and click_coords[1] >= c.START_BUTTON_COORDS[1]
                and click_coords[1]
                <= c.START_BUTTON_COORDS[1] + c.START_BUTTON_COORDS[3]
            ):
                start = False

        return start, running

    @property
    def valid_placement(self):
        """
        Property for health

        Return:
            self._health: an int that represents the current health
        """
        return self._valid_placement
