class Dog:

    def __init__(self, name, age, furcolour):
        self.name = name
        self.age = age
        self.furcolour = furcolour

    def bark(self, str):
        print("Bark!" + str)

mydog = Dog("Ndongi", 13, "Brown")
mydog.bark("Woof Woof!")

print(mydog.age)