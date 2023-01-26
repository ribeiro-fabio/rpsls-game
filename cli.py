import random

from action import Action


class CLI:
    def get_player_action(self) -> Action:
        while True:
            try:
                choices = [f"[{i + 1}]{action}" for i, action in enumerate(Action)]
                selection = int(input(f"Enter a choice {choices}:"))

                if selection in range(1, len(choices) + 1):
                    return list(Action)[selection - 1]
                else:
                    print("That was no valid number. Try again.")
            except ValueError:
                print("You entered something other than a number. Try again.")

    def get_cpu_action(self) -> Action:
        return random.choice(list(Action))

    def display_rules(self):
        pass


cli = CLI()
cli.get_player_action()
