from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

#Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")


#Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 500)

elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hielixer = Item("MegaElixer", "elixer", "Fully restores HP/MP party's member", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


#Create inventory
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion, "quantity":5},
                {"item": superpotion, "quantity":5}, {"item": elixer, "quantity":5},
                {"item": hielixer, "quantity": 2}, {"item": grenade, "quantity":5}]


#Instantiate People
player = Person(460, 65, 60, 34, player_spells, player_items)
enemy = Person(1200, 65, 45, 25, [], [])

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
        print(bcolors.OKGREEN + "You attacked for", dmg, "points of damage" + bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
    
        if magic_choice == -1:
            continue
        
        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()
        
        current_mp = player.get_mp()
    
        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
       
        player.reduce_mp(spell.cost)
        
        if spell.magic_type == "White":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", 
                  str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.magic_type == "Black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg),
                  "points of damage" + bcolors.ENDC)
    
    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1
        
        if item_choice == -1:
            continue
        
        item = player.items[item_choice]["item"]
        
        if player.items[item_choice]["quantity"] == 0:
            print(bcolors.FAIL + "\n" + "None left" + bcolors.ENDC)
            continue
            
        player.items[item_choice]["quantity"] -= 1
        
        if item.item_type == "potion":
            player.heal(item.prop)
            print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop),
                  "HP" +bcolors.ENDC)
        elif item.item_type == "elixer":
            player.hp = player.maxhp
            player.mp = player.maxmp
            print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
        elif item.item_type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.OKBLUE + "\n" + item.name + " deals", str(item.prop), "points of damage" + bcolors.ENDC)
            
    
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print(bcolors.FAIL + "Enemy attacks for", enemy_dmg, "\n" + bcolors.ENDC)

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
    