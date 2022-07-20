class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f'Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old')


class Dog:

    def __init__(self, age_factor):
        self.age_factor = age_factor

    def human_age(self):
        age = self.age_factor * 7
        print(f'The dog’s age {self.age_factor} in human equivalent = {age} years')


class TVController:

    def __init__(self, channel):
        self.channel = channel
        self.channel_number = 0

    def first_channel(self):
        print(self.channel[0])

    def last_channel(self):
        print(self.channel[-1])

    def controller_channels(self, number):
        self.channel_number = self.channel_number + number
        return self.channel[self.channel_number]

    def turn_channel(self, n):
        return self.channel[n-1]
        # return self.controller_channels(1)

    def next_channel(self):
        try:
            return self.controller_channels(+1)
        except:
            self.channel_number = 0
            return self.controller_channels(self.channel_number)

    def previous_channel(self):
        try:
            return self.controller_channels(-1)
        except:
            self.channel_number = -1
            return self.controller_channels(self.channel_number)

    def current_channel(self):
       return self.channel[self.channel_number]

    def is_exist(self, arg):
        if isinstance(arg, int):
            if len(self.channel) >= arg:
                print(f'yes "{arg}" : {self.channel[arg-1]}')
            else:
                print('No')
        else:
            if arg in self.channel:
                print(f'yes {arg}')
            else:
                print(f'no {arg}')


class Military:

    def __init__(self, last_name, forces, function, experience):
        self.last_name = last_name
        self.forces = forces
        self.function = function
        self.experience = experience

    @staticmethod
    def salute():
        print('Glory to Ukraine!')

    def get_weapons(self, weapon):
        self.weapon = weapon
        print(f'{weapon} received')

    def print_forces(self):
        print(self.forces)


class Soldier(Military):
    RANK = 'Soldier'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Major(Military):
    RANK = 'Major'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def main():
    # Task 1
    carl = Person('Carl', 'Johnson', 26)
    carl.talk()

    # Task 2
    dog_1 = Dog(3)
    dog_1.human_age()

    # Task 3
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = TVController(CHANNELS)
    controller.first_channel()
    controller.last_channel()
    print(controller.turn_channel(1))
    print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    # print(controller.next_channel())
    print(controller.previous_channel())
    print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    # print(controller.previous_channel())
    print(controller.current_channel())
    # print(controller.current_channel())
    controller.is_exist(1)
    controller.is_exist(3)
    controller.is_exist(4)
    controller.is_exist('TV1000')

    soldier_1 = Soldier('Petrov', 'naval forces', 'naval forces', 10)
    soldier_1.salute()
    soldier_1.get_weapons('MLRS')
    print(soldier_1.weapon)
    soldier_1.print_forces()


if __name__ == '__main__':
    main()