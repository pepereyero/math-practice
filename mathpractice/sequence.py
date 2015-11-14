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


#---------------------------------------------------------------------

class Problem(object):
    def __init__(self, history_file):
        self.history_file = history_file
        if not os.path.exists(history_file):
            with open(history_file, 'wb') as fd:
                pickle.dump({'history': [(0, False)]}, fd)

    def level_from_history(self):
        with open(self.history_file, 'rb') as fd:
            history = pickle.load(fd)['history']
            self.last_level = history[-1][0] + 1
            return self.last_level

    def store_answer(self, correct):
        """Saves a pocket in a key in the dic of the
        file. The name of the 'key' is the name of the text.
        """
        with open(fname, 'rb') as fd:
            dic = pickle.load(fd)
            dic['history'].append((self.last_level, correct))

    def create_question(self):
        """Creates the question according to the user's history, which is a
        list that contains tuples (level, achieved), like
        [(0, True), (0, True), (1, True), (1, False)]
        """
        ### si has hecho n seguidos achieved pasas al siguiente.
        return self.build_question(self.level_from_history())

    def check_answer(self, answer):
        correct = self.is_correct(answer)
        self.store_answer(correct)
        return correct


class MemorySequence(Problem):
    def __init__(self, history_file='mem-seq.pkl'):
        super(MemorySequences, self).__init__(history_file)
        self.sequence = None
        self.levels = {0: (3, 10),
                       1: (4, 10),
                       2: (4, 20)}

    def _create_sequence(self, length, s_range):
        """Returns a sequence of numbers of length
        <length> made out with numbers in the range
        of <s_range>

        >>> set_num_sequence(3, [9, 45])
        [40, 37, 24]
        """
        self.sequence = [random.randint(s_range[0], s_range[1]) for n in range(length)]
        return self.sequence

    def build_question(self, level):
        """Creates the question according to the user's history, which is a
        list that contains tuples (level, achieved), like
        [(0, True), (0, True), (1, True), (1, False)]
        """
        if level in self.levels:
            lenth, s_range = self.levels[level]
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
            if [int(i) for i in answer.split()] == sequence:
                return True
        except:
            pass
        return False



class RawInputUserInterface(object):
    def _init(self, problem):
        self.problem = problem

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

    def show_off():
        for e in range(70):
            print


    def ask_all(length, s_range, n_questions, memorization_time=2, corrects=0, counter=0):
        if counter == n_questions:
            return corrects
        sequence = set_num_sequence(length, s_range)
        answer = ask_num_sequence(sequence, memorization_time)
        if check_answer(sequence, answer):
            return ask_all(length, s_range, n_questions,
                           memorization_time, corrects+1, counter+1)
        return ask_all(length, s_range, n_questions, memorization_time, corrects, counter+1)


    def check_dic(scores_file):
        if not os.path.exists(scores_file):
            set_first_dic(scores_file)
        last_score_dic = load_dic(scores_file)
        if 'last score' not in last_score_dic:
            return None
        return last_score_dic['last score']


    def practice():
        scores_file = "sequence_scores.pkl"
        last_score = check_dic(scores_file)
        if last_score is None:
             last_score = {'length':3, 's_range':[1, 10], 'corrects':None}
        n_questions = 2
        corrects = ask_all(last_score['length'], last_score['s_range'], n_questions)
        if corrects == n_questions:
            print "Well done, %d out of %d! You get to the next level" % (n_questions,
                                                                          n_questions)
            last_score['length'] += 1
            save_dic('last score', last_score, scores_file)
        else:
            print "You have to get all %d correct to get to the next level" % n_questions
            save_dic('last score', last_score, scores_file)



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
        print practice()



if __name__ == '__main__':
    main()

#print ask_all(3, (1, 10))
