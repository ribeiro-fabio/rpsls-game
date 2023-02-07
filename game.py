from cli import CLI
from rules import Rules


class Game:
    def __init__(self) -> None:
        self.cli = CLI()
        self.rules = Rules()

    def turn(self):
        # separar lógica do jogo da chamada do jogo
        player_name = self.cli.get_player_name()
        cpu = "CPU"

        self.cli.display_player_action()

        player_action = self.cli.get_player_action()
        cpu_action = self.cli.get_cpu_action()

        winner = self.rules.get_winner(player_action, cpu_action)
        self.cli.display_round(player_name, cpu, player_action, cpu_action)

        if winner == player_action:
            self.cli.display_winner(player_name, winner)
        elif winner == cpu_action:
            self.cli.display_winner(cpu, winner)
        else:
            self.cli.display_tie()

    def play(self):
        self.cli.display_opening_message()
        self.cli.display_rules()
        turns = 3
        try:
                play_again = input("Play again? (y/n): ")
                print("")
                if play_again.lower() != "y":
                    break
            except ValueError:
                print("Please enter y or n.")
