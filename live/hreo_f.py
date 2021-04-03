from live.ez import EZ
from live.jinx import JInx

class HeroFactory:

    def createhero(self,name):
        if name == "Jinx":
            return JInx()
        elif name == "ez":
            return EZ()
        else:
            raise Exception("此英雄不在英雄工厂中")

hero_factory = HeroFactory()
jinx = hero_factory.createhero("Jinx")
ez = hero_factory.createhero("ez")
jinx.fight(ez.hp,ez.power)