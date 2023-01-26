from enum import Enum


class Action(Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"
    LIZARD = "Lizard"
    SPOCK = "Spock"

    def __str__(self) -> str:
        return self.value
