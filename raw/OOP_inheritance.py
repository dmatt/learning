class Animal(object):
    # Example of an Abstract method in base class
    def vocalize(self):
        raise NotImplementedError

    def get_status(self):
        return 'overridden from base class'

class Lion(Animal):
    def __init__(self, roar_volume):
        self.roar_volume = roar_volume

    def roar(self):
        if self.roar_volume == 'loud':
            return 'ROOOOAAAAAWWWRRRR'
        else:
            return 'rawr'

    def vocalize(self):
        print(self.roar())

class Zazu(Animal):
    def squawk(self):
        return 'squawk!!'

    # method that calls other method
    def vocalize(self):
        print(self.squawk())

class Mufasa(Lion):
    def __init__(self, roar_volume='loud'):
        self.status = 'king'
        self.roar_volume = roar_volume

    def get_status(self):
        return self.status

class Simba(Mufasa):
    def __init__(self, roar_volume='quiet'):
        self.status = 'prince'
        self.roar_volume = roar_volume

if __name__ == "__main__":
    a_simba = Simba()
    a_simba.vocalize()
    a_simba.get_status()