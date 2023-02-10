from action import Action


class Rules:
    __VICTORIES = {
        Action.ROCK: {Action.SCISSORS, Action.LIZARD},
        Action.PAPER: {Action.ROCK, Action.SPOCK},
        Action.SCISSORS: {Action.PAPER, Action.LIZARD},
        Action.LIZARD: {Action.PAPER, Action.SPOCK},
        Action.SPOCK: {Action.ROCK, Action.SCISSORS},
    }

    @classmethod
    def get_winner(cls, action1: Action, action2: Action):
        if action1 in Rules.__VICTORIES[action2]:
            return action2
        elif action2 in Rules.__VICTORIES[action1]:
            return action1
        else:
            return None, "It's a tie"
