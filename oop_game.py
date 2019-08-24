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
        guess = input('%s %s %s \n > ' % (guesses_left, hint, self.obfuscated_word))
        self.guesses_left -= 1
        return guess

    def challenge_user(self):
        answer = self.prompt_guess()
        if answer == self.word:
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
            try:
                result_string = current_scene.enter()
            except AttributeError as err:
                print('invalid answer')
                raise
            else:
                # Progress forward by overriding the new current_scene for next iteration of loop 
                current_scene = self.scene_map.next_scene(result_string)


class Death(Scene):
    quips = [
        'u ded bro',
        'lol ded, you said youd try not to die',
        'you died, sorry',
        'so ded',
        'killed you haha, ur ded now'
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Win(Scene):
    congrats = [
        'yay u won and did not die',
        'good job bub',
        'u won, play again soon bye',
    ]

    def enter(self):
        print("you ride off into the sunset, eventually making your way back to earth.")
        print(Win.congrats[randint(0, len(self.congrats)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print('You are on your spaceship in the **Central Corridor**, normal day in year 3288')
        print('Oh no! Red alert! Ship invaded by aliens. Everyone dead except for you. You must get bomb from Weapons Armory and blow up Bridge')
        print('After getting into Escape pod. U are now running down corridor to Armory, scary Alien jump out and blocks door')
        print('What do you do?')

        validated_action = validated_prompt(
            "T for throw shoe, D for dodge, C for cry \n > ",
            ['T', 'D', 'C']
        )

        if validated_action == 'T':
            print('U try to throw shoe but if makes Alien angry, not ded. He bite ur face off.')
            return 'death'
        elif validated_action == 'D':
            print('You jump out of the way and sruvive, you head to the Armory to get lots o\' guns')
            return 'laser_weapon_armory'
        elif validated_action == 'C':
            print('U cry baby tears and alien feels bad, he gives you directions to Armory to get lots o\' guns')
            return 'laser_weapon_armory'

# Helper function for all prompts which re-prompts if input is not allowed. Handles `enter` properly
def validated_prompt(message, allowed_commands):
    attempted_action = input(message)
    if attempted_action.upper() not in allowed_commands:
        print("Invalid! Try: {}".format(allowed_commands))
        return validated_prompt(message, allowed_commands)
    else:
        return attempted_action.upper()

class LaserWeaponArmory(Scene):
    def enter(self):
        print('You walk inside bright room filled with weapons along all walls')
        print('And a suitcase conveiniently sits in the middle of the room')
        print('You see a wall of swords, a wall of lazer machine guns, and a wall of baseball bats')
        print('What do?')

        validated_action = validated_prompt(
            "S for get swords, L for lazer guns, B for bomb \n > ",
            ['S', 'B', 'L']
        )

        if validated_action == 'S':
            print('The swords are too spikey and don\'t fit in suitcase, takes too long and alien eat you \n > ')
            return 'death'
        elif validated_action == 'B':
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
        elif validated_action == 'L':
            print('You put a few Lazer guns into your bag and you must run to the bridge to blow it up')
            return 'the_bridge'

class TheBridge(Scene):
    def enter(self):
        print('You step off the turbolift onto the bridge.')
        print('You see an alien trying to hack into the ships main computer.')
        print('The alien is focused, do you want to sneak behind him and place the bomb under')
        print('the chair? Or do you want to throw the bomb and run?')
        print('What do you do?')

        validated_action = validated_prompt(
            "S for be sneaky, T for throw the bomb and run! \n > ",
            ['S', 'T']
        )

        if validated_action == 'S':
            print('You carefully arm the bomb under the aliens butt, and sneak out of the bridge. Time to escape.')
            return 'escape_pod'
        elif validated_action == 'T':
            print('In haste, you throw the bomb and forget to arm it. It hits the alien in the head but does not explode. He\'s confused and mad and eats your face.')
            return 'death'

class EscapePod(Scene):
    def enter(self):
        print('You presurize the escape pod airlock and seal yourself into the pod ')
        print('This is your last ticket off the ship, back to earth')
        print('Do you know how to fly this thing?')
        print('You see an unnessarily confusing control panel, which button to you press?')

        validated_action = validated_prompt(
            "X - EXTRAPOLATE DESTRUCTIVE SELF BURNINATION \n Y - DEBUG MAIN ESCAPE COMPUTER \n Z - CONNECT TO EARTH AUTO_OVERRIDE \n D - DO SPACE DONUTS \n > ",
            ['X', 'Y', 'Z', 'D']
        )

        if validated_action == 'X':
            print('The escape pod heats up like an easy-bake oven and you burn up like a pop-tart in a malfunctioning toaster')
            return 'death'
        elif validated_action == 'Y':
            print('THe computer readout says Y THO? CANNOT COMPUTER. NOT PROGRAMMED TO INSPECT SELF. PERMANENT SHUTDOWN INITIATED. GOODBYE HUMAN.')
            return 'death'
        elif validated_action == 'Z':
            print('Connected to young timmy\'s XBOX, timmy now in full remote control of escape pod. Have a nice flight')
            return 'win'
        elif validated_action == 'D':
            print('You take the escape pod for a joyride, doing donuts in the vacuum of space. Ship explodes, and do you.')
            return 'death'

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