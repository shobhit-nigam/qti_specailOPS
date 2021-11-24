class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __float__(self):
        temp = self.hours + self.minutes*0.01
        return temp



sat = time(0, 55)
sun = time(1, 35)

x = float(sun)
print(x)
