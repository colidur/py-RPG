from classes.game import Person, bcolors

magic = [{'name': 'Fire', 'cost': 10, 'dmg': 60},
         {'name': 'Thunder', 'cost': 10, 'dmg': 60},
         {'name': 'Blizzard', 'cost': 10, 'dmg': 60}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + "AN ENNEMY ATTACKS !" + bcolors.ENDC)

while running:
    print("============================")
    player.choose_action()
    choice = input("Choose your action:")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, ".Player HP:", player.get_hp())

'''bcolors.ENDC est nécessaire à chaque fois qu'on utilise bcolors pour
modifier une string'''
