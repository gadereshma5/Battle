from classes.game import person,bcolors

magic=[{"name":"fire","cost":10,"dmg":60},{"name":"thunder","cost":10,"dmg":60},{"name":"dlizzard","cost":10,"dmg":60}]

player=person(460,65,60,34,magic)
print(player.generate_spell(0))
print(player.generate_spell(1))

