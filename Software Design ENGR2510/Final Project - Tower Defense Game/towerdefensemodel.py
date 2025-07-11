"""
Implementation of Game class
"""

import math
import random
import pygame
import constants as c
from towerdefenseview import Environment
from towerdefensecontroller import Controller

pygame.init()


class Game:
    """
    Game element used to facilitate tower defense gameplay

    Attributes:
        image: an Environment instance that maps game elements to screen
        wave: a int that represents the current enemy wave
        health: an int that represents the health a player has
        money: an int that represents the money a player has
        enemy_list: a list that represents enemies in one wave
        spawned_enemies: an int that represents the amount of enemies
        spawned in one wave
        killed_enemies: an int that represents the amount of enemies
        killed in one wave
        killed_enemies: an int that represents the amount of enemies
        missed in one wave
        last_enemy_spawn: an int that represents the time of the last
        enemy spawned
    """

    def __init__(self):
        """
        Creates instance of Game

        Attributes:
            screen: a pygame display representing the game screen
            image: an instance of Environment
            wave: an int representing the wave number
            health: an int representing the health of the player
            money: an int representing the money that the player has
            enemy_list: a list representing enemies
            spawned_enemies: an int representing all spawned enemies
            killed_enemies: an int representing all killed enemies
            missed_enemies: an int representing all enemies missed by towers
            last_enemy_spawn: keeps track of the time of the game for last spawn
            enemy_group: the type of enemy sprite
        """
        self._screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
        self._image = Environment(self._screen)
        self._wave = 1
        self._health = c.STARTING_HEALTH
        self._money = c.STARTING_MONEY
        self._enemy_list = []
        self._spawned_enemies = 0
        self._killed_enemies = 0
        self._missed_enemies = 0
        self._last_enemy_spawn = pygame.time.get_ticks()
        self.enemy_group = pygame.sprite.Group()

    def main(self):
        """
        main docstring here:
        """
        restart = True

        pygame.init()
        pygame.display.set_caption("Olin Tower Defense")

        while restart:
            self._wave = 1
            self._health = c.STARTING_HEALTH
            self._money = c.STARTING_MONEY
            self._enemy_list = []
            self._spawned_enemies = 0
            self._killed_enemies = 0
            self._missed_enemies = 0
            self._last_enemy_spawn = pygame.time.get_ticks()
            self.enemy_group = pygame.sprite.Group()
            restart = False
            running = True
            start = True

            clock = pygame.time.Clock()
            game_environment = Environment(self._screen)
            game_controller = Controller(game_environment, self)

            self.create_waves()
            self.enemy_group = pygame.sprite.Group()
            tower_group = []

            while start:
                game_environment.draw_start_screen()
                c.START_BUTTON.press_button(self._screen)
                for event in pygame.event.get():
                    start, running = game_controller.control_start_screen(
                        event, start, running
                    )
                pygame.display.update()
                clock.tick(c.FPS)

            # game loop
            while running:
                self._screen.fill(c.LIGHT_GREEN)
                game_environment.draw_path()
                game_environment.draw_positions(
                    c.TOWER_BASE, c.TOWER_POSITIONS_THEORY
                )

                # updating enemies
                for enemy in self.enemy_group:
                    enemy.update(self, self.enemy_group)
                    game_environment.draw_healthbar(enemy)

                # drawing towers and enemies
                self.enemy_group.draw(self._screen)
                for tower_instance in tower_group:
                    game_environment.draw_tower(
                        self._screen,
                        (tower_instance.x, tower_instance.y),
                        tower_instance.image,
                        tower_instance.radius,
                    )
                for tower_instance in tower_group:
                    tower_instance.flash_text(self._screen)
                game_environment.flash_text()
                game_environment.draw_sidebar(
                    self.money, self.health, self.wave
                )
                c.ARCHER_BUTTON.press_button(self._screen)
                c.WIZARD_BUTTON.press_button(self._screen)
                c.INFERNO_BUTTON.press_button(self._screen)
                c.SELL_BUTTON.press_button(self._screen)
                c.UPGRADE_BUTTON.press_button(self._screen)

                self.spawn_enemies(self.enemy_group)
                self.update_wave()

                # for loop through the event queue
                for event in pygame.event.get():
                    # Check for QUIT event
                    if event.type == pygame.QUIT:
                        running = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        tower_group = game_controller.control_towers(
                            pygame.mouse.get_pressed(),
                            pygame.mouse.get_pos(),
                            tower_group,
                        )

                for tower_instance in tower_group:
                    self.enemy_group = tower_instance.tower_attack(
                        self.enemy_group, self._screen
                    )

                running, restart = self.check_game_over(
                    event, running, restart, game_controller
                )

                pygame.display.update()
                clock.tick(c.FPS)

    def create_waves(self):
        """
        Creates a new wave of enemies

        Args:
            self: instance
        Returns:
            None
        """
        if self._wave <= len(c.ENEMY_WAVE_DATA):
            enemies = c.ENEMY_WAVE_DATA[self._wave - 1]
            for enemy_type, count in enemies.items():
                for _ in range(count):
                    self._enemy_list.append(enemy_type)
            # randomize order each enemy spawns
            random.shuffle(self._enemy_list)

    def check_wave_eliminated(self):
        """
        Checks that a wave is eliminated

        Args:
            self: instance
        returns:
            a bool representing if the wave is eliminated
        """
        if (self._killed_enemies + self._missed_enemies) == len(
            self._enemy_list
        ):
            return True
        else:
            return False

    def reset_for_next_wave(self):
        """
        Resets instance variables for next wave

        Args:
            self: instance

        Returns:
            None
        """
        self._wave += 1
        self._enemy_list = []
        self._spawned_enemies = 0
        self._killed_enemies = 0
        self._missed_enemies = 0

    def level_finished(self):
        """
        Checks if the level is finished

        args:
            self: instance
        returns:
            a bool that represents if the level is finished
        """
        if self._wave == len(c.ENEMY_WAVE_DATA) + 1:
            return True
        return False

    def update_wave(self):
        """
        Moves game to next wave if necessary

        args:
            self: instance
        returns:
            None
        """
        if self.check_wave_eliminated() and self.level_finished() is False:
            self.reset_for_next_wave()
            self.create_waves()

    def spawn_enemies(self, enemy_group):
        """
        Spawns enemies on map

        Args:
            self: instance
            enemy_group: a list that represents a group of enemies

        Returns:
            None
        """
        if pygame.time.get_ticks() - self._last_enemy_spawn > c.SPAWN_DELAY:
            if self._spawned_enemies < len(self._enemy_list):
                enemy_type = self._enemy_list[self._spawned_enemies]
                if enemy_type == "barbs":
                    enemy = Barb(c.BARB)
                if enemy_type == "goblins":
                    enemy = Goblin(c.GOBLIN)
                if enemy_type == "giants":
                    enemy = Giant(c.GIANT)
                enemy_group.add(enemy)
                self._spawned_enemies += 1
                self._last_enemy_spawn = pygame.time.get_ticks()

    def update_money(self, value):
        """
        Updates player money after each kill or tower bought

        Args:
            value: a int representing the value of the transaction
        Returns:
            None
        """
        self._money += value

    def update_health(self, health_decrement):
        """
        Updates player health after enemy reaches end of path

        Args:
            health_decrement: a int representing the amount each enemy
            takes off of player health

        Returns:
            None
        """
        self._health = max(0, self._health - health_decrement)

    def update_killed_enemies(self):
        """
        Updates killed_enemies count

        Args:
            self: instance

        Returns:
            None
        """
        self._killed_enemies += 1

    def update_missed_enemies(self):
        """
        Updates missed_enemies count

        Args:
            self: instance

        Returns:
        None
        """
        self._missed_enemies += 1

    def check_game_over(self, event, running, restart, game_controller):
        """
        Checks if the game is over

        Args:
            self: instance
            event: pygame event
            running (bool): determines if the game runs or not
            restart (bool): determines whether to restart or not
            game_controller: variable for inputs for end screen

        Returns:
            None
        """
        if self.health <= 0 and not self.level_finished():
            self._image.draw_lose_screen()
            c.LOSE_QUIT_BUTTON.press_button(self._screen)
            c.LOSE_RESTART_BUTTON.press_button(self._screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                running, restart = game_controller.control_end_screen(
                    pygame.mouse.get_pos()
                )

        if self.health > 0 and self.level_finished():
            self._image.draw_win_screen()
            c.WIN_QUIT_BUTTON.press_button(self._screen)
            c.WIN_RESTART_BUTTON.press_button(self._screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                running, restart = game_controller.control_end_screen(
                    pygame.mouse.get_pos()
                )
        return running, restart

    @property
    def money(self):
        """
        Property for money

        Args:
            self: instance

        Return:
            self._money: an int that represents the in-game currency
        """
        return self._money

    @property
    def health(self):
        """
        Property for health

        Args:
            self: instance

        Return:
            self._health: an int that represents the current health
        """
        return self._health

    @property
    def wave(self):
        """
        Property for wave

        Args:
            self: instance

        Return:
            self._wave: an int that represents the current wave
        """
        return self._wave

    @property
    def enemy_list(self):
        """
        Property for enemy_list

        Args:
            self: instance

        Return:
            self._enemy_list: a list that represents all enemies
        """
        return self._enemy_list

    @property
    def killed_enemies(self):
        """
        Property for killed_enemies

        Args:
            self: instance

        Return:
            self._killed_enemies: an int that represents the number of
            killed enemies
        """
        return self._killed_enemies

    @property
    def spawned_enemies(self):
        """
        Property for spawned_enemies

        Args:
            self: instance

        Return:
            self._spawned_enemies: an int that represents the number of spawned
            enemies
        """
        return self._spawned_enemies

    @property
    def missed_enemies(self):
        """
        Property for missed_enemies

        Args:
            self: instance

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._missed_enemies


class Tower:
    """
    This class manages all tower related functions

    Attributes:
        game (Game): The game instance the tower belongs to
    """

    def __init__(self, coords, game):
        """
        Creates instance of Tower

        Attributes:
            game (Game): The game instance the tower belongs to
            images (list): List of tower images
            image (pygame.Surface): The current tower image
            projectile_image (pygame.Surface): The image of tower's projectile
            last_shot (int): Timestamp of the last shot
            tick_2 (int): Timestamp of a secondary action
            flash_time (int): Timestamp for flashing text
            flashing_text (str): Text to be displayed when flashing
            tower_value (int): The value of the tower
            projectile_width (int): Width of tower's projectile
            x (int): The x-coordinate of the tower
            y (int): The y-coordinate of the tower
            level (int): The level of the tower
            damage (int): The damage of the tower
            attack_range (int): The attack range of the tower
            radius (int): The radius of the tower
            cooldown_time (int): The cooldown time of the tower
            cooldown_2_time (int): The secondary cooldown time of the tower
            enemies_in_range (list): List of enemies in range of the tower
            enemies_in_range_position (list): List of positions of enemies in range of the tower
            target_enemy (Enemy): The target enemy of the tower
        """
        self.game = game
        self.images = c.ARCHER_IMAGES
        self.image = self.images[0]
        self.projectile_image = None
        self.last_shot = pygame.time.get_ticks()
        self.tick_2 = pygame.time.get_ticks()
        self.flash_time = -3000
        self.flashing_text = "Hi"
        self.tower_value = 50
        self.projectile_width = 40
        self._x = coords[0]
        self._y = coords[1]
        self._level = 0
        self._damage = 50
        self._attack_range = 150
        self._radius = 150
        self._cooldown_time = 500
        self._cooldown_2_time = 20
        self._enemies_in_range = []
        self._enemies_in_range_position = []
        self._target_enemy = None

    def flash_text(self, window):
        """
        Display flashing text on the window.

        Args:
            window (pygame.Surface): The game window surface.
        """
        if pygame.time.get_ticks() - self.flash_time < 3000:
            text = pygame.font.SysFont("Arial", 60).render(
                self.flashing_text, True, (255, 0, 0)
            )
            text_rect = text.get_rect(
                center=((c.WIDTH - 200) // 2, c.HEIGHT // 2)
            )
            window.blit(text, text_rect)

    def tower_attack(self, enemy_group, window):
        """
        Perform tower's attack on enemies within range.

        Args:
            enemy_group (list): List of enemy objects.
            window (pygame.Surface): The game window surface.

        Returns:
            list: Updated list of enemy objects after attack.
        """
        self._enemies_in_range = []
        self._enemies_in_range_position = []
        for enemy in enemy_group:
            distance_to_enemy = math.sqrt(
                (self.x - enemy.rect.x - 35) ** 2
                + (self.y + 30 - enemy.rect.y - 35) ** 2
            )
            if distance_to_enemy < self._attack_range:
                self._enemies_in_range.append(enemy)
                self._enemies_in_range_position.append(enemy.position)
        if len(self._enemies_in_range) > 0 or self._target_enemy:
            if self._target_enemy:
                self.animate(self._target_enemy, window)
            if self.cooldown():
                if self._target_enemy:
                    self._target_enemy.decrement_health(self._damage)
                if len(self._enemies_in_range) > 0:
                    self._target_enemy = self._enemies_in_range[
                        self._enemies_in_range_position.index(
                            max(self._enemies_in_range_position)
                        )
                    ]
                else:
                    self._target_enemy = None

            return enemy_group
        return enemy_group

    def animate(self, target_enemy, window):
        """
        Animate tower's attack on a target enemy.

        Args:
            target_enemy (Enemy): The enemy being targeted.
            window (pygame.Surface): The game window surface.
        """
        distance_to_enemy = math.sqrt(
            (target_enemy.rect.x + 35 - self.x) ** 2
            + (target_enemy.rect.y + 35 - self.y + 25) ** 2
        )

        angle = math.degrees(
            math.atan2(
                -(target_enemy.rect.y + 35 - self.y + 25),
                (target_enemy.rect.x + 35 - self.x),
            )
        )

        scaled_image = pygame.transform.smoothscale(
            self.projectile_image,
            (distance_to_enemy * 2, self.projectile_width),
        )

        rotated_image, new_rect = rot_center(
            scaled_image, angle, self.x, self.y - 25
        )
        window.blit(rotated_image, new_rect)

    def upgrade(self):
        """
        Upgrade the tower's level and attributes if conditions are met.

        Args:
            self: instance

        Returns:
            None
        """
        if self._level == 2:
            self.flashing_text = "Tower Is Already Max Level!"
            self.flash_time = pygame.time.get_ticks()
        elif self.game.money - 100 < 0:
            self.flashing_text = "Not Enough Money!"
            self.flash_time = pygame.time.get_ticks()
        else:
            self._level += 1
            self.image = self.images[self._level]
            self._radius += 15
            self._attack_range += 15
            self._damage += 10
            self.game.update_money(-100)

    def cooldown(self):
        """
        Check if the tower's cooldown time has passed.

        Returns:
            bool: True if cooldown time has passed, False otherwise.
        """
        if pygame.time.get_ticks() - self.last_shot > (self._cooldown_time):
            self.last_shot = pygame.time.get_ticks()
            return True
        return False

    def cooldown_2(self):
        """
        Check if the tower's secondary cooldown time has passed.

        Returns:
            bool: True if secondary cooldown time has passed, False otherwise.
        """
        if pygame.time.get_ticks() - self.tick_2 > (self._cooldown_2_time):
            self.tick_2 = pygame.time.get_ticks()
            return True
        return False

    @property
    def x(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._x

    @property
    def y(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._y

    @property
    def level(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._level

    @property
    def damage(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._damage

    @property
    def attack_range(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._attack_range

    @property
    def radius(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._radius

    @property
    def cooldown_time(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._cooldown_time

    @property
    def cooldown_2_time(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._cooldown_2_time

    @property
    def enemies_in_range(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._enemies_in_range

    @property
    def enemies_in_range_position(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._enemies_in_range_position

    @property
    def target_enemy(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._target_enemy


class ArcherTower(Tower):
    """
    This class inherits Tower

    Attributes:
        game (Game): The game instance the tower belongs to
    """

    def __init__(self, coords, game):
        """
        Creates instance of ArcherTower

        Attributes:
            game (Game): The game instance the tower belongs to
            images (list): List of tower images
            image (pygame.Surface): The current tower image
            projectile_image (pygame.Surface): The image of tower's projectile
            last_shot (int): Timestamp of the last shot
            tick_2 (int): Timestamp of a secondary action
            flash_time (int): Timestamp for flashing text
            flashing_text (str): Text to be displayed when flashing
            tower_value (int): The value of the tower
            projectile_width (int): Width of tower's projectile
            x (int): The x-coordinate of the tower
            y (int): The y-coordinate of the tower
            level (int): The level of the tower
            damage (int): The damage of the tower
            attack_range (int): The attack range of the tower
            radius (int): The radius of the tower
            cooldown_time (int): The cooldown time of the tower
            cooldown_2_time (int): The secondary cooldown time of the tower
            enemies_in_range (list): List of enemies in range of the tower
            enemies_in_range_position (list): List of positions of enemies in
            range of the tower
            target_enemy (Enemy): The target enemy of the tower
        """
        super().__init__(coords, game)
        self.images = c.ARCHER_IMAGES
        self.image = self.images[0]
        self.projectile_images = c.ARCHER_PROJECTILES
        self.last_shot = pygame.time.get_ticks()
        self._damage = 30
        self._attack_range = 225
        self._radius = 225
        self._cooldown_time = 600
        self._cooldown_2_times = [100, 200, 300, 400, 500]
        self._tower_value = 50

    def animate(self, target_enemy, window):
        """
        Animate tower's attack on a target enemy.

        Args:
            target_enemy (Enemy): The enemy being targeted.
            window (pygame.Surface): The game window surface.
        """
        distance_to_enemy = math.sqrt(
            (target_enemy.rect.x + 35 - self.x) ** 2
            + (target_enemy.rect.y + 35 - self.y + 25) ** 2
        )

        angle = math.degrees(
            math.atan2(
                -(target_enemy.rect.y + 35 - self._y + 25),
                (target_enemy.rect.x + 35 - self._x),
            )
        )

        scaled_image = pygame.transform.smoothscale(
            self.projectile_images[self.cooldown_2()],
            (distance_to_enemy * 2, 20),
        )

        rotated_image, new_rect = rot_center(
            scaled_image, angle, self._x, self._y - 25
        )
        window.blit(rotated_image, new_rect)

    def cooldown_2(self):
        """
        Check if the tower's secondary cooldown time has passed.

        Args:
            self: instance
        Returns:
            bool: True if secondary cooldown time has passed, False otherwise.
        """
        if (
            (self._cooldown_2_times[0])
            > pygame.time.get_ticks() - self.tick_2
            > 0
        ):
            return 0
        if (
            (self._cooldown_2_times[1])
            > pygame.time.get_ticks() - self.tick_2
            > (self._cooldown_2_times[0])
        ):
            return 1
        if (
            (self._cooldown_2_times[2])
            > pygame.time.get_ticks() - self.tick_2
            > (self._cooldown_2_times[1])
        ):
            return 2
        if (
            (self._cooldown_2_times[3])
            > pygame.time.get_ticks() - self.tick_2
            > (self._cooldown_2_times[2])
        ):
            return 3
        if (
            (self._cooldown_2_times[4])
            > pygame.time.get_ticks() - self.tick_2
            > (self._cooldown_2_times[3])
        ):
            return 4
        self.tick_2 = pygame.time.get_ticks()
        return 5


class WizardTower(Tower):
    """
    This class inherits from Tower to make an instance of a Wizard Tower

    Attributes:
        game (Game): The game instance the tower belongs to
    """

    def __init__(self, coords, game):
        """ "
        Creates instance of ArcherTower

        Attributes:
            game (Game): The game instance the tower belongs to
            images (list): List of tower images
            image (pygame.Surface): The current tower image
            projectile_image (pygame.Surface): The image of tower's projectile
            last_shot (int): Timestamp of the last shot
            tick_2 (int): Timestamp of a secondary action
            flash_time (int): Timestamp for flashing text
            flashing_text (str): Text to be displayed when flashing
            tower_value (int): The value of the tower
            projectile_width (int): Width of tower's projectile
            x (int): The x-coordinate of the tower
            y (int): The y-coordinate of the tower
            level (int): The level of the tower
            damage (int): The damage of the tower
            attack_range (int): The attack range of the tower
            radius (int): The radius of the tower
            cooldown_time (int): The cooldown time of the tower
            cooldown_2_time (int): The secondary cooldown time of the tower
            enemies_in_range (list): List of enemies in range of the tower
            enemies_in_range_position (list): List of positions of enemies in
            range of the tower
            target_enemy (Enemy): The target enemy of the tower
        """
        super().__init__(coords, game)
        self.last_shot = pygame.time.get_ticks()
        self.tick_2 = pygame.time.get_ticks()
        self.images = c.WIZARD_IMAGES
        self.image = self.images[0]
        self.projectile_image = c.WIZARD_PROJECTILE
        self.projectile_width = 80
        self._cooldown_time = 1500
        self._cooldown_2_time = 500
        self._damage = 20
        self._attack_range = 160
        self._radius = 160
        self._tower_value = 70

    def tower_attack(self, enemy_group, window):
        """
        Perform tower's attack on enemies within range.

        Args:
            enemy_group (list): List of enemy objects.
            window (pygame.Surface): The game window surface.

        Returns:
            list: Updated list of enemy objects after attack.
        """
        self._enemies_in_range = []
        self._enemies_in_range_position = []
        for enemy in enemy_group:
            distance_to_enemy = math.sqrt(
                (self.x - enemy.rect.x - 35) ** 2
                + (self.y + 30 - enemy.rect.y - 35) ** 2
            )
            if distance_to_enemy < self._attack_range:
                self._enemies_in_range.append(enemy)
                self._enemies_in_range_position.append(enemy.position)
        if len(self._enemies_in_range) > 0:
            for enemy in self._enemies_in_range:
                if self.cooldown_2():
                    self.animate(enemy, window)
                if self.cooldown() and self.cooldown_2():
                    enemy.decrement_health(self._damage)
            if self.cooldown() and self.cooldown_2():
                self.tick_2 = pygame.time.get_ticks()
                self.last_shot = pygame.time.get_ticks()
        return enemy_group

    def cooldown(self):
        """
        Check if the tower's cooldown time has passed.

        Returns:
            bool: True if cooldown time has passed, False otherwise.
        """
        if pygame.time.get_ticks() - self.last_shot > (self._cooldown_time):
            return True
        return False

    def cooldown_2(self):
        """
        Check if the tower's secondary cooldown time has passed.

        Returns:
            bool: True if secondary cooldown time has passed, False otherwise.
        """
        if pygame.time.get_ticks() - self.tick_2 > (self._cooldown_2_time):
            return True
        return False


class InfernoTower(Tower):
    """
    This class inherits from Tower to make an instance of an Inferno Tower

    Attributes:
        game (Game): The game instance the tower belongs to
    """

    def __init__(self, coords, game):
        """
        Creates instance of ArcherTower

        Attributes:
            game (Game): The game instance the tower belongs to
            images (list): List of tower images
            image (pygame.Surface): The current tower image
            projectile_image (pygame.Surface): The image of tower's projectile
            last_shot (int): Timestamp of the last shot
            tick_2 (int): Timestamp of a secondary action
            flash_time (int): Timestamp for flashing text
            flashing_text (str): Text to be displayed when flashing
            tower_value (int): The value of the tower
            projectile_width (int): Width of tower's projectile
            x (int): The x-coordinate of the tower
            y (int): The y-coordinate of the tower
            level (int): The level of the tower
            damage (int): The damage of the tower
            attack_range (int): The attack range of the tower
            radius (int): The radius of the tower
            cooldown_time (int): The cooldown time of the tower
            cooldown_2_time (int): The secondary cooldown time of the tower
            enemies_in_range (list): List of enemies in range of the tower
            enemies_in_range_position (list): List of positions of enemies in
            range of the tower
            target_enemy (Enemy): The target enemy of the tower
        """
        super().__init__(coords, game)
        self.last_shot = pygame.time.get_ticks()
        self.tick_2 = pygame.time.get_ticks()
        self.images = c.INFERNO_IMAGES
        self.image = self.images[0]
        self.projectile_image = c.INFERNO_PROJECTILE
        self._cooldown_time = 100
        self._cooldown_2_time = 400
        self._enemies_in_range = []
        self._target_enemy = None
        self._new_target_enemy = None
        self._damage_counter = 1
        self._tower_value = 70
        self._damage = 2
        self._attack_range = 150

    def tower_attack(self, enemy_group, window):
        """
        Perform tower's attack on enemies within range.

        Args:
            enemy_group (list): List of enemy objects.
            window (pygame.Surface): The game window surface.

        Returns:
            list: Updated list of enemy objects after attack.
        """
        self._enemies_in_range = []
        self._enemies_in_range_position = []
        for enemy in enemy_group:
            distance_to_enemy = math.sqrt(
                (self.x - enemy.rect.x - 35) ** 2
                + (self.y + 30 - enemy.rect.y - 35) ** 2
            )
            if distance_to_enemy < self._attack_range:
                self._enemies_in_range.append(enemy)
                self._enemies_in_range_position.append(enemy.position)
        if len(self._enemies_in_range) > 0:
            if self._new_target_enemy == self._target_enemy:
                if self.cooldown_2():
                    self._damage_counter += 1
            else:
                self._damage_counter = 1
                self._target_enemy = self._new_target_enemy
            self._new_target_enemy = self._enemies_in_range[
                self._enemies_in_range_position.index(
                    max(self._enemies_in_range_position)
                )
            ]
            if self._target_enemy:
                self.animate(self._target_enemy, window)
            if self.cooldown():
                self._new_target_enemy.decrement_health(
                    self._damage**self._damage_counter
                )
            return enemy_group
        return enemy_group

    def upgrade(self):
        """
        Upgrade the tower's level and attributes if conditions are met.

        Args:
            self: instance

        Returns:
            None
        """
        if self._level == 2:
            self.flashing_text = "Tower Is Already Max Level!"
            self.flash_time = pygame.time.get_ticks()
        elif self.game.money - 100 < 0:
            self.flashing_text = "Not Enough Money!"
            self.flash_time = pygame.time.get_ticks()
        else:
            self._level += 1
            self.image = self.images[self._level]
            self._radius += 25
            self._attack_range += 25
            self._damage += 0.5
            self.game.update_money(-100)

    @property
    def damage_counter(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._damage_counter

    @property
    def new_target_enemy(self):
        """
        Property for missed_enemies

        Return:
            self._missed_enemies: an int that representing the number of
            enemies that reached the end
        """
        return self._new_target_enemy


def rot_center(image, angle, x, y):
    """
    A function that rotates an image

    Args:
        angle (int): An int representing an angle
        x (int): An int representing x coordinate of the image
        y (int): An int representing y coordinate of the image

    Returns:
        rotated_image (object): The rotated image
        new_rect (int): The x,y coordinates for the

    """
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(x, y)).center
    )
    return rotated_image, new_rect


class Enemy(pygame.sprite.Sprite):
    """
    Base enemy class

    Attributes:
        _max_health: an int representing the max health of an enemy
        _speed: a float representing the speed of an enemy
        _health: an int representing the current health of an enemy
        _position: and int representing initial position multiplayer
        _kill_value: an int representing the money a player gets from a kill
        _health_decrement: an int that represents how much an enemy
        decrements player health if it reached the end of the path
        image: a string representing the source location of the sprite image
        rect: FILL THIS IN LATer!!!!
    """

    _max_health = 200
    _speed = 0.005
    _health = 200
    _position = -2.1
    _kill_value = 10
    _health_decrement = 10

    def __init__(self, image):
        """
        Creates an instance of Enemy

        Args:
            image: a string representing the source location of the sprite image
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()

    def update(self, world, enemy_group):
        """
        Updates the status of enemies on the screen

        Args:
            screen: a pygame display representing the game screen
            world: a game instance representing the current tower defense game
            enemy_group: a list representing the enemy group on the map
        """
        self.move()
        self.reach_end(world, enemy_group)
        self.is_dead(world)

    def move(self):
        """
        Moves the enemy
        """
        self._position += self._speed
        self.rect.x = (self._position + 5 * math.cos(self._position) + 3.5) * 90
        self.rect.y = (
            -self._position - math.sin(2 * self._position) - 2.1
        ) * -90
        return (self.rect.x, self.rect.y)

    def is_dead(self, world):
        """
        Checks if the enemy is dead

        Args:
            world: a game instance representing the current tower defense game
        """
        if self._health <= 0:
            world.update_killed_enemies()
            world.update_money(self._kill_value)
            self.kill()
            return True
        return False

    def reach_end(self, world, enemy_group):
        """
        Checks if the enemy reaches the end of the path

        Args:
            world: a game instance representing the current tower defense game
            enemy_group: a list representing the enemy group on the map
        """
        if self.rect.x >= c.WIDTH - 200:
            world.update_missed_enemies()
            world.update_health(self._health_decrement)
            self.kill()
            enemy_group.remove(self)
            return True
        return False

    def decrement_health(self, damage):
        """
        Decrement health of enemy

        Args:
            damage: an int that represents how much to decrement by
        """
        self._health -= damage
        return self._health

    @property
    def position(self):
        """
        Property to access _position attribute

        Returns
            self._position: a float that gives the position of the enemy
        """
        return self._position

    @property
    def health(self):
        """
        Property to access health attribute

        Returns
            self._health: an int that gives the health of the enemy
        """
        return self._health

    @property
    def max_health(self):
        """
        Property to access the max_health attribute

        Returns
            self._max_health: an int that gives the max health of the enemy
        """
        return self._max_health


class Barb(Enemy):
    """
    Barbarian enemy

    Attributes:
        _max_health: an int representing the max health of an enemy
        _speed: a float representing the speed of an enemy
        _health: an int representing the current health of an enemy
        _position: and int representing initial position multiplayer
        _kill_value: an int representing the money a player gets from a kill
        _health_decrement: an int that represents how much an enemy
        decrements player health if it reached the end of the path
        image: a string representing the source location of the sprite image
        rect: an int representing the coordinates for the sprite hit box
    """

    def __init__(self, image):
        """
        Creates an instance of a Giant

        Args:
            image: a string representing the source location of the sprite image
        """
        super().__init__(image)
        self._kill_value = 8
        self._max_health = 200
        self._speed = 0.005
        self._health = 200


class Giant(Enemy):
    """
    Giant enemy

    Attributes:
        _max_health: an int representing the max health of an enemy
        _speed: a float representing the speed of an enemy
        _health: an int representing the current health of an enemy
        _position: and int representing initial position multiplayer
        _kill_value: an int representing the money a player gets from a kill
        _health_decrement: an int that represents how much an enemy
        decrements player health if it reached the end of the path
        image: a string representing the source location of the sprite image
        rect: an int representing the coordinates for the sprite hit box
    """

    def __init__(self, image):
        """
        Creates an instance of a Giant

        Args:
            image: a string representing the source location of the sprite image
        """
        super().__init__(image)
        self._kill_value = 12
        self._speed = 0.0025
        self._health = 500
        self._max_health = 500


class Goblin(Enemy):
    """
    Goblin enemy

    Attributes:
        _max_health: an int representing the max health of an enemy
        _speed: a float representing the speed of an enemy
        _health: an int representing the current health of an enemy
        _position: and int representing initial position multiplayer
        _kill_value: an int representing the money a player gets from a kill
        _health_decrement: an int that represents how much an enemy
        decrements player health if it reached the end of the path
        image: a string representing the source location of the sprite image
        rect: an int representing the coordinates for the sprite hit box
    """

    def __init__(self, image):
        """
        Creates an instance of a Goblin

        Args:
            image: a string representing the source location of the sprite image
        """
        super().__init__(image)
        self._kill_value = 4
        self._speed = 0.01
        self._health = 100
        self._max_health = 100
