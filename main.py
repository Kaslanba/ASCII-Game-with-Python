import random
import time
from warrior import Warrior
from mage import Mage
from archer import Archer
from goblin import Goblin
from orc import Orc
from dragon import Dragon
from vampire import Vampire
from spiderqueen import SpiderQueen

welcome_message = """
    ___                     ___           _         ___                                    
   /   \___  ___ _ __      /   \__ _ _ __| | __    /   \_   _ _ __   __ _  ___  ___  _ __  
  / /\ / _ \/ _ \ '_ \    / /\ / _` | '__| |/ /   / /\ / | | | '_ \ / _` |/ _ \/ _ \| '_ \ 
 / /_//  __/  __/ |_) |  / /_// (_| | |  |   <   / /_//| |_| | | | | (_| |  __/ (_) | | | |
/___,' \___|\___| .__/  /___,' \__,_|_|  |_|\_\ /___,'  \__,_|_| |_|\__, |\___|\___/|_| |_|
                |_|                                                 |___/                   
"""


def fight(character, target):
    select2_answers = ["a", "b", "c", "d", "e"]
    select3_answers = ["hp", "mp", "no"]
    headtails_list = ["head", "tail"]
    print(f"""
            ----------------------------------------------------------------------------------------------------------------
            {target.ascii_alive}
                                                    Name: {target.name}
                                                    Health: {target.health}/{target.max_health}
                                                    Attack: {target.attack}
            ----------------------------------------------------------------------------------------------------------------
            You faced with the {target.name}.
            So, make your choice. Head or Tail?
            ----------------------------------------------------------------------------------------------------------------
            Name: {character.name} - Health: {character.health}/{character.max_health}
            Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
            ----------------------------------------------------------------------------------------------------------------
                        """)
    answer = random.randint(0, 1)
    should_repeat = True
    while should_repeat:
        head_or_tails = input("Which one would you like to select? (Head, Tail): ").lower()
        if head_or_tails not in headtails_list:
            print("Please write 'Head' or 'Tail'")
            continue
        else:
            should_repeat = False
    time.sleep(3)
    if head_or_tails == headtails_list[answer]:
        print(f"""
            ----------------------------------------------------------------------------------------------------------------
            {target.ascii_alive}
                                                    Name: {target.name}
                                                    Health: {target.health}/{target.max_health}
                                                    Attack: {target.attack}
            ----------------------------------------------------------------------------------------------------------------
            You have the first attack! Be wise while choosing your move. You'll need that resources.

            Select your move:
            ----------------------------------------------------------------------------------------------------------------
            Name: {character.name} - Health: {character.health}/{character.max_health}
            Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
            ----------------------------------------------------------------------------------------------------------------
            A-) {character.spells[3][0]} -> Damage: {character.spells[3][1]}
            B-) {character.spells[0][0]} -> Damage: {character.spells[0][1]} Mana: {character.spells[0][2]} 
            C-) {character.spells[1][0]} -> Damage: {character.spells[1][1]} Mana: {character.spells[1][2]}
            D-) {character.spells[2][0]} -> Damage: {character.spells[2][1]} Mana: {character.spells[2][2]}
            E-) Inventory
                        """)
        while not target.is_dead() and not character.is_dead():
            monster_damage = target.attack
            should_repeat = True
            while should_repeat:
                select2 = input("What would you like to do? (A, B, C, D, E): ").lower()
                if select2 not in select2_answers:
                    print("Please write one of (A, B, C, D, E)")
                    continue
                else:
                    should_repeat = False
            if select2 == "a":
                damage = character.attack
            elif select2 == "b":
                if character.type == "warrior":
                    if character.mana >= character.mortal_strike_mana:
                        damage = character.mortal_strike()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.lightning_bolt_mana:
                        damage = character.lightning_bolt()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.penetrating_arrow_mana:
                        damage = character.penetrating_arrow()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "c":
                if character.type == "warrior":
                    if character.mana >= character.shield_bash_mana:
                        damage = character.shield_bash()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.blizzard_mana:
                        damage = character.blizzard()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.aimed_shot_mana:
                        damage = character.aimed_shot()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "d":
                if character.type == "warrior":
                    if character.mana >= character.berserk_mana:
                        damage = character.berserk()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.meteor_strike_mana:
                        damage = character.meteor_strike()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.burst_fire_mana:
                        damage = character.burst_fire()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "e":
                print("Items in your inventory:")
                for item in character.inventory:
                    print(f"{item} - Amount: {character.inventory[item]}")
                should_repeat = True
                while should_repeat:
                    select3 = input("Do you want to use any potion? (HP, MP, No): ").lower()
                    if select3 not in select3_answers:
                        print("Please write one of (HP, MP, No)")
                        continue
                    else:
                        should_repeat = False
                if select3 == "hp":
                    if character.inventory["Health Potion"] > 0:
                        if character.health == character.max_health:
                            print("Your health is full. You can't use health potion!")
                        else:
                            character.addHealth(20)
                            print(f"Used health potion! New health: {character.health}")
                            character.remove_item("Health Potion", 1)
                            if character.health > character.max_health:
                                character.health = character.max_health
                    else:
                        print("Do not have enough potion to use.")
                elif select3 == "mp":
                    if character.inventory["Mana Potion"] > 0:
                        if character.mana == character.max_mana:
                            print("Your mana is full. You can't use mana potion!")
                        else:
                            character.addMana(20)
                            print(f"Used mana potion! New mana: {character.mana}")
                            character.remove_item("Mana Potion", 1)
                            if character.mana > character.max_mana:
                                character.mana = character.max_mana
                    else:
                        print("Do not have enough potion to use.")
                continue
            target.take_damage(damage)
            character.addMana(10)
            if character.mana > character.max_mana:
                character.mana = character.max_mana
            if not target.is_dead():
                character.take_damage(monster_damage)
            print(f"""
                ----------------------------------------------------------------------------------------------------------------
                {target.ascii_alive}
                                                        Name: {target.name}
                                                        Health: {target.health}/{target.max_health}
                                                        Attack: {target.attack}
                ----------------------------------------------------------------------------------------------------------------
                You dealt {damage} damage to the {target.name}!
                {target.name} dealt {monster_damage} damage to you!

                Select your next move:
                ----------------------------------------------------------------------------------------------------------------
                Name: {character.name} - Health: {character.health}/{character.max_health}
                Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
                ----------------------------------------------------------------------------------------------------------------
                A-) {character.spells[3][0]} -> Damage: {character.spells[3][1]}
                B-) {character.spells[0][0]} -> Damage: {character.spells[0][1]} Mana: {character.spells[0][2]} 
                C-) {character.spells[1][0]} -> Damage: {character.spells[1][1]} Mana: {character.spells[1][2]}
                D-) {character.spells[2][0]} -> Damage: {character.spells[2][1]} Mana: {character.spells[2][2]}
                E-) Inventory
                            """)
            if target.is_dead():
                target.health = 0
                print(f"""
                    ----------------------------------------------------------------------------------------------------------------
                    {target.ascii_dead}
                                                            Name: {target.name}
                                                            Health: {target.health}/{target.max_health}
                                                            Attack: {target.attack}
                    ----------------------------------------------------------------------------------------------------------------
                    You killed the {target.name}!
                    Here is your reward:
                    {target.inventory}
                    ----------------------------------------------------------------------------------------------------------------
                    Name: {character.name} - Health: {character.health}/{character.max_health}
                    Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
                    ----------------------------------------------------------------------------------------------------------------
                                """)

                for item in target.inventory:
                    character.add_item(item, target.inventory[item])

    else:
        monster_damage = target.attack
        character.take_damage(monster_damage)
        print(f"""
            ----------------------------------------------------------------------------------------------------------------
            {target.ascii_alive}
                                                    Name: {target.name}
                                                    Health: {target.health}/{target.max_health}
                                                    Attack: {target.attack}
            ----------------------------------------------------------------------------------------------------------------
            {target.name} attacks first! Dealt {monster_damage} damage to you!
            ----------------------------------------------------------------------------------------------------------------
            Name: {character.name} - Health: {character.health}/{character.max_health}
            Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
            ----------------------------------------------------------------------------------------------------------------
            A-) {character.spells[3][0]} -> Damage: {character.spells[3][1]}
            B-) {character.spells[0][0]} -> Damage: {character.spells[0][1]} Mana: {character.spells[0][2]} 
            C-) {character.spells[1][0]} -> Damage: {character.spells[1][1]} Mana: {character.spells[1][2]}
            D-) {character.spells[2][0]} -> Damage: {character.spells[2][1]} Mana: {character.spells[2][2]}
            E-) Inventory
                        """)
        while not target.is_dead() and not character.is_dead():
            should_repeat = True
            while should_repeat:
                select2 = input("What would you like to do? (A, B, C, D, E): ").lower()
                if select2 not in select2_answers:
                    print("Please write one of (A, B, C, D, E)")
                    continue
                else:
                    should_repeat = False
            if select2 == "a":
                damage = character.attack
            elif select2 == "b":
                if character.type == "warrior":
                    if character.mana >= character.mortal_strike_mana:
                        damage = character.mortal_strike()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.lightning_bolt_mana:
                        damage = character.lightning_bolt()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.penetrating_arrow_mana:
                        damage = character.penetrating_arrow()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "c":
                if character.type == "warrior":
                    if character.mana >= character.shield_bash_mana:
                        damage = character.shield_bash()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.blizzard_mana:
                        damage = character.blizzard()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.aimed_shot_mana:
                        damage = character.aimed_shot()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "d":
                if character.type == "warrior":
                    if character.mana >= character.berserk_mana:
                        damage = character.berserk()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "mage":
                    if character.mana >= character.meteor_strike_mana:
                        damage = character.meteor_strike()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
                elif character.type == "archer":
                    if character.mana >= character.burst_fire_mana:
                        damage = character.burst_fire()
                    else:
                        print("Not enough mana! Try another move.")
                        continue
            elif select2 == "e":
                print("Items in your inventory:")
                for item in character.inventory:
                    print(f"{item} - Amount: {character.inventory[item]}")
                should_repeat = True
                while should_repeat:
                    select3 = input("Do you want to use any potion? (HP, MP, No): ").lower()
                    if select3 not in select3_answers:
                        print("Please write one of (HP, MP, No)")
                        continue
                    else:
                        should_repeat = False
                if select3 == "hp":
                    if character.inventory["Health Potion"] > 0:
                        if character.health == character.max_health:
                            print("Your health is full. You can't use health potion!")
                        else:
                            character.addHealth(20)
                            print(f"Used health potion! New health: {character.health}")
                            character.remove_item("Health Potion", 1)
                            if character.health > character.max_health:
                                character.health = character.max_health
                    else:
                        print("Do not have enough potion to use.")
                elif select3 == "mp":
                    if character.inventory["Mana Potion"] > 0:
                        if character.mana == character.max_mana:
                            print("Your mana is full. You can't use mana potion!")
                        else:
                            character.addMana(20)
                            print(f"Used mana potion! New mana: {character.mana}")
                            character.remove_item("Mana Potion", 1)
                            if character.mana > character.max_mana:
                                character.mana = character.max_mana
                continue
            target.take_damage(damage)
            character.addMana(10)
            if character.mana > character.max_mana:
                character.mana = character.max_mana
            if not target.is_dead():
                character.take_damage(monster_damage)
                print(f"""
                    ----------------------------------------------------------------------------------------------------------------
                    {target.ascii_alive}
                                                            Name: {target.name}
                                                            Health: {target.health}/{target.max_health}
                                                            Attack: {target.attack}
                    ----------------------------------------------------------------------------------------------------------------
                    You dealt {damage} damage to the {target.name}!
                    {target.name} dealt {target.attack} damage to you!
    
                    Select your next move:
                    ----------------------------------------------------------------------------------------------------------------
                    Name: {character.name} - Health: {character.health}/{character.max_health}
                    Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
                    ----------------------------------------------------------------------------------------------------------------
                    A-) {character.spells[3][0]} -> Damage: {character.spells[3][1]}
                    B-) {character.spells[0][0]} -> Damage: {character.spells[0][1]} Mana: {character.spells[0][2]} 
                    C-) {character.spells[1][0]} -> Damage: {character.spells[1][1]} Mana: {character.spells[1][2]}
                    D-) {character.spells[2][0]} -> Damage: {character.spells[2][1]} Mana: {character.spells[2][2]}
                    E-) Inventory
                                """)
            if target.is_dead():
                target.health = 0
                print(f"""
                    ----------------------------------------------------------------------------------------------------------------
                    {target.ascii_dead}
                                                            Name: {target.name}
                                                            Health: {target.health}/{target.max_health}
                                                            Attack: {target.attack}
                    ----------------------------------------------------------------------------------------------------------------
                    You killed the {target.name}!
                    Here is your reward:
                    {target.inventory}
                    ----------------------------------------------------------------------------------------------------------------
                    Name: {character.name} - Health: {character.health}/{character.max_health}
                    Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
                    ----------------------------------------------------------------------------------------------------------------
                                """)

                for item in target.inventory:
                    character.add_item(item, target.inventory[item])


