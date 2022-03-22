#! /usr/bin/env python3

#importing packages

import re
import sys

def Darwin(string, object, ln):
    """

    Assigning variables

    string = Defining the pattern we are searching for, in this case it is any 
    word that has herit in the middle

    object is just compliling and telling it to ignore case

    ln is setting the line number = 0 outside of the loop

    ------

    Using "with open" to open a file as either reading "r" or writing "w"

    Creating a new file called herit to store the output of the code.
    in this file sshould be every instance of a word containing "herit" in either upper or 
    lower case and the line it is on with a tab seperation.

    ------

    Example
    471     Inheritance
    660     inherited
    """
    print('Opening origin.txt')
    with open('origin.txt', 'r') as in_stream:
        print('Opening output.txt')
        with open('herit.txt', 'w') as out_stream:
            for line in in_stream:
                line = line.strip()
                ln = ln + 1
                word_list = line.split()
                all = object.findall(line)

                for i in all:
                    out_stream.write(str(ln) + '\t{0}\n'.format(i))
    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('herit.txt is closed?', out_stream.closed)

if __name__ == '__main__':
    ln = 0
    string = r'[\w]*herit[\w]*'
    object = re.compile(string, re.IGNORECASE)
    Darwin(string, object, ln)

