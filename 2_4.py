class X:
    def __init__(self, a, b):
        if a != 'Николай':
            self.a = 'Я не ' + a + ', а Николай'
        else:
            self.a = a
        self.b = b
        print(self.a)

y = X('МАКСДАУН', -4)

