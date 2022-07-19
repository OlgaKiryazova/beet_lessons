class Door:
    #  class attribute
    material = 'wood'

    def __init__(self, width, hight=180):
        # insrance attributes
        self.width = width
        self.hight = hight


    @staticmethod
    def open_door():
        print('door open')


    @classmethod
    def paint(cls):
        print(f'{cls} paint door')

    def close_door(self):
        print('door close')


class CarEngine:

    MIN_CYLINDERS = 4
    MAX_CYLINDERS = 8
    MIN_CAPACITY = 1400
    MAX CAPACITY = 5200

    def __init__(self, fuel_type, capacity, cylinders, idle_rpms=700, max_rpms=8000):
        self.fuel_type = fuel_type
        self.capacity = capacity
        self.cylinders = cylinders
        self.idle_rpms = idle_rpms
        self.max_rpms = max_rpms

        self.sparks = self.cylinders
        self.pump_injector = self.cylinders

        self.rpms = self.idle_rpms
    def start(self):
        print("engine starts")

    def stop(self):
        print("engine stops")

    def accelerate(self):
        self.rpms *=2
        if self.rpms > self.max_rpms:
            print('engine over heated')
        print(f'rpms {self.rpms}')

class GasEngine(CarEngine):
    ...

class




def main():
    door_1 = Door(80, 200)

    door_2 = Door(60)
    # door_1.width = 80
    # door_1.hight = 180
    print(door_1.width, door_1.hight)
    print(door_1.width * door_1.hight)
    print(door_1.material)
    door_1.open_door()

    print(Door(80).paint())
    print(door_1.paint())


if __name__ == '__main__':
    main()