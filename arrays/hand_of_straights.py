


def isStaightHand(hand, W):
    if len(hand) % W != 0:
        return False
    hand = sorted(hand)

