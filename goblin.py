from creature import Creature


class Goblin(Creature):
    def __init__(self, name, health, attack, inventory):
        Creature.__init__(self, name, health, attack, inventory)


    ascii_alive = """
                                                         ,      ,
                                                        /(.-""-.)\_
                                                    |\  \/      \/  /|              
                                                    | \ / =.  .= \ / |              
                                                    \( \   o\/o   / )/              
                                                     \_, '-/  \-' ,_/
                                                       /   \__/   \_
                                                       \ \__/\__/ /
                                                     ___\ \|--|/ /___
                                                   /`    \      /    `\_
                                                  /       '----'       \_
    """

    ascii_dead = """
                                                         ,      ,
                                                        /(.-""-.)\_
                                                    |\  \/      \/  /|
                                                    | \ / =.  .= \ / |
                                                    \( \   X\/X   / )/
                                                     \_, '-/  \-' ,_/
                                                       /   \__/   \_
                                                       \ \__/\__/ /
                                                     ___\ \|--|/ /___
                                                   /`    \      /    `\_
                                                  /       '----'       \_
"""
