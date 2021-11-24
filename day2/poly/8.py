class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __add__(self, other):
        tot_min = self.minutes + self.hours*60 + other.minutes + other.hours*60

        temp = time()
        temp.hours = tot_min//60
        temp.minutes = tot_min%60

        return temp

sat = time(0, 55)
sun = time(1, 35)
total = time()

sat.display()

print("----")
total = sat + sun
total.display()
