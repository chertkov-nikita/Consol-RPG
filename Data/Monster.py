def attack(hero, monster):
    hero.heal_points -= monster['damage']


monsters = [
    {'name': 'snake', 'image': 's', 'damage': 5, "get": attack, 'passable': True},
    {'name': 'rat', 'image': '>', 'damage': 3, "get": attack, 'passable': True},
    {'name': 'bug', 'image': 'o', 'damage': 1, "get": attack, 'passable': True}
]
