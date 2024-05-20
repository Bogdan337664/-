import math
class Point:
    def __init__(self, coord_x, coord_y):
        self.coordinates = []
        self.coordinates.append([coord_x, coord_y])

    def add_point(self, coord_x, coord_y):
        self.coordinates.append([coord_x, coord_y])
        return self.coordinates

    def distance(self):
        print(math.sqrt((abs(self.coordinates[1][0] - self.coordinates[0][0]) ** 2 + abs(self.coordinates[1][1] - self.coordinates[0][1]) ** 2)))
        return math.sqrt((abs(self.coordinates[1][0] - self.coordinates[0][0]) ** 2 + abs(self.coordinates[1][1] - self.coordinates[0][1]) ** 2))

    def move(self, shift_x, shift_y):
        self.coordinates[0][0] += shift_x
        self.coordinates[0][1] += shift_y
        return self.coordinates

    def check_axis(self):
        if self.coordinates[0][0] == 0 or self.coordinates[0][1] == 0:
            print('Belongs to axis')
            return True
        else:
            print('Does not belong to axis')
            return False

p = Point(1, 2)
p.add_point(3, 4)
p.distance()
