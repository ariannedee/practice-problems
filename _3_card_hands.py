"""
Deal a hand of 5 cards.
"""
suits = ['♠︎', '♣︎', '♥︎', '♦︎']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Create deck of cards
cards = []

assert len(cards) == 52, f"There were {len(cards)} cards in the deck"

# Deal 5 random cards
hand = []

assert len(hand) == 5, f"There were {len(hand)} cards in the hand"
assert len(cards) == 47, f"There should be 5 fewer cards in the deck after dealing, {len(cards)} != 47"

print(hand)
