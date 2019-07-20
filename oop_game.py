from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("This base scene not configured. Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print("\n - ")
            # Jump into current scene and stored returned result as `result_string`
            result_string = current_scene.enter()
            # Progress forward by overriding the new current_scene for next iteration of loop 
            current_scene = self.scene_map.next_scene(result_string)            

class Death(Scene):
    quips = [
        'u ded bro',
        'lol ded, you said youd try not to di',
        'you died, sorry',
        'so ded',
        'kild u haha, ur ded now'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Win(Scene):
    congrats = [
        'yay u won and did not di',
        'good job bub',
        'u won, play again soon bye',
    ]

    def enter(self):
        print(Win.congrats[randint(0, len(self.congrats)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print('You are on your spaceship in the **Central Corridor**, normal day in year 3288')
        print('Oh no! Red alert! U ship invaded by alien. All ded except you. U must get bomb from Weapons Armory and blow up Bridge')
        print('after getting into Escape pod. U are now running down corridor to Armory, scary Alien jump out blocking door')
        print('What do?')

        action = input("S for shoot, D for dodge, C for cry >")

        if action == 'S':
            print('U try to shoot but if makes Alien angry, not ded. He bite ur face off.')
            return 'death'
        elif action == 'D':
            print('You jump out of the way and sruvive, keep running to escape pod')
            return 'escape pod'
        elif action == 'C':
            print('U cry baby tears and alien feels bad and helps you to escape pod')
            return 'escape pod'

class LaserWeaponArmory(Scene):
    def enter(self):
        pass

class TheBridge(Scene):
    def enter(self):
        pass

class EscapePod(Scene):
    def enter(self):
        pass

class Map(object):
    scenes = {
        'central_cooridor': CentralCorridor(),
        'escape_pod': EscapePod(),
        'the_bridge': TheBridge(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'death': Death(),
        'win': Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        """lookup the the scene class from a string in the dict"""
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

if __name__ == '__main__':
    a_map = Map('central_cooridor')
    a_game = Engine(a_map)
    a_game.play()