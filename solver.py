# input: ['x+y - 40', '2*x+4*y - 108'], ['x', 'y']
# output: '{26;14}'

import sympy


def main(equations_lst, unkn_lst):
    A, b = build_matrix(equations_lst, unkn_lst)
    sol = solver(A, b, unkn_lst)
    return sol


def build_matrix(equations_lst, unkn_lst):
    return sympy.linear_eq_to_matrix(equations_lst, unkn_lst)


def solver(A, b, unkn_lst):
    return sympy.linsolve((A, b), unkn_lst)


equations = ['x+y - 40', '2*x+4*y - 108']
unkn = ['x', 'y']
print(main(equations, unkn))
