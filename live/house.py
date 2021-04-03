#通过class定义一个类
class House:
    #类的属性（静态属性）
    door = ""
    floor = ""
    #类的方法
    #使用defi当以函数，类中的函数叫做（动态）方法
    def cook(self):
        print("在厨房做饭")

    def sleep(self):
        print("在卧室睡觉")

#实例对象
bob_house = House()
bob_house.door = "white"
bob_house.floor = "black"

#可以定义多个实例对象
#修改实例的属性不会影响类本身
print("house.door的值为",House.door)
#修改当前实例的属性不会影响到其他的实例
mary_house = House()
print(mary_house)