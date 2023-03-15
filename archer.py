from player import Player


class Archer(Player):
    type = "archer"
    spells = [("Penetrating Arrow", "60", "20"), ("Aimed Shot", "100", "40"), ("Burst Fire", "70", "35"),
              ("Normal Attack", "40")]

    def __init__(self, name, health=0, attack=0, mana=0):
        Player.__init__(self, name)
        self.health = 80
        self.max_health = 80
        self.attack = 40
        self.mana = 50
        self.max_mana = 50

        self.penetrating_arrow_mana = 20
        self.aimed_shot_mana = 40
        self.burst_fire_mana = 35

    def penetrating_arrow(self):
        self.mana -= 20
        print(f"{self.name} used Penetrating Arrow!")
        return self.attack * 1.5

    def aimed_shot(self):
        self.mana -= 40
        print(f"{self.name} used Aimed Shot!")
        return self.attack * 2.5

    def burst_fire(self):
        self.mana -= -35
        print(f"{self.name} used Burst Fire!")
        return self.attack * 1.75