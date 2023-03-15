from creature import Creature


class Player(Creature):
    def __init__(self, name, health=0, attack=0, mana=0, inventory={}):
        Creature.__init__(self, name, health, attack)
        self.mana = mana
        self.max_mana = mana
        self.inventory = {"Health Potion": 2,
                          "Mana Potion": 2,
                          }

    def add_item(self, item, amount):
        if item in self.inventory:
            initial_amount = self.inventory[item]
            self.inventory[item] = initial_amount + amount
        else:
            self.inventory[item] = amount

    def remove_item(self, item, amount):
        initial_amount = self.inventory[item]
        self.inventory[item] = initial_amount - amount

    def addHealth(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def addMana(self, amount):
        self.mana += amount
        if self.mana > self.max_mana:
            self.mana = self.max_mana

    def set_health(self, value):
        self.health = value

    def set_mana(self, value):
        self.mana = value

    def set_maxhealth(self, value):
        self.max_health = value

    def set_maxmana(self, value):
        self.max_mana = value



