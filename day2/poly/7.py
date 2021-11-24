class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")



sat = time(0, 55)
sun = time(1, 35)
total = time()

sat.display()

print("----")
# error
total = sat + sun
