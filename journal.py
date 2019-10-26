"""A daily journal entry prompter that stores entries in a txt file"""

from datetime import datetime
from pathlib import Path

JOURNAL_FOLDER = Path('/Users/dmatt/Desktop/Daily\ Journal/')
FILE_PREFIX = 'Journal Entry '
FILE_EXT = '.txt'
# Questions come from this 5 Minute Journal system https://www.intelligentchange.com/blogs/news/five-minute-journal-tips
QUESTIONS = {
    'one': "I am greatful for...",
    'two': "What would make today great?",
    'three': "Daily affirmations: I am...",
    'four': "3 amazing things that happened today...",
    'five': "How could I have made today even better?",
}

class FileHandler(object):
    """Reads, writes, and looks up journal entry text files"""
    def __init__(self, entry):
        self.entry = entry
        self.filename = FILE_PREFIX + str(entry.date) + FILE_EXT

    def write_entry(self):
        with open(JOURNAL_FOLDER / self.filename, w) as f:
            f.write(entry.date + '\n')
            for k, v in self.entry.answers.items():
                f.write('**{}**\n{}\n\n'.format(self.entry.questions[k], v))


class MotivationalQuote(object):
    def __init__(self):
        self.quote = 'You are alive, that is pretty OK!'
        self.by = 'Unknown'

    def get(self):
        return "\"{}\" – {}".format(self.quote, self.by)

    def get_new(self):
        # TODO: Get this from the internets
        pass


class Entry(object):
    """Collection of questions, user input answers, and date. self.answers has the following structure:

    {
        "one": "answer",
        "two": "answer",
    }

    """
    def __init__(self, questions=QUESTIONS):
        self.date = datetime.now()
        self.answers = dict()
        self.questions = questions

    def create(self):
        """Iterates through all available questions and adds user input to the answers dictionary"""
        prompt = Prompt()
        prompt.intro()
        for k, v in self.questions.items():
            answer = prompt.ask_question(v)
            self.answers[k] = answer


class Prompt(object):
    """Supports asking a question to command line and returns an answer"""
    def intro(self):
        a_quote = MotivationalQuote()
        print("{} {}".format(datetime.now(), a_quote.get()))

    def ask_question(self, question):
        answer = input(question + ' ')
        return str(answer)


if __name__ == '__main__':
    an_entry = Entry()
    an_entry.create()
    filer = FileHandler(an_entry)
    filer.write_entry()
