import random


class Deck:

    def __init__(self):
        self.suits = ["spades", "clubs", "hearts", "diamonds"]
        self.ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        if len(self.cards) > 1 :
            random.shuffle(self.cards)


    def deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if len(self.cards) > 0 :
                card = self.cards.pop()
                cards_dealt.append(card)

        return cards_dealt


deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print('*'*20)
print(deck2.cards)

# if rank == "A":
#         value = 11
# elif rank in ["J", "Q", "K"]:
#     value = 10
# else:
#     value = rank