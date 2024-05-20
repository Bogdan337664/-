class Beverage:
    def initialize(self, additive=1):
        self.additive = additive
    
    def display(self):
        if self.additive != 1:
            return f'Soda with {self.additive}'
        else:
            return 'Plain soda'

cola = Beverage('coloring')
print(cola.display())
