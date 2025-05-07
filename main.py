"""
Yoonho Na
403
TP6 Roche Papier Ciseau main
"""
from Attack_animation import AttackAnimation, AttackType
from game_state import GameState
import arcade
from random import randint


class MyGame(arcade.View):
    """
    Main class de jeu
    """
    def __init__(self):
        """
        Variables
        """
        super().__init__()
        self.game_state = GameState.NOT_STARTED
        self.sprites = arcade.SpriteList()
        self.comp_sprites = arcade.SpriteList()

        self.computer = arcade.Sprite("./assets/compy.png")
        self.computer.center_x = 1040
        self.computer.center_y = 400
        self.computer.scale = 1.5
        self.comp_sprites.append(self.computer)

        self.face = arcade.Sprite("./assets/faceBeard.png")
        self.face.center_x = 300
        self.face.center_y = 400
        self.face.scale = 0.3
        self.sprites.append(self.face)

        self.rock = AttackAnimation(AttackType.ROCK)
        self.rock.center_x = 220
        self.rock.center_y = 280
        self.rock.scale = 0.45
        self.sprites.append(self.rock)

        self.paper = AttackAnimation(AttackType.PAPER)
        self.paper.center_x = 310
        self.paper.center_y = 285
        self.sprites.append(self.paper)

        self.scissor = AttackAnimation(AttackType.SCISSORS)
        self.scissor.center_x = 380
        self.scissor.center_y = 285
        self.scissor.scale = 0.45
        self.sprites.append(self.scissor)

        self.comp_rock = AttackAnimation(AttackType.ROCK)
        self.comp_rock.center_x = 1040
        self.comp_rock.center_y = 280
        self.comp_rock.scale = 0.45

        self.comp_paper = AttackAnimation(AttackType.PAPER)
        self.comp_paper.center_x = 1050
        self.comp_paper.center_y = 285

        self.comp_scissor = AttackAnimation(AttackType.SCISSORS)
        self.comp_scissor.center_x = 1040
        self.comp_scissor.center_y = 285
        self.comp_scissor.scale = 0.45

        self.player_point = 0
        self.comp_point = 0
        self.attack_choice = False
        self.player_attack_type = AttackType
        self.computer_attack_type = AttackType
        self.game_win = 0

    def on_draw(self):
        """
        Aspects visuels
        """
        self.clear()

        arcade.draw.draw_lbwh_rectangle_outline(
            270,
            250,
            65,
            65,
            arcade.csscolor.PINK)

        arcade.draw.draw_lbwh_rectangle_outline(
            190,
            250,
            65,
            65,
            arcade.csscolor.PINK)

        arcade.draw.draw_lbwh_rectangle_outline(
            350,
            250,
            65,
            65,
            arcade.csscolor.PINK)

        arcade.draw.draw_lbwh_rectangle_outline(
            1010,
            250,
            65,
            65,
            arcade.csscolor.PINK)

        arcade.draw_text(
            f"Points de joueur:{self.player_point}",
            240,
            200
        )

        arcade.draw_text(
            f"Points de ordinateur:{self.comp_point}",
            975,
            200
        )

        if self.game_state == GameState.NOT_STARTED:
            arcade.draw_text(
                "Touche espace pour jouer",
                150,
                500,
                arcade.color.PINK,
                70
            )
        elif self.game_state == GameState.ROUND_ACTIVE:
            arcade.draw_text("Round Active",
                             300,
                             500,
                             arcade.csscolor.WHITE,
                             100
                             )
            arcade.draw_text("cliquer sur votre choix",
                             500,
                             450,
                             arcade.csscolor.WHITE,
                             25)
            if self.attack_choice is False:
                if self.comp_scissor in self.comp_sprites:
                    self.comp_sprites.remove(self.comp_scissor)
                elif self.comp_rock in self.comp_sprites:
                    self.comp_sprites.remove(self.comp_rock)
                elif self.comp_paper in self.comp_sprites:
                    self.comp_sprites.remove(self.comp_paper)
                elif self.scissor not in self.sprites:
                    self.sprites.append(self.scissor)
                elif self.rock not in self.sprites:
                    self.sprites.append(self.rock)
                elif self.paper not in self.sprites:
                    self.sprites.append(self.paper)

        elif self.game_state == GameState.ROUND_DONE:

            arcade.draw_text("Toucher espace pour continuer",
                             250,
                             650,
                             arcade.csscolor.WHITE,
                             50)
            if self.game_win == 1:
                arcade.draw_text("Draw",
                                 550,
                                 500,
                                 arcade.csscolor.WHITE,
                                 60)
            elif self.game_win == 2:
                arcade.draw_text("Computer Wins",
                                 400,
                                 500,
                                 arcade.csscolor.WHITE,
                                 60)
            elif self.game_win == 3:
                arcade.draw_text("Player Wins",
                                 450,
                                 500,
                                 arcade.csscolor.WHITE,
                                 60)

        elif self.game_state == GameState.GAME_OVER:
            arcade.draw_text("toucher espace pour recommencer",
                             180,
                             650,
                             arcade.csscolor.WHITE,
                             50)
            if self.player_point == 3:
                arcade.draw_text("Player Wins Game",
                                 160,
                                 510,
                                 arcade.csscolor.WHITE,
                                 100)
            elif self.comp_point == 3:
                arcade.draw_text("Computer Wins Game",
                                 50,
                                 510,
                                 arcade.csscolor.WHITE,
                                 100)
        self.sprites.draw()
        self.comp_sprites.draw()

    def on_update(self, delta_time: float):
        """
        Aspect logic
        """
        self.rock.on_update()
        self.paper.on_update()
        self.scissor.on_update()
        self.comp_rock.on_update()
        self.comp_paper.on_update()
        self.comp_scissor.on_update()

        if self.player_point == 3:
            self.game_state = GameState.GAME_OVER
        elif self.comp_point == 3:
            self.game_state = GameState.GAME_OVER

        if self.game_state == GameState.ROUND_ACTIVE and self.attack_choice:
            pc_attack = randint(0, 2)
            if pc_attack == 0:
                self.computer_attack_type = AttackType.ROCK
                if self.comp_rock not in self.sprites:
                    self.comp_sprites.append(self.comp_rock)
                self.game_state = GameState.ROUND_DONE
            elif pc_attack == 1:
                self.computer_attack_type = AttackType.PAPER
                if self.comp_paper not in self.sprites:
                    self.comp_sprites.append(self.comp_paper)
                self.game_state = GameState.ROUND_DONE
            else:
                self.computer_attack_type = AttackType.SCISSORS
                if self.comp_scissor not in self.sprites:
                    self.comp_sprites.append(self.comp_scissor)
                self.game_state = GameState.ROUND_DONE

        elif self.game_state == GameState.ROUND_DONE and self.attack_choice:

            if self.player_attack_type == AttackType.ROCK:
                if self.computer_attack_type == AttackType.ROCK:
                    self.game_win = 1
                elif self.computer_attack_type == AttackType.PAPER:
                    self.game_win = 2
                    self.comp_point += 1
                elif self.computer_attack_type == AttackType.SCISSORS:
                    self.game_win = 3
                    self.player_point += 1
            elif self.player_attack_type == AttackType.PAPER:
                if self.computer_attack_type == AttackType.ROCK:
                    self.game_win = 3
                    self.player_point += 1
                elif self.computer_attack_type == AttackType.PAPER:
                    self.game_win = 1
                elif self.computer_attack_type == AttackType.SCISSORS:
                    self.game_win = 2
                    self.comp_point += 1
            elif self.player_attack_type == AttackType.SCISSORS:
                if self.computer_attack_type == AttackType.ROCK:
                    self.game_win = 2
                    self.comp_point += 1
                elif self.computer_attack_type == AttackType.PAPER:
                    self.game_win = 3
                    self.player_point += 1
                elif self.computer_attack_type == AttackType.SCISSORS:
                    self.game_win = 1

            self.attack_choice = False
            self.player_attack_type = AttackType
            self.computer_attack_type = AttackType

    def on_key_press(self, symbol, modifiers):
        """
            Traiter des touches espaces
        """
        if symbol == arcade.key.SPACE:
            if self.game_state == GameState.NOT_STARTED:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.ROUND_DONE:
                self.game_state = GameState.ROUND_ACTIVE
            elif self.game_state == GameState.GAME_OVER:
                self.game_state = GameState.ROUND_ACTIVE
                self.attack_choice = False
                self.player_attack_type = AttackType
                self.computer_attack_type = AttackType
                self.game_win = 0
                self.comp_point = 0
                self.player_point = 0

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        """
            Traiter des touches sur le souris
        """
        if self.game_state == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
                self.attack_choice = True
                self.paper.remove_from_sprite_lists()
                self.scissor.remove_from_sprite_lists()
            elif self.scissor.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS
                self.attack_choice = True
                self.rock.remove_from_sprite_lists()
                self.paper.remove_from_sprite_lists()
            elif self.paper.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
                self.attack_choice = True
                self.rock.remove_from_sprite_lists()
                self.scissor.remove_from_sprite_lists()


def main():
    window = arcade.Window(1280, 720, "Roche Papier Ciseau")
    mygame = MyGame()
    window.show_view(mygame)
    arcade.run()


main()
