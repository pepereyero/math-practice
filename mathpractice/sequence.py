# -*- coding: utf-8 -*-
"""mathpractice.sequence

Practice remembering sequences.
"""
from __future__ import division

import numpy as np
import random
import time


def set_first_dic(fname):
    """Sets an empty diccionary in an empty
    file"""
    pickle.dump({}, open(fname, "wb"))


def load_dic():
    """Loads the pickle dic from a file.
    """
    return pickle.load( open( "d_d.pkl", "rb" ) )


def save_new_dic(dic, name):
    """Saves a sub_dic(keys_dic) in the dic of the
    file. The name of the 'key' is the name of the text.
    """
    keys_dic = load_dic()
    keys_dic[name] = dic
    pickle.dump( keys_dic, open( "d_d.pkl", "wb" ) )


def set_num_sequence(length, s_range):
    """Returns a sequence of numbers of length
    <length> made out with numbers in the range
    of <s_range>

    >>> set_num_sequence(3, (9, 45))
    [40, 37, 24]
    """
    return [random.randint(s_range[0], s_range[1]) for n in range(length)]


def show_off():
    for e in range(100):
        print


def ask_num_sequence(sequence, memorization_time):
    """Asks for a sequence: first of all prints out the
    sequence for a determinate period of time (memorization
    time). And then asks the user to enter the previously
    shown sequence.
    """
    print sequence
    time.sleep(memorization_time)
    show_off()
    return raw_input("Enter the sequence: ")


def check_answer(sequence, answer):
    """Checks if a answer is correct.

    >>> check_answer([1, 2, 4], "1, 2, 3")
    False
    """
    if answer.split(', ') == sequence:
        return True
    return False



def _doctest():
    import doctest
    random.seed(0)
    doctest.testmod()


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)

    # https://docs.python.org/3.3/howto/argparse.html
    parser.add_argument('-t', '--test', help='run tests', action="store_true")
    parser.add_argument('-n', '--number', help='a number', type=int)
    #parser.add_argument('astring', help='a positional (mandatory) argument')
    args = parser.parse_args()
    if args.test:
        _doctest()
    else:
        print args.astring


if __name__ == '__main__':
    main()
