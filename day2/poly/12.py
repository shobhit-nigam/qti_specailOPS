class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours and {self.minutes} minutes")

    def __lt__(self, other):
        return (self.minutes + self.hours*60) < (other.minutes + other.hours*60)

    def __gt__(self, other):
        return (self.minutes + self.hours*60) > (other.minutes + other.hours*60)

    def __eq__(self, other):
        return (self.minutes + self.hours*60) == (other.minutes + other.hours*60)

sat = time(0, 55)
sun = time(1, 35)
mon = time(1, 50)

if sun > mon:
    print("productive sunday")
elif sun == mon:
    print("two great days")
else:
    print("productive monday")



# varx += 1
# varx = varx + 1
