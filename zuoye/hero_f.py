from zuoye.police import Police
from zuoye.timo import Timo


class HeroFactory():
    name = ""

    def caeatehero(self,name):
        if name == "timo":
            return Timo()
        elif name == "police":
            return Police()
        else:
            raise Exception("此英雄不在英雄工厂中")

hero_factory = HeroFactory()
timo = hero_factory.caeatehero("timo")
police = hero_factory.caeatehero("police")
timo.speak_lines(timo)
police.speak_lines(police)