from vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, color):
        super().__init__(color)

    def drive(self):
        print('werrrr werrrrrrr werrrrrrrrrrrr')

    def stop(self):
        print('skrt skrt!')


class Car(Vehicle):
    def __init__(self, color):
        super().__init__(color)        
        
    def drive(self):
        print('vrooooooommm')


class Truck(Vehicle):
    def __init__(self, color):
        super().__init__(color)

    def drive(self):
        print('vrum vrum vrum vrum')


class Boat(Vehicle):
    def __init__(self, color):
        super().__init__(color)

    def drive(self):
        print('wsssshhhhhhhhh')

    def stop(self):
        print('swish swish swish')


class Lawn_Mower(Vehicle):
    def __init__(self, color):
        super().__init__(color)

    def drive(self):
        print('clink clunk wurrrrrrrr')

    def stop(self):
        print('brummp')


CL360 = Motorcycle("orange & black")
CL360.new_name("Honda CL360")

Civic = Car("gray")
Civic.new_name("Honda Civic")

Tacoma = Truck("matte gray")
Tacoma.new_name("Tacoma")

Yacht = Boat("white")
Yacht.new_name("Yacht")

mower = Lawn_Mower("green")
mower.new_name("big ass lawnmower")


print(f"My {CL360.name} is {CL360.color}. It goes fast and it's like:")
CL360.drive()
print("Then I stop and it's like:")
CL360.stop()
print("It can:")
CL360.turn("sharply")
print()

print(f"My {Civic.name} is {Civic.color}. It goes fast and it's like:")
Civic.drive()
print("Then I stop and it's like:")
Civic.stop()
print("It can:")
Civic.turn("fairly sharply")
print()

print(f"My dream {Tacoma.name} would be {Tacoma.color}. It would go fast and be like:")
Tacoma.drive()
print("Then I'd stop and it'd be like:")
Tacoma.stop()
print("It can:")
Tacoma.turn("not so well")
print()

print(f"If I get rich I may buy a {Yacht.name}. It would probably be {Yacht.color}. It would only go leisurely speeds and be like:")
Yacht.drive()
print("Then I'd stop and it'd be like:")
Yacht.stop()
print("It can:")
Yacht.turn("all over the place")
print()

print(f"Someday I may buy a {mower.name}. It would probably be {mower.color}. It wouldn't be able to go fast and just be like:")
mower.drive()
print("Then I'd stop and it'd be like like:")
mower.stop()
print("It can:")
mower.turn("on a dime")