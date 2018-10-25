#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Deck import Deck

if __name__ == "__main__":
    deck = Deck(60)
    deck.show("No Shuffle")

    deck.shuffle_hindu(10)
    deck.show("Hindu Shuffle")

    deck.reset()
    deck.shuffle_pile(8)
    deck.show("Pile Shuffle")

    deck.reset()
    deck.shuffle_faro()
    deck.show("Faro Shuffle")
