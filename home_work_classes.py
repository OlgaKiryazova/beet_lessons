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
        return self.channel[0]

    def last_channel(self):
        return self.channel[-1]

    def _controller_channels(self, number):
        self.channel_number = self.channel_number + number
        return self.channel[self.channel_number]

    def turn_channel(self, n):
        return self.channel[n-1]
        # return self.controller_channels(1)

    def next_channel(self):
        try:
            return self._controller_channels(+1)
        except:
            self.channel_number = 0
            return self._controller_channels(self.channel_number)

    def previous_channel(self):
        try:
            return self._controller_channels(-1)
        except:
            self.channel_number = -1
            return self._controller_channels(self.channel_number)

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

    def __init__(self, last_name, forces, experience):
        self.last_name = last_name
        self.forces = forces
        self.experience = experience

        self.weapon = None

    @staticmethod
    def salute():
        print('Glory to Ukraine!')

    def get_weapons(self, weapon):
        self.weapon = weapon
        print(f'{weapon} received')

    def attack(self):
        pass


class Soldier(Military):
    RANK = 'Soldier'
    soldiers = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.soldiers.append(self.last_name)

    def attack(self):
        print(f'Took {self.weapon} and and went on the attack')



class Major(Military):
    RANK = 'Major'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def attack(self):
        print(f' {Soldier.soldiers} soldiers were ordered to attack')


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

    soldier_1 = Soldier('Petrov', 'naval forces', '2 years')
    soldier_2 = Soldier('Petrenco', 'naval forces', '3 years')
    soldier_1.salute()
    print(Soldier.soldiers)
    soldier_1.get_weapons('MLRS')
    print(soldier_1.weapon)
    major = Major('Ivanov', 'naval forces', '10 years')
    major.attack()



if __name__ == '__main__':
    main()