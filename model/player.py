class Player:
    def __init__(self, pseudo, health, attack, weapon=None):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = weapon
    def set_weapon(self, weapon):
        self.weapon = weapon
        
    def get_weapon(self):
        return self.weapon

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_information(self):
        return f"Pseudo: {self.pseudo}, Health: {self.health}, Attack: {self.attack}"

    def attack_player(self, player):
        total_damage = self.attack
        if self.weapon:
            total_damage += self.weapon.get_damage()
        player.health = max(0, player.health - total_damage)
        print(f"{self.pseudo} attack {player.pseudo}")



class Warrior(Player):
    def __init__(self, pseudo, health, attack, weapon=None):
        super().__init__(pseudo, health, attack, weapon)
        self.armor = 3

    def get_armor(self):
        return self.armor

    def attack_player(self, player):
        total_damage = self.attack
        # super().attack_player(player)
        if self.armor > 0:
            self.armor -= 1
            total_damage = max(0, self.attack - player.get_armor())
        if self.weapon:
            total_damage += self.weapon.get_damage()
        player.health = max(0, player.health - total_damage)
        print(f"{self.pseudo} attack {player.pseudo}")