# Useage:
# solve_problem(sentence)

from parser import parse_sen
from solver import solve

def solve_problem(sen):
    '''
    returns a set of numbers that should be the result of the sentence.
    '''
    eqs = parse_sen(sen)
    return solve(eqs, ['x', 'y'])


if __name__ == '__main__':
    sen = 'the sum of two numbers is 68. their difference is 16. what are the numbers?'
    print(solve_problem(sen))
