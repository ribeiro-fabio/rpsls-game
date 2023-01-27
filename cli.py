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
                    print("That was no valid number. Try again.")
            except ValueError:
                print("You entered something other than a number. Try again.")

    def get_cpu_action(self) -> Action:
        return random.choice(self.ACTIONS)

    def display_player_action(self) -> None:
        choices = [f"[{i + 1}]{action}" for i, action in enumerate(self.ACTIONS)]
        print(f"Valid actions: {choices}")

    def display_rules(self) -> None:
        print("***The Rules: Scissors cuts Paper, Paper covers Rock,")
        print("Rock crushes Lizard, Lizard poisons Spock,")
        print("Spock smashes Scissors, Scissors decapitates Lizard,")
        print("Lizard eats Paper, Paper disproves Spock,")
        print("Spock vaporizes Rock, (and as it always has) Rock crushes Scissors.")
        print("")
        input("Press Enter to continue... ")

    def display_opening_message(self) -> None:
        print("****************************************************")
        print("Welcome to the Rock, Paper, Scissors, Lizard, Spock!")
        print("****************************************************")
        print("")


cli = CLI()
cli.display_opening_message()
cli.display_rules()
cli.display_player_action()
cli.get_player_action()
