from Data.Objects import objects
import random

class Unit:
    def __init__(self, fields):
        self.x = None
        self.y = None
        self.fields = fields
        self.level = 0
        self.field = self.fields[self.level]
        self.future_image = None
        self.image = '@'
        self.find_hero()
        self.money = 0
        self.heal_points = 50
        self.experience = 0
        self.hero_level = 1
        self.defend = 0
        self.attack = 5
        self.overhand = None
        self.work_field()

    def work_field(self):
        self.field = [list(line) for line in self.field]

    def next_level(self):
        """
        Переход на следущую локацию
        """
        self.level += 1
        self.field = self.fields[self.level]
        self.work_field()
        self.find_hero()

    def events(self, key):
        self.field[self.y][self.x] = '.'

        if key == 'w':
            if self.y != 0:
                self.future_image = self.field[self.y - 1][self.x]
                if self.inspection['passable']:
                    self.y -= 1
                    self.inspection['get'](self, self.inspection)
        elif key == 's':
            if len(self.field)-1 != self.y:
                self.future_image = self.field[self.y + 1][self.x]
                print(self.inspection)
                if self.inspection['passable']:
                    self.y += 1
                    self.inspection['get'](self, self.inspection)
        elif key == 'a':
            self.future_image = self.field[self.y][self.x - 1]
            if self.inspection['passable']:
                self.x -= 1
                self.inspection['get'](self, self.inspection)
        elif key == 'd':
            self.future_image = self.field[self.y][self.x + 1]
            if self.inspection['passable']:
                self.x += 1
                self.inspection['get'](self, self.inspection)

    def find_hero(self):
        """
        Ищет персонажа
        """
        j = 0
        i = -1
        for line in self.field:
            try:
                i = line.index(self.image)
                break
            except ValueError:
                j += 1

        if i == -1:
            raise AttributeError("Hero not found")
        else:
            self.x = i
            self.y = j

    def update(self):
        self.field[self.y][self.x] = self.image

    @property
    def inspection(self):
        for item in objects:
            if item['image'] == self.future_image:
                return item

    @property
    def free_place(self):
        path_list = []
        if self.field[self.y+1][self.x] == '.':
            path_list.append((self.y+1, self.x))
        elif self.field[self.y][self.x-1] == '.':
            path_list.append((self.y, self.x-1))
        elif self.field[self.y][self.x+1] == '.':
            path_list.append((self.y, self.x+1))
        elif self.field[self.y-1][self.x] == '.':
            path_list.append((self.y-1, self.x))
        return path_list[random.randint(0, len(path_list) - 1)]

    def empty_overhand(self):
        if self.overhand:
            for item in objects:
                if item['name'] == self.overhand:
                    self.field[self.free_place[0]][self.free_place[1]] = item['image']