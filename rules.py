from action import Action


class Rules:
    victories = {
        Action.ROCK: {Action.SCISSORS, Action.LIZARD},
        Action.PAPER: {Action.ROCK, Action.SPOCK},
        Action.SCISSORS: {Action.PAPER, Action.LIZARD},
        Action.LIZARD: {Action.PAPER, Action.SPOCK},
        Action.SPOCK: {Action.ROCK, Action.SCISSORS},
    }

    @staticmethod
    def get_winner(action1: Action, action2: Action):
        if action1 in Rules.victories[action2]:
            return action2
        elif action2 in Rules.victories[action1]:
            return action1
        else:
            return None, "It's a tie"