def get_weapon(hero, item):
    hero.empty_overhand()
    hero.attack = item["attack"]
    hero.overhand = item['name']


def get_money(hero, item):
    hero.money += item['value']


def next_level(hero, item):
    hero.next_level()


def get_defend(hero, item):
    hero.defend += item['defend']


def nine(hero, item):
    pass


objects = [
    {'name': 'sword', 'image': '†', "attack": 15, "get": get_weapon, 'passable': True},
    {'name': 'knifes', 'image': '‡', "attack": 5 + 5, "get": get_weapon, 'passable': True},
    {'name': 'ax', 'image': 'ґ', "attack": 20, "get": get_weapon, 'passable': True},
    {'name': 'little_armor', 'image': '★', "defend": 5, "get": get_defend, 'passable': True},
    {'name': 'average_armor', 'image': '+', "defend": 8, "get": get_defend, 'passable': True},
    {'name': 'heavy_armor', 'image': '✪', "defend": 10, "get": get_defend, 'passable': True},
    {'name': 'little_purse_money', 'image': '$', 'value': 20, "get": get_money, 'passable': True},
    {'name': 'purse_money', 'image': '&', 'value': 50, "get": get_money, 'passable': True},
    {'name': 'wall', 'image': '#', 'passable': False, "get": nine},
    {'name': 'torch', 'image': 'Ї', 'passable': False, "get": nine},
    {'name': 'floor', 'image': '.', 'passable': True, "get": nine},
    {'name': 'door', 'image': '/', 'get': next_level, 'passable': True}
]
