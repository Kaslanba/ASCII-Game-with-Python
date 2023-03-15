from player import Player


class Warrior(Player):
    type = "warrior"
    spells = [("Mortal Strike", "60", "25"), ("Shield Bash", "45", "20"), ("Berserk", "90", "40"),
              ("Normal Attack", "30")]

    def __init__(self, name, health=0, attack=0, mana=0):
        Player.__init__(self, name)
        self.health = 100
        self.max_health = 100
        self.attack = 30
        self.mana = 40
        self.max_mana = 40

        self.mortal_strike_mana = 20
        self.shield_bash_mana = 10
        self.berserk_mana = 30

    def mortal_strike(self):
        self.mana -= 25
        print(f"{self.name} used Mortal Strike!")
        return self.attack * 2

    def shield_bash(self):
        self.mana -= 20
        print(f"{self.name} used Shield Bash!")
        return self.attack * 1.5

    def berserk(self):
        self.mana -= 40
        print(f"{self.name} used Berserk!")
        return self.attack * 3