def enter_dungeon(character):
    print(welcome_message)
    time.sleep(2)
    print(f"Welcome to the Deep Dark Dungeon {character.name}!")
    time.sleep(2)
    print("In the dungeon, there are several types of monsters as we know from the notes of previous adventurers")
    time.sleep(3)
    print("And there are rumors that says powerful bosses walks around the dungeon.")
    time.sleep(2)
    print("You will fight and slay them until you die.")
    time.sleep(5)
    print("Ehm, maybe an exit from the dungeon exists... Who knows!")
    time.sleep(2)
    print("Enough talking.")
    print(f"Good luck on your adventure {character.name}!")
    time.sleep(3)
    print("Little Note: In the dungeon, fights are turn based and first striker concluded with head or tails game.")
    time.sleep(2)
    print("Also, after every turn, you regenerate 10 mana.")
    time.sleep(5)

    treasure_chest = {"Health Potion": 1, "Mana Potion": 1}

    goblin = Goblin('Goblin', 150, 15, {"Health Potion": 2, "Mana Potion": 2})
    orc = Orc('Orc', 200, 20, {'Health Potion': 3, 'Mana Potion': 2})
    spider_queen = SpiderQueen('Spider Queen', 200, 40, {'Health Potion': 4, 'Mana Potion': 4})
    vampire = Vampire('Vampire', 300, 35, {'Health Potion': 5, 'Mana Potion': 5})
    dragon = Dragon('Dragon', 350, 50)

    monsters = [goblin, orc, spider_queen, vampire, dragon]

    select1_answers = ["left", "right"]

    print(f"""
        ----------------------------------------------------------------------------------------------------------------
                                        Name: {character.name} - Health: {character.health}/{character.max_health}
                                        Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
        ----------------------------------------------------------------------------------------------------------------
                                    |.'',                                     ,''.|       
                                    |.'.'',                                 ,''.'.|
                                    |.'.'.'',                             ,''.'.'.|
                                    |.'.'.'.'',                         ,''.'.'.'.|
                                    |.'.'.'.'.|                         |.'.'.'.'.|
                                    |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
                                    |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
                                    |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
                                    |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
                                    |,',',',',|---|',|'|???????|'|,'|---|,',',',',|
                                    |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
                                    |.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
                                    |.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
                                    |.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
                                    |.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
                                    |.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
                                    |.'.','         /%%%%%%%%%%%%%\         ','.'.|
                                    |.','          /%%%%%%%%%%%%%%%\          ','.|
                                    |;____________/%%%%%      %%%%%%\____________;|
        ----------------------------------------------------------------------------------------------------------------
        While walking, you came to end of the road. There are two options for you, left or right. Which path do you want
        to select and build your adventure on?
        ----------------------------------------------------------------------------------------------------------------
        """)
    time.sleep(2)
    should_repeat = True
    while should_repeat:
        select1 = input("Which way do you want to go (Left or Right): ").lower()
        if select1 not in select1_answers:
            print("Please write 'Left' or 'Right'")
        else:
            should_repeat = False

    time.sleep(3)
    if select1 == "left":
        target = monsters[0]
        fight(character, target)

    if select1 == "right":
        print(f"""
        ----------------------------------------------------------------------------------------------------------------
                                                            _.--.
                                                        _.-'_:-'||
                                                    _.-'_.-::::'||
                                               _.-:'_.-::::::'  ||
                                             .'`-.-:::::::'     ||
                                            /.'`;|:::::::'      ||_
                                           ||   ||::::::'     _.;._'-._
                                           ||   ||:::::'  _.-!oo @.!-._'-.
                                           .  ||:::::.-!()oo @!()@.-'_.|
                                            '.'-;|:.-'.&$@.& ()$%-'o.'\||
                                              `>'-.!@%()@'@_%-'_.-o _.|'||
                                               ||-._'-.@.-'_.-' _.-o  |'||
                                               ||=[ '-._.--'    o |'||
                                               || '-.]=|| |'|      o  |'||
                                               ||      || |'|        _| ';
                                               ||      || |'|    _.-'_.-'
                                               |'-._   || |'|_.-'_.-'
                                                '-._'-.|| |' `_.-'
                                                    '-.||_/.-'
        ----------------------------------------------------------------------------------------------------------------
        Lucky you! Chose the correct way and found the treasure!
        Here is your loot: 
                """)
        for item in treasure_chest:
            print("    ", item)
        print("""
        ----------------------------------------------------------------------------------------------------------------
        """)
        for item in treasure_chest:
            character.add_item(item, treasure_chest[item])

    print("You're walking through the corridor...")
    time.sleep(10)

    print("After passing from the gate, you ended up in a room with a sacred door in it.")
    time.sleep(2)
    print("You went near the door with silent steps.")
    time.sleep(2)
    print("Angry breathing sounds were coming from inside.")
    time.sleep(2)
    print("After getting enough encouragement, you suddenly opened the door!")

    target = monsters[1]
    fight(character, target)

    if not character.is_dead():
        print("Well, you've proved the power of the blood that flows in your veins.")
        time.sleep(2)
        print("Just saying, there was some rumors that says this dungeon is alive.")
        time.sleep(2)
        print("It increases power of the monsters after every room you pass.")
        time.sleep(2)
        print("Be careful about your future fights, true form of the dungeon just appeared!")
        time.sleep(5)

        print(f"""
            Some of your stats are updated.
            New Health:{character.health} / {character.max_health}
            New Mana: {character.mana} / {character.max_mana}
        """)

        character.set_health(character.health + 50)
        character.set_maxhealth(character.max_health + 50)
        character.set_mana(character.mana + 50)
        character.set_maxmana(character.max_mana + 50)

        target = monsters[2]
        fight(character, target)

    if not character.is_dead():
        print("Can you hear the sounds?!?.")
        time.sleep(2)
        print("Some crying sounds coming from the deeps of the dungeon.")
        time.sleep(5)
        print("You will learn the meaning of this very soon.")
        time.sleep(2)
        print("Just do what you doing. And keep staying alive!")
        time.sleep(5)

        target = monsters[3]
        fight(character, target)

    if not character.is_dead():
        print("Unresistable heat comes from end of the corridor")
        time.sleep(2)
        print("You sense the danger")
        time.sleep(2)
        print("But..No one can interrupt you from entering the final room")
        time.sleep(2)
        print("This...this is the true form of your spirit")
        time.sleep(2)
        print("Let's go adventurer! Final fight for your life")
        time.sleep(5)

        target = monsters[4]
        fight(character, target)
        if not character.is_dead():
            time.sleep(3)

            print(f"""    
                                    /\_/\___  _   _  / / /\ \ (_)_ __  
                                    \_ _/ _ \| | | | \ \/  \/ / | '_ 
                                     / \ (_) | |_| |  \  /\  /| | | | |
                                     \_/\___/ \__,_|   \/  \/ |_|_| |_|
    
                                Good luck on your next adventures {character.name}!
                            """)

    if character.is_dead():
        character.health = 0
        print(f"""
        ----------------------------------------------------------------------------------------------------------------
                                        Name: {character.name} - Health: {character.health}/{character.max_health}
                                        Attack: {character.attack} - Mana: {character.mana}/{character.max_mana}
        ----------------------------------------------------------------------------------------------------------------
                                                 _____  _____
                                                <     `/     |
                                                 >          (
                                                |   _     _  |
                                                |  |_) | |_) |
                                                |  | \ | |   |
                                                |            |
                                 ______.______%_|            |__________  _____
                               _/                                       \|     |
                              |                   {character.name}             <
                              |_____.-._________              ____/|___________|
                                                | * fi/ll/in |
                                                | + 19/10/97 |
                                                |            |
                                                |            |
                                                |   _        <
                                                |__/         |
                                                 / `--.      |
                                               %|            |%
                                           |/.%%|          -< @%%%
                                           `\%`@|     v      |@@%@%%
                                         .%%%@@@|%    |    % @@@%%@%%%%
                                    _.%%%%%%@@@@@@%%_/%\_%@@%%@@@@@@@%%%%%%
        ----------------------------------------------------------------------------------------------------------------
        The {target.name} hit you so hard.
        Rest in peace {character.name}...
        ----------------------------------------------------------------------------------------------------------------
                    """)


char_name = input("Enter your character's name: ")
char_class_list = ["warrior", "mage", "archer"]
should_repeat = True
while should_repeat:
    char_class = input("Enter class of your character (Warrior, Mage, Archer): ").lower()
    if char_class not in char_class_list:
        print("Please write one of (Warrior, Mage, Archer)")
        continue
    else:
        should_repeat = False
for x in range(0, 5):
    print("-")
    time.sleep(0.5)
time.sleep(2)
if char_class == "warrior":
    character = Warrior(char_name)
elif char_class == "mage":
    character = Mage(char_name)
elif char_class == "archer":
    character = Archer(char_name)
print("Your character has been created!")
enter_dungeon(character)
