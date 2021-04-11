class Hero():
    name = ""
    hp = 0
    power = 0

    def fight(self,enemy_hp,enemy_power):
        my_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power
        if my_hp > enemy_final_hp:
            print(f"{self.name}赢了")
        elif my_hp < enemy_final_hp:
            print(f"敌人赢了")
        else:
            print("我们打平了")


    def speak_lines(self,name):
        if self.name == "timo":
            print("提莫队长正在待命")
        elif self.name == "police":
            print("见识一下法律的子弹")