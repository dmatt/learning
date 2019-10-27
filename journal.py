"""A daily journal entry prompter that stores entries in a txt file"""

from datetime import datetime
from pathlib import Path

from quotes import *

JOURNAL_FOLDER = Path('/Users/dmatt/Desktop/Daily Journal/')

FILE_PREFIX = 'Journal Entry '
FILE_EXT = 'txt'
# Questions come from this 5 Minute Journal system:
# https://www.intelligentchange.com/blogs/news/five-minute-journal-tips
QUESTIONS = {
    'one': "I am greatful for...",
    'two': "What would make today great?",
    'three': "Daily affirmations: I am...",
    'four': "3 amazing things that happened today...",
    'five': "How could I have made today even better?",
}

def format_date(datetime_obj, simple=False):
    if simple:
        return datetime_obj.strftime("%m-%d-%Y")
    return datetime_obj.strftime("%m/%d/%Y, %H:%M:%S")

class FileHandler(object):
    """Reads, writes, and looks up journal entry text files"""
    def __init__(self, entry):
        self.entry = entry # instance of an Entry object to handle
        self.filename = '{} {}.{}'.format(FILE_PREFIX, format_date(self.entry.date, simple=True), FILE_EXT)

    def write_entry(self):
        """
        Opens file and writes questions/answers in the format:

        Date

        **Question 1**
        Answer

        **Question 2**
        Answer

        etc.
        """
        p = JOURNAL_FOLDER / self.filename
        with p.open(mode='w') as f:
            f.write(format_date(self.entry.date) + '\n\n')
            for k, v in self.entry.answers.items():
                f.write('**{}**\n{}\n\n'.format(self.entry.questions[k], v))
        Prompt(self.entry).outro()


class Entry(object):
    """
    Collection of questions, user input answers, and date. self.answers has the following structure:
    {
        "one": "answer",
        "two": "answer",
    }
    """
    def __init__(self, questions=QUESTIONS):
        self.date = datetime.now()
        self.questions = questions
        self.answers = dict()

    def create(self):
        """Iterates through all available questions and adds user input to the answers dictionary"""
        prompt = Prompt()
        prompt.intro()
        for k, v in self.questions.items():
            answer = prompt.ask_question(v)
            self.answers[k] = answer


class Prompt(object):
    """Asks a question to command line and returns user's answer as a string"""
    def __init__(self, entry=None):
        self.entry = entry # instance of an Entry object to handle

    def intro(self):
        a_quote = Motivational()
        print("{} {} {} {} {}".format('\n\n', format_date(datetime.now()), '\n\n', a_quote.get(), '\n\n',))

    def ask_question(self, question):
        answer = input(question + ' ')
        return str(answer)

    def outro(self):
        print("{}Saved Journal Entry for {}, see you tomorrow! {}".format( \
            '\n', format_date(self.entry.date, simple=True),'\n'
        ))

if __name__ == '__main__':
    an_entry = Entry()
    an_entry.create()
    filer = FileHandler(an_entry)
    filer.write_entry()
