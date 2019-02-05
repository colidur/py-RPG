from classes.game import Person, bcolors
from classes.magic import Spell


#Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

#Instantiate People
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(bcolors.FAIL + "AN ENNEMY ATTACKS !" + bcolors.ENDC)

while running:
    print("============================")
    player.choose_action()
    index = int(input("Choose your action: ")) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.", 
              enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
    
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()
    
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
              "points of damage." + bcolors.ENDC)
        
    
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "\n")

    print("-------------------------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + 
          str(enemy.get_max_hp()) + bcolors.ENDC + "\n")
    
    print("Your HP: ", bcolors.OKGREEN + str(player.get_hp()) + "/" + 
          str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(player.get_mp()) + "/" + 
          str(player.get_max_mp()) + bcolors.ENDC +"\n")

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You loose, GAME OVER" + bcolors.ENDC)
        running = False
    