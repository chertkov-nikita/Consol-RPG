class Monster:
    def __init__(self, fields, image):
        self.x = None
        self.y = None
        self.have = True
        self.fields = fields
        self.level = 0
        self.field = self.fields[self.level]
        self.image = image
        self.i = 0
        self.work_field()
        self.find_monster()

    def work_field(self):
        self.field = [list(line) for line in self.field]

    def find_monster(self):
        """
        Ищет монстра
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
            self.have = False
            raise AttributeError('Monster not found')
        else:
            self.x = i
            self.y = j

    def move(self):
        if self.have:
            self.field[self.y][self.x] = '.'


class Snake(Monster):
    def __init__(self):
        self.image = 's'

    def move(self):
        Monster.move(self)
        # path_list = [lambda: self.x-1, lambda: self.y-1, lambda: self.x+1, lambda: self.y+1]
        path_list = [(-1, 0), (1, 0)]
        self.x += path_list[self.i][0]
        self.y += path_list[self.i][1]
        self.i += 1
        if self.i >= len((path_list)):
            self.i = 0
        # if self.i == 0:
        #     self.x = path_list[0]()
        #     self.i += 1
        # elif self.i == 1:
        #     self.y = path_list[1]()
        #     self.i += 1
        # elif self.i == 2:
        #     self.x = path_list[2]()
        #     self.i += 1
        # elif self.i == 3:
        #     self.y = path_list[3]()
        #     self.i = 0
