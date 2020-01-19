"""A daily journal entry prompter that stores entries in a txt file"""

from datetime import datetime
from pathlib import Path
import argparse

from quotes import *

JOURNAL_FOLDER = Path('/Users/dmatt/Dropbox (Personal)/Daily Journal/')

FILE_PREFIX = 'Journal Entry '
FILE_EXT = 'txt'

# Questions come from this 5 Minute Journal system:
# https://www.intelligentchange.com/blogs/news/five-minute-journal-tips
QUESTIONS = [
    "I am greatful for...",
    "What would make today great?",
    "Daily affirmations: I am...",
    "3 amazing things that happened today...",
    "How could I have made today even better?",
]

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
        Quote

        **Question 1**
        Answer

        **Question 2**
        Answer

        etc.
        """
        p = JOURNAL_FOLDER / self.filename
        with p.open(mode='a+') as f:
            f.write(
                format_date(self.entry.date) + '\n' +
                str(self.entry.quote) + '\n\n'
            )
            for k, v in self.entry.answers.items():
                f.write('**{}**\n{}\n\n'.format(k, v))

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
        self.answers = dict()
        self.quote = Motivational()
        full_day = not (meridiem.a != meridiem.p)
        questions_sliced = questions[:3] if meridiem.a else questions[3:]
        self.questions = questions if full_day else questions_sliced


    def create(self):
        """Iterates through all available questions and adds user input to the answers dictionary"""
        prompt = Prompt()
        prompt.intro()

        for q in self.questions:
            answer = prompt.ask_question(q)
            self.answers[q] = answer


class Prompt(object):
    """Asks a question to command line and returns user's answer as a string"""
    def __init__(self, entry=None):
        self.entry = entry # instance of an Entry object to handle

    def intro(self):
        print("{}{}{}{}{}".format(
            '\n',
            format_date(datetime.now()),
            '\n',
            Motivational(),
            '\n',
        ))

    def ask_question(self, question):
        answer = input(question + ' ')
        return str(answer)

    def outro(self):
        later = "this evening" if meridiem.a else "tomorrow"
        print("{}Saved Journal Entry for {}, see you {}! {}".format(
            '\n', format_date(self.entry.date, simple=True),
            later,
            '\n'
        ))

if __name__ == '__main__':    
    parser = argparse.ArgumentParser(description='Use -a for AM and -p for PM')
    parser.add_argument("-a", help="This is the AM variable", action="store_true", default=False)
    parser.add_argument("-p", help="This is the PM variable", action="store_true", default=False)
    # Does the user want AM or PM?
    meridiem = parser.parse_args()

    an_entry = Entry()
    an_entry.create()
    filer = FileHandler(an_entry)
    filer.write_entry()
