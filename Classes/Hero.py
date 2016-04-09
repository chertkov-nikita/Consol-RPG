class Unit:
    def __init__(self, fields, status_bar):
        self.x = None
        self.y = None
        self.fields = fields
        self.level = 0
        self.field = self.fields[self.level]
        self.image = '@'
        self.find_hero()
        self.status_bar = status_bar
        self.status_bar_cope = None
        self.money = 0
        self.heal_points = 50
        self.experience = 0
        self.hero_level = 1
        self.defend = 0
        self.attack = 5
        self.owerhand = 0
        self.fill_bar()
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
                if self.field[self.y-1][self.x] != '#':
                    self.y -= 1
        elif key == 's':
            if self.y != len(self.field)-1:
                if self.field[self.y+1][self.x] != '#':
                    self.y += 1

        if key == 'a':
            if self.field[self.y][self.x-1] != '#' and self.field[self.y][self.x-1] != '/':
                self.x -= 1
        elif key == 'd':
            if self.field[self.y][self.x+1] != '#':
                self.x += 1

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
        self.fill_bar()

    def inspection(self):
        """
        Проверка на ключевые символы
        """
        if self.field[self.y][self.x] == '/':
            self.next_level()
        if self.field[self.y][self.x] == '$':
            self.money += 10
        if self.field[self.y][self.x] == '=':
            self.owerhand += 3

    def fill_bar(self):
        """
        Заполняет status_bar значениями
        """
        self.status_bar_cope = self.status_bar[:]
        self.status_bar_cope[0] = self.status_bar_cope[0].format(str(self.hero_level))
        self.status_bar_cope[1] = self.status_bar_cope[1].format(str(self.heal_points))
        self.status_bar_cope[2] = self.status_bar_cope[2].format(str(self.experience))
        self.status_bar_cope[3] = self.status_bar_cope[3].format(str(self.owerhand))
        self.status_bar_cope[4] = self.status_bar_cope[4].format(str(self.attack))
        self.status_bar_cope[5] = self.status_bar_cope[5].format(str(self.defend))
        self.status_bar_cope[6] = self.status_bar_cope[6].format(str(self.money))
