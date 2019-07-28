from sys import exit
import random
from random import randint
from urllib import urlopen
from six.moves import input as input

class Challenge(object):
    """
    use challenge_user() to provide a challenge that changes each instance, can
    be type guess passoword or close_airlock, and both will return 'success' or 'failure'
    """
    CHALLENGE_TYPES = ['guess_password', 'close_airlock']
    WORD_URL = "http://learncodethehardway.org/words.txt"
    WORDS = []

    def __init__(self, type='guess_password'):
        self.type = type
        self.guesses_left = 3
        self.word = self.get_random_word()
        self.obfuscated_word = self.word.replace(self.word[randint(0, len(self.word)-1)], '*')
        self.completed = False

    def get_random_word(self):
        try:
            # load up the words from the website
            for word in urlopen(self.WORD_URL).readlines():
                self.WORDS.append(word.strip().decode("utf-8"))
            return random.sample(self.WORDS, 1)[0]
        except Exception as e:
            print('Could not open word URL because: %s' % e)

    def prompt_guess(self):
        word = self.word
        hint = 'The password is missing letters for some strange reason, guess the full password: '
        guesses_left = 'You have %s guesses left!' % self.guesses_left
        guess = input('%s %s %s \n >' % (guesses_left, hint, self.obfuscated_word))
        self.guesses_left -= 1
        return guess

    def challenge_user(self):
        answer = self.prompt_guess()
        if answer == self.word:
            import pdb; pdb.set_trace()
            self.completed = True
            return 'success'
        else:
            return 'failure'

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
            # Jump into current scene and store returned result as `result_string`
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

        action = input("T for throw shoe, D for dodge, C for cry >")

        if action.upper() == 'T':
            print('U try to throw shoe but if makes Alien angry, not ded. He bite ur face off.')
            return 'death'
        elif action.upper() == 'D':
            print('You jump out of the way and sruvive, you head to the Armory to get lots o\' guns')
            return 'laser_weapon_armory'
        elif action.upper() == 'C':
            print('U cry baby tears and alien feels bad, he gives you directions to Armory to get lots o\' guns')
            return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):
    def enter(self):
        print('You walk inside bright room filled with weapons along all walls')
        print('And a suitcase conveiniently sits in the middle of the room')
        print('You see a wall of swords, a wall of lazer machine guns, and a wall of baseball bats')
        print('What do?')

        action = input("S for get swords, L for lazer guns, B for bomb \n>")

        if action.upper() == 'S':
            print('The swords are too spikey and don\'t fit in suitcase, takes too long and alien eat you')
            return 'death'
        elif action.upper() == 'B':
            print('you must unlock the bomb first.')
            bomb_challenge = Challenge()
            while bomb_challenge.guesses_left > 0 and not bomb_challenge.completed:
                result = bomb_challenge.challenge_user()
            if result == 'success':
                print('Good jobs, you unlocked the bomb, head to the Bridge to blow that sucker up')
                return 'the_bridge'
            else:
                print('Sorry you guessed really bad, intruder detected, bomb go into self-destruct mode now...')
                return 'death'
        elif action.upper() == 'L':
            print('You put a few Lazer guns into your bag and you must run to the bridge to blow it up')
            return 'the_bridge'

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
    # print(Challenge('guess_password').prompt_guess())