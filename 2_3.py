class TriangleValidator:
    def initialize(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
    def check_triangle(self):
        a = self.side_a
        b = self.side_b
        c = self.side_c
        try:
            if a > 0 and b > 0 and c > 0:
                if a + b > c and a + c > b and b + c > a:
                    print('Great, you can build a triangle from these sides!')
                else:
                    print('Unfortunately, these sides cannot form a triangle.')
            else:
                print('Cannot work with negative numbers')
        except TypeError:
            print('Please input only numbers')

triangle = TriangleValidator(3, 4, 5)
triangle.check_triangle()
