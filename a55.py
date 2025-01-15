class robot:
    species='robot'
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def intro(self):
        print("Hello...my name is", self.name)
    def details(self):
        print("I am", self.age,"years old")
    def sing(self,s):
        print(self.name,"is singing ",s,"song")
o1=robot("Sophie",100)#object/instance,created from a class 
o2=robot("Atlas",250)
o1.intro()
o1.details()
o1.sing("beep")
o2.intro()
o2.details()
o2.sing("lalalalala")
print(o1.species)
print(o2.species)