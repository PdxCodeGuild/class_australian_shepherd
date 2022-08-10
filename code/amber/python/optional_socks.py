# SOCK SORTER

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

rando_socks = []

while len(rando_socks) < 100:
  rando_socks.append(random.choice(sock_types))
