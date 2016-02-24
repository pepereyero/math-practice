# -*- coding: utf-8 -*-
"""mathpractice.sequence

Practice remembering sequences.
"""
from __future__ import division

import numpy as np
import random
import time
import pickle
import os.path
import sympy


#---------------------------------------------------------------------

class Problem(object):
    def __init__(self, history_file, good_for_next_level):
        self.history_file = history_file
        self.good_for_next_level = good_for_next_level
        if not os.path.exists(history_file):
            with open(history_file, 'wb') as fd:
                pickle.dump({'history': [(0, False)]}, fd)

    def _check_list(self, lst):
        """Checks if all the the elements[1] of all the elements
        in the list are True.
        """
        if all([l[1] for l in lst]):
            return True
        return False

    def check_history(self, history):
        """Checks if all the last five elemnts in the list
        are True.
        """
        if len(history) >= self.good_for_next_level:
            return self._check_list(history[-self.good_for_next_level:])
        return False

    def level_from_history(self):
        """Returns the level in which the user is based on the previous
        history: if the last 5 are correct adds one to the level.
        """
        with open(self.history_file, 'rb') as fd:
            history = pickle.load(fd)['history']
            if self.check_history(history):
                self.last_level = history[-1][0] + 1
            else:
                self.last_level = history[-1][0]
            return self.last_level

    def store_answer(self, correct):
        """Saves a pocket in a key in the dic of the
        file. The name of the 'key' is the name of the text.
        """

        with open(self.history_file, 'rb') as fd:
            dic = pickle.load(fd)
            dic['history'].append((self.last_level, correct))

        with open(self.history_file, 'wb') as fd:
            pickle.dump(dic, fd)

    def create_question(self):
        """Creates the question according to the user's history, which is a
        list that contains tuples (level, achieved), like
        [(0, True), (0, True), (1, True), (1, False)]
        """

        return self.build_question(self.level_from_history())

    def check_answer(self, answer):
        """Checks if the answer is correct, and stores the result.
        """

        correct = self.is_correct(answer)
        self.store_answer(correct)
        return correct


class MemorySequence(Problem):
    def __init__(self, history_file='mem-seq.pkl', good_for_next_level=5):
        super(MemorySequence, self).__init__(history_file, good_for_next_level)
        self.sequence = None
        self.levels = {0: (3, 10),
                       1: (4, 10),
                       2: (4, 20)}
        self.ask_type = show_off_ask
        self.ask_inputs = (5) #5 = show time.
        self.print_mode = None

    def _create_sequence(self, length, s_range):
        """Returns a sequence of numbers of length
        <length> made out with numbers in the range
        of <s_range>

        >>> set_num_sequence(3, [9, 45])
        [40, 37, 24]
        """

        self.sequence = [random.randint(1, s_range) for n in range(length)]
        return self.sequence

    def build_question(self, level):
        """Creates the question according to the user's history, which is a
        list that contains tuples (level, achieved), like
        [(0, True), (0, True), (1, True), (1, False)]
        """

        if level in self.levels:
            length, s_range = self.levels[level]
        else:
            length, s_range = level+2, level*10
        return self._create_sequence(length, s_range)

    def is_correct(self, answer):
        """Checks if an answer is correct.

        >>> check_answer([1, 2, 4], "1, 2, 3")
        False
        """

        sequence = self.sequence
        try:
            if [int(i) for i in answer.replace(',', ' ').split()] == sequence:
                return True
        except:
            pass
        return False


class TimedFunctions(Problem):
    def __init__(self, history_file='time-functions.pkl', good_for_next_level=5):
        super(TimedFunctions, self).__init__(history_file, good_for_next_level)
        self.fraction = None
        self.levels = {0: (5, 10, 10, 2), #den range, num range, time, length
                       1: (10, 20, 15, 2),
                       2: (15, 22, 20, 3)}
        self.ask_type = ask_with_time

    def _get_single_fraction(self, den_range, nom_range):
        """Gets a single fraction in form of a two elements tuple,
        the first element is the numerator and the second element is
        the denominator.
        """
        return (random.randint(-nom_range, nom_range),
                random.randint(-den_range, den_range))

    def _get_fraction_operation(den_range, num_range, length):
        pass


