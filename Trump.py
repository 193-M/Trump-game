class Trump:
    def __init__(self):
        from random import shuffle
        self.suits = ["♤", "♧", "♡", "♢"]
        self.values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.deck = [(suit, value)for suit in self.suits for value in self.values]
        shuffle(self.deck)
    
    def setDeck(self):
        return self.deck
    
    def draw(self, deck):
        return deck.pop()
    
    def change(self, value):
        if value == "A":
            number = 1
        elif value == "J":
            number = 11
        elif value == "Q":
            number = 12
        elif value == "K":
            number = 13
        else:
            number = int(value)
        return number