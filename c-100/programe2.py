class Car(object):
    def __init__(self, brandname=None, carcolor=None, finish=None):
        self.brandname= brandname 
        self.carcolor= carcolor 
        self.finish= finish

ferrari = Car("Ferrari","Blue","Matt")
print(ferrari.carcolor)
print(ferrari.finish)