class SimpleFirstSecondOrder(Problem):
    def __init__(self, history_file='simple-first-second-order-eq.pkl', good_for_next_level=5):
         super(SimpleFirstSecondOrder, self).__init__(history_file, good_for_next_level)
         self.equation = None
         self.levels = {0: (2, 5, 5), #range,  time
                        1: (6, 7, 6),
                        2: (12, 14, 8)}
         self.ask_type = ask_with_time
         self.ask_inputs = None
         self.print_mode = equation_formating

    def _get_equation(self, range1, range2, order):
        """Gets a simple equation. If the input <order> is 'first',
        assigns o self.sequence a first order equation otherwise
        a second order equation.
        """
        x = sp.var('x')
        if order == 'first':
            self.equation = randint(-range1, range1) * (x + randint(-range2, range2))
        else:
            self.equation = randint(-a, a) * (x + randint(-b, b)) * (x + randint(-b, b))
        return self.equation

    def _formating(self):
        """Formats an equation like the one preduced by _get_equation so
        that it can be printed"""

        return str(self.equation) + ' = 0'

    def _get_result(self):
        return sp.solve(self.equation, x)

    def build_question(self, level):
        """Gets a simple first order equation based on the level, which
        is worked out by the history of previous attempts. """

        if level in self.levels:
            range1, range2, self.ask_inputs = self.levels[level]
        else:
            range1, range2, self.ask_inputs = level*6, level*7, level+6
        return self._get_equation(range1, range2, random.choice(['first', 'second']))

    def check_answer(self, answer):
        solution = _get_result(self)





def show_off():
    for e in range(70):
        print

def regular_ask(question):
        return raw_input('Solve ' + str(question) + ' : ')

def show_off_ask(question,  max_time):
        """Asks for a sequence: first of all prints out the
        sequence for a determinate period of time (memorization
        time). And then asks the user to enter the previously
        shown sequence.
        """

        print question
        time.sleep(max_time)
        show_off()
        return raw_input("Enter the sequence: ")

def ask_with_time(question, answer_time):
        """Asks giving the user a determinate time to answer the quesion
        """

        answer = regular_ask(question)
        time.sleep(answer_time)
        show_off()
        return answer


class RawInputUserInterface(object):
    def __init__(self, problem):
        self.problem = problem

    def ask_once(self, question):
        return self.problem.ask_type(question, self.problem.ask_inputs)

    def practice(self, togo=problem.good_for_next_level-1):
        question = self.problem.create_question()
        answer = self.ask_once(question)
        if answer == 'exit':
            return 'Well done!'

        grade = self.problem.check_answer(answer)
        if grade is True:
            if togo == 0:
                print 'You pass to the next level!! \n'
                togo = 5
            else:
                togo -= 1
                print '%d togo' % togo
        else:
            print 'Incorrect.'
            togo = 5
            print '5 to go.'
        return self.practice(togo)

def math_practice(exercise_type):
    problem = exercise_type()
    m_practice = RawInputUserInterface(problem)
    print m_practice.practice()


#-------------------------------------------------------


def _doctest():
    import doctest
    random.seed(0)
    doctest.testmod()


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)

    # https://docs.python.org/3.3/howto/argparse.html
    parser.add_argument('-t', '--test', help='run tests', action="store_true")
    #parser.add_argument('-l', '--length', help='sequence length', type=int)
    #parser.add_argument('-r', '--range', help='sequence range', type=str)
    # parser.add_argument('astring', help='a positional (mandatory) argument')
    args = parser.parse_args()
    if args.test:
        _doctest()
    else:
        #print tuple(args.range.split(','))
        #print args.length, args.range
        #print ask_all(args.length, tuple([int(i) for i in args.range.split(',')]))
        math_practice(MemorySequence)



if __name__ == '__main__':
    main()

#print ask_all(3, (1, 10))
