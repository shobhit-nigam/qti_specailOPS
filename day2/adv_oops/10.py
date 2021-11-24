class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __call__(self, h=0, m=0):
        self.hours = h
        self.minutes = m



sat = time(0, 55)
sun = time(1, 35)
#total = time(1.5)

sat(1, 30)

sat.display()
