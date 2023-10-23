class Animal:
    def speaks(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class DogChild(Dog):
    def eats(self):
        print("Drinking milk")

dog= Dog() #this is the object
dog.bark()
dog.speaks()

dogmdogo=DogChild() #Object2
dogmdogo.bark()
dogmdogo.speaks()
dogmdogo.eats()