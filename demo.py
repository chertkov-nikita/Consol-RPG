from Data.Status_bar import demo_status_bar, status_bar
from Classes.Hero import Unit
from Data.fields import fields

hero = Unit(fields, status_bar)

hero.next_level()
hero.next_level()

print(hero.field)
