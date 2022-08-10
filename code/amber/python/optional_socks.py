# SOCK SORTER

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

rando_socks = []

while len(rando_socks) < 100:
  rando_socks.append(random.choice(sock_types))

ankle = 0
crew = 0
calf = 0
thigh = 0

for each in rando_socks:
  if each == 'ankle':
    ankle += 1
  elif each == 'crew':
    crew += 1
  elif each == 'calf':
    calf += 1
  elif each == 'thigh':
    thigh += 1

ankle_pair = ankle // 2
ankle_loose = ankle % 2
crew_pair = crew // 2
crew_loose = crew % 2
calf_pair = calf // 2
calf_loose = calf % 2
thigh_pair = thigh // 2
thigh_loose = thigh % 2
