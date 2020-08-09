"""
__author__:'vacada'
__description__:
'
定义“动物”、“猫”、“动物园”三个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，猫类继承自动物类。
动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'
__mtime__:2020/8/9
"""

from abc import ABCMeta, abstractmethod

class Zoo(object):
    # zoo = list()
    def __init__(self, name):
        super().__init__()
        self.name = name

    # 添加动物
    def add_animal(self, cls):
        # 如果动物园没有对应动物，添加一个对应动物属性
        if not hasattr(self, cls.__class__.__name__):
            setattr(self, cls.__class__.__name__, cls.name)


class Animal(metaclass=ABCMeta):
    def __init__(self, animal_type, animal_body_type, animal_character):
        self.animal_type = animal_type
        self.animal_body_type = animal_body_type
        self.animal_character = animal_character
    
    # def __getattribute__(self, item):
    #     if item == animal_body_type:
    #     return super().__getattribute__(item)

    # 判断是否是凶猛动物
    @property
    def is_ferocious_animal(self):
        return self.animal_type == '食肉' and '小' not in self.animal_body_type and self.animal_character == '凶猛'
    
    @property
    @abstractmethod
    def is_pet(self):
        pass



class Cat(Animal):
    # 定义猫咪叫声的类属性
    barking = 'meow~~'
    _instance = None  

    def __new__(cls, name, animal_type, animal_body_type, animal_character, *args, **kargs):
        if not cls._instance:
            cls._instance = super(Cat, cls).__new__(cls, *args, **kargs)
        return cls._instance

    def __init__(self, name, animal_type, animal_body_type, animal_character):
        super().__init__(animal_type, animal_body_type, animal_character)
        self.name = name
    
    # 根据是否是凶猛动物判断是否适合作为宠物
    @property
    def is_pet(self):
        return not self.is_ferocious_animal


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫1', '食肉', '小', '温顺')
    # 增加一个猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
