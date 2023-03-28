import sys # 3. never used

class Person:
    def __init__(self, first_name,  last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    if "Windows" in platform.platform():
        print("You're using Windows!")

    self.age = self.getAge(1,2,3)

    def getAge(this):
        return "18"

# it has 4 issues
# 1. "too many positional arguments" error in the call of the method getAge
# 2. The getAge method it