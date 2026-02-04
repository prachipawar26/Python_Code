class Bird:
    def fly(self):
        print("Bird is flapping wings")

class Airplane:
    def fly(self):
        print("Airplane is engaging engines")

class Whale:
    def swim(self):
        print("Whale is swimming")

def lift_off(entity):
    # We don't check 'isinstance(entity, Bird)'
    # We just try to call the method
    entity.fly()

# These work perfectly:
lift_off(Bird())
lift_off(Airplane())

# This fails because Whale doesn't "quack" (fly)
# lift_off(Whale())  
