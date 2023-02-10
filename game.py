from cli import CLI
from rules import Rules


class Game:
    rules = Rules()
    cli = CLI()

    def __init__(self):
        self.player_name = ""
        self.cpu = "CPU"

    def turn(self):

        self.cli.display_player_action()

        player_action = self.cli.get_player_action()
        cpu_action = self.cli.get_cpu_action()

        winner = Rules.get_winner(player_action, cpu_action)
        self.cli.display_round(self.player_name, self.cpu, player_action, cpu_action)

        if winner == player_action:
            self.cli.display_winner(self.player_name, winner)
        elif winner == cpu_action:
            self.cli.display_winner(self.cpu, winner)
        else:
            self.cli.display_tie()

    def play(self):
        self.cli.display_opening_message()
        self.cli.display_rules()
        self.player_name = self.cli.get_player_name()
        self.turn()

        while True:
            play_again = input("Play again? (y/n): ")
            if play_again.lower() not in ("y", "n"):
                print("Invalid input. Enter y or n")
            elif play_again.lower() == "y":
                self.turn()
            else:
                print("Goodbye!")
                break
