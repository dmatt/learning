import os
import time

class Line():
    def __init__(self, length):
        self.length = length
        self.visual = length * '-'
    
    def print_line(self):
        print(self.visual)

class LineList():
    def __init__(self, *args):
        self.list = [Line(length) for length in args]
        self.length = len(self.list)

    def print_line_list(self):
        os.system('clear')
        print('\n\n')
        for line in self.list:
            line.print_line()
        time.sleep(.001)

    def bubble_sort(self):
        ignore_last_n = 0
        while ignore_last_n < self.length:
            for i in range(self.length - 1 - ignore_last_n):
                a = self.list[i]
                b = self.list[i + 1]
                if a.length > b.length:
                    self.list[i] = b
                    self.list[i + 1] = a
                self.print_line_list()
            ignore_last_n += 1

if __name__ == '__main__':
    a_line_list = LineList(15,1,3,6,8,12,23,29,34,5,12,7,42,54,23,1,11,10,3,4,7,8,3,2,9,8,7,6,1)
    a_line_list.print_line_list()
    a_line_list.bubble_sort()