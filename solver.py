# input: ['x+y - 40', '2*x+4*y - 108'] -> list of strings, ['x', 'y'] -> list of strings
# output: '{(26,14)}' -> set of intgers

import sympy as sy


def solver(equations_lst, unkn_lst):
    A, b = build_matrix(equations_lst, unkn_lst)
    solution = set(sol(A, b, unkn_lst))
    return solution


def build_matrix(equations_lst, unkn_lst):
    return sy.linear_eq_to_matrix(equations_lst, unkn_lst)


def sol(A, b, unkn_lst):
    return sy.linsolve((A, b), unkn_lst)


if __name__ == '__main__':
    equations = ['x+y - 40', '2*x+4*y - 108']
    unkn = ['x', 'y']
    print(set(solver(equations, unkn)))
