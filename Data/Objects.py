def get_sword(hero, item):
    hero.attack = item["attack"]
    hero.overhand = item['name']


def get_money(hero, item):
    hero.money += item['value']


def next_level(hero):
    hero.next_level()

objects = [
    {'name':'sword', 'image':'|', "attack": 20, "get": get_sword, 'passable':True},
    {'name':'money', 'image':'$', 'value':20, "get":get_money, 'passable':True},
    {'name':'wall', 'image':'#', 'passable':False},
    {'name':'door', 'image':'/', 'get':next_level, 'passable':True}
]
