class Creature:

    def __init__(self, name, health=0, attack=0, inventory={}):
        self.inventory = inventory
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack

    def attack(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= damage

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False
