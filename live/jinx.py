from live.ez import EZ
from live.hero import Hero


class JInx(Hero):
    hp = 2000
    power = 210
    name = "Jinx"



jinx = JInx()
ez = EZ()
ez.fight(jinx.hp,jinx.power)