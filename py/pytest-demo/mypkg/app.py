class App:
    def __init__(self, v):
        print('App.__init__')
        self.m = v

    def getV(self):
        return self.m
