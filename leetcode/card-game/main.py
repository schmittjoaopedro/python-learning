"""
1. working solution
2. design for extensibility

card game war
2 player card game
deck of 52 cards [1...52]
randomly shuffle deck and deal out evenly to players
on each turn:
- both players turn over top card
- player with higher card wins the turn and gets 2 points (1 point per card)
this continues until players are out of cards
player with mosts points win
tie:
- player that won the highest card throughout the game wins

print which player won
print both players' scores
"""
from typing import List
import random


class Game:
    cards = []
    players = []

    def addCards(self, numCards):  # Add Cards Policy Interface makes sense
        for i in range(1, numCards + 1):
            self.cards.append(Card(i, f"Card {i}"))

    def addPlayers(self, numPlayers):  # Add Player Policy interface
        for i in range(1, numPlayers + 1):
            self.players.append(Player(f"Player {i}"))

    def init(self):  # Possible place to implete an init policy
        shuffled_cards = self.cards.copy()
        random.shuffle(shuffled_cards)
        deckSize = len(shuffled_cards) // len(self.players)
        for i in range(len(self.players)):
            self.players[i].cards = shuffled_cards[i * deckSize:i * deckSize + deckSize]

    def turn(self):
        if len(self.players[0].cards) == 0:
            return False

        turnedCards = []

        # Card selection phase
        for player in self.players:
            card = player.cards.pop()
            turnedCards.append((player, card))
            if not player.highestCard or card.cardId > player.highestCard.cardId:
                player.highestCard = card

        # Compute turn winner
        wonPlayer, wonCard = turnedCards[0]
        for item in turnedCards[1:]:
            player, card = item
            if wonCard.cardId < card.cardId:
                wonPlayer, wonCard = player, card

        # Score computing phase
        wonPlayer.score += len(turnedCards)
        return len(self.players[0].cards) != 0

    def printGameStats(self):
        print([f"{t.score} {len(t.cards)}" for t in self.players])

    def defineWinner(self):
        sortedPlayers = sorted(self.players,
                               key=lambda p: (p.score, p.highestCard.cardId),
                               reverse=True)
        print("Winner:", sortedPlayers[0].name)
        for player in self.players:
            print("Player", player.name, "Score", player.score, "Highest", player.highestCard.cardId)


class Card:
    cardId: int
    name: str

    def __init__(self, cardId, name):
        self.cardId = cardId
        self.name = name


class Player:
    name: str
    cards: List
    highestCard = None
    score = 0

    def __init__(self, name, cards=None):
        self.name = name
        self.cards = cards or []


game = Game()
game.addCards(30)
game.addPlayers(3)
game.init()
while game.turn():
    game.printGameStats()
game.printGameStats()
game.defineWinner()
