# input: ['x+y = 40', '2*x+4*y = 108'] -> list of strings, ['x', 'y'] -> list of strings
# output: '{(26,14)}' -> FiniteSet of Integers

import sympy as sy


def solve(equations_lst, unkn_lst):
    A, b = sy.linear_eq_to_matrix(replace_equ(equations_lst), unkn_lst)
    return sy.linsolve((A, b), unkn_lst)


def replace_equ(equations_lst):
    lst = []
    for equ in equations_lst:
        s = equ.replace("= ", "-(")
        s += ')'
        lst.append(s)
    return lst


if __name__ == '__main__':
    equations_smp = ['x+y = 40', '2*x+4*y = 108']
    unkn = ['x', 'y']
    print(solve(equations_smp, unkn))
