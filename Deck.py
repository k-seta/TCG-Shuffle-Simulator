#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random
import numpy as np
import matplotlib.pyplot as plt


class Deck:
    n = 0  # The number of cards in a deck
    order = []
    order_init = []

    def __init__(self, n):
        self.n = n
        self.order = range(n)
        self.order_init = list(self.order)

    def reset(self):
        self.order = list(self.order_init)

    def shuffle_rand(self):
        # Mersenne Twister
        random.shuffle(self.order)
        return self

    def shuffle_pile(self, n):
        tmp = []
        for i in range(n):
            tmp.append(self.order[i::n])
        random.shuffle(tmp)
        order = []
        for x in tmp:
            order.extend(x)
        self.order = order
        return self

    def shuffle_hindu(self, h):
        order = []
        end = self.n
        while True:
            cut = h + random.randint(-3, 3)
            if cut < end:
                start = end - cut
                order.extend(self.order[start:end])
                end = start
            else:
                order.extend(self.order[:end])
                break
        self.order = order
        return self

    def shuffle_faro(self):
        # Gilbert–Shannon–Reeds model
        init_packets = [random.randint(0, 1) for i in range(self.n)]
        first_packet_size = init_packets.count(0)
        first_packet = self.order[:first_packet_size]
        second_packet = self.order[first_packet_size:]
        order = []
        while True:
            first_packet_size = len(first_packet)
            second_packet_size = len(second_packet)
            if first_packet_size > 0 and second_packet_size > 0:
                if random.randint(1, first_packet_size+second_packet_size) <= first_packet_size:
                    order.append(first_packet.pop(0))
                else:
                    order.append(second_packet.pop(0))
            else:
                order.extend(first_packet)
                order.extend(second_packet)
                break
        self.order = order
        return self

    def show(self, title=None):
        x = np.array(self.order_init)
        y = np.array(self.order)

        if title == None:
            plt.title("The Order of the Shuffled Deck")
        else:
            plt.title(title)
        plt.xlabel("initial order")
        plt.ylabel("shuffled order")
        plt.grid(True)
        plt.scatter(x, y)
        plt.show()
