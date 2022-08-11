# SOCK SORTER V.2

import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

sock_colors = ['black', 'white', 'blue']

rando_socks = []

while len(rando_socks) < 100:
  color_type = [random.choice(sock_types), random.choice(sock_colors)]
  rando_socks.append(color_type)

black_ankle = 0
white_ankle = 0
blue_ankle = 0

black_crew = 0
white_crew = 0
blue_crew = 0

black_calf = 0
white_calf = 0
blue_calf = 0

black_thigh = 0
white_thigh = 0
blue_thigh = 0

for each in rando_socks:
  if 'ankle' in each and 'black' in each:
    black_ankle += 1
  elif 'ankle' in each and 'white' in each:
    white_ankle += 1
  elif 'ankle' in each and 'blue' in each:
    blue_ankle += 1

  elif 'crew' in each and 'black' in each:
    black_crew += 1
  elif 'crew' in each and 'white' in each:
    white_crew += 1
  elif 'crew' in each and 'blue' in each:
    blue_crew += 1

  elif 'calf' in each and 'black' in each:
    black_calf += 1
  elif 'calf' in each and 'white' in each:
    white_calf += 1
  elif 'calf' in each and 'blue' in each:
    blue_calf += 1

  elif 'thigh' in each and 'black' in each:
    black_thigh += 1
  elif 'thigh' in each and 'white' in each:
    white_thigh += 1
  elif 'thigh' in each and 'blue' in each:
    blue_thigh += 1

sock_dict = {
  'black_ankle': {'pairs': black_ankle // 2,
                  'loose': black_ankle % 2
  },
  'white_ankle': {'pairs': white_ankle // 2,
                  'loose': white_ankle % 2
  },
  'blue_ankle': {'pairs': blue_ankle // 2,
                 'loose': blue_ankle % 2
  },

  'black_crew': {'pairs': black_crew // 2,
                 'loose': black_crew % 2
  },
  'white_crew': {'pairs': white_crew // 2,
                 'loose': white_crew % 2
  },
  'blue_crew': {'pairs': blue_crew // 2,
                'loose': blue_crew % 2
  },

  'black_calf': {'pairs': black_calf // 2,
                 'loose': black_calf % 2
  },
  'white_calf': {'pairs': white_calf // 2,
                 'loose': white_calf % 2
  },
  'blue_calf': {'pairs': blue_calf // 2,
                'loose': blue_calf % 2
  },

  'black_thigh': {'pairs': black_thigh // 2,
                  'loose': black_thigh % 2
  },
  'white_thigh': {'pairs': white_thigh // 2,
                  'loose': white_thigh % 2
  },
  'blue_thigh': {'pairs': blue_thigh // 2,
                 'loose': blue_thigh % 2
  }
}

'''
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

sock_dict = {
  'ankle': {'pairs': ankle_pair,
            'loose': ankle_loose,
            'total': ankle},
  'crew': {'pairs': crew_pair,
            'loose': crew_loose,
            'total': crew},
  'calf': {'pairs': calf_pair,
            'loose': calf_loose,
            'total': calf},
  'thigh': {'pairs': thigh_pair,
            'loose': thigh_loose,
            'total': thigh}
}

print(f'''#\n
#Ankle: {sock_dict["ankle"]}\n
#Crew: {sock_dict["crew"]}\n
#Calf: {sock_dict["calf"]}\n
#Thigh: {sock_dict["thigh"]}\n
''')
'''
