class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __add__(self, other):
        temp = time()
        if type(other) is time:
            tot_min = self.minutes + self.hours*60 + other.minutes + other.hours*60
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        elif type(other) is int:
            tot_min = self.minutes + self.hours*60 + other
            temp.hours = tot_min//60
            temp.minutes = tot_min%60

        else:
            print("some error message")

        return temp

sat = time(0, 55)
sun = time(1, 35)
mon = time(1, 20)

sat.display()

print("----")
# chaining of operators
total = sat + sun + 10
total.display()
