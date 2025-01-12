QUESTION 1

# Define a Smartphone class
class Smartphone:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color

    def make_call(self, number):
        print(f"Calling {number} from {self.brand} {self.model}")

    def send_text(self, message):
        print(f"Sending '{message}' from {self.brand} {self.model}")

# Define a subclass of Smartphone with additional attributes and methods
class FlagshipPhone(Smartphone):
    def __init__(self, brand, model, storage, color, camera_resolution):
        super().__init__(brand, model, storage, color)
        self.camera_resolution = camera_resolution

    def take_picture(self):
        print(f"Taking a picture with {self.camera_resolution} camera on {self.brand} {self.model}")

# Create instances of Smartphone and FlagshipPhone
iphone = Smartphone("Apple", "iPhone 14", 128, "Space Gray")
samsung = FlagshipPhone("Samsung", "Galaxy S22", 256, "Phantom Black", "50MP")

# Test the methods
iphone.make_call("123-456-7890")
iphone.send_text("Hello, world!")

samsung.make_call("987-654-3210")
samsung.send_text("This is a flagship phone!")
samsung.take_picture()





QUESTION 2
# Define an Animal class with a move() method
class Animal:
    def move(self):
        pass

# Define subclasses of Animal with their own move() methods
class Dog(Animal):
    def move(self):
        print("Walking")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

# Create instances of the Animal subclasses
dog = Dog()
bird = Bird()
fish = Fish()

# Test the move() method using polymorphism
animals = [dog, bird, fish]
for animal in animals:
    animal.move()