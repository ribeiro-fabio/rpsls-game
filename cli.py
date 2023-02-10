import random

from action import Action


class CLI:
    ACTIONS = list(Action)

    def get_player_action(self) -> Action:
        while True:
            try:
                selection = int(input("Enter a choice: "))
                if selection in range(1, len(self.ACTIONS) + 1):
                    return self.ACTIONS[selection - 1]
                else:
                    print("Invalid input. Enter a valid number.")
            except ValueError:
                print("You entered something other than a number. Try again.")

    def get_cpu_action(self) -> Action:
        return random.choice(self.ACTIONS)

    def get_player_name(self) -> str:
        player_name = input("Enter your name: ")
        return player_name.strip()

    def display_player_action(self) -> None:
        choices = [f"[{i}]{action}" for i, action in enumerate(self.ACTIONS, start=1)]
        print(f"Valid actions: {choices}")

    def display_tie(self) -> None:
        print("*** It's a tie *** \n")

    def display_winner(self, winner_name, winner_action) -> None:
        print(f"*** [{winner_name}] -> {winner_action} wins! *** \n")

    def display_round(self, player_name, cpu, player_action, cpu_action) -> None:
        print(f"\n*** [{player_name}] {player_action} x [{cpu}] {cpu_action} ***\n")

    def display_rules(self) -> None:
        print("*** The Rules: Scissors cuts Paper, Paper covers Rock,")
        print("Rock crushes Lizard, Lizard poisons Spock,")
        print("Spock smashes Scissors, Scissors decapitates Lizard,")
        print("Lizard eats Paper, Paper disproves Spock,")
        print("Spock vaporizes Rock, (and as it always has) Rock crushes Scissors.\n")
        input("Press Enter to continue... ")
        print("")

    def display_opening_message(self) -> None:
        print("****************************************************")
        print("Welcome to the Rock, Paper, Scissors, Lizard, Spock!")
        print("****************************************************")
        print("")
