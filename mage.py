from player import Player


class Mage(Player):
    type = "mage"
    spells = [("Lightning Bolt", "75", "25"), ("Blizzard", "87.5", "35"), ("Meteor Strike", "125", "40"),
              ("Normal Attack", "50")]

    def __init__(self, name, health=0, attack=0, mana=0):
        Player.__init__(self, name)
        self.health = 60
        self.max_health = 60
        self.attack = 50
        self.mana = 70
        self.max_mana = 70

        self.lightning_bolt_mana = 25
        self.blizzard_mana = 35
        self.meteor_strike_mana = 40

    def lightning_bolt(self):
        self.mana -= 25
        print(f"{self.name} used Lightning Bolt!")
        return self.attack * 1.5

    def blizzard(self):
        self.mana -= 35
        print(f"{self.name} used Blizzard!")
        return self.attack * 1.75

    def meteor_strike(self):
        self.mana -= 40
        print(f"{self.name} used Meteor Strike!")
        return self.attack * 2.5