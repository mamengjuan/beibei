from zuoye.hero import Hero
from zuoye.timo import Timo


class Police(Hero):
    hp = 1000
    power = 200
    name = "police"

    # def fight(self,enemy_hp,enemy_power):
    #     my_hp = self.hp - enemy_power
    #     enemy_final_hp = enemy_hp - self.power
    #     if my_hp > enemy_final_hp:
    #         print(f"police赢了")
    #     elif my_hp < enemy_final_hp:
    #         print(f"敌人赢了")
    #     else:
    #         print("我们打平了")

timo = Timo()
police = Police()
police.fight(timo.hp,timo.power)