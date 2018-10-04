import sympy as sy


def solve(equations_lst, unkn_lst):
    """solves the problem from list of equation and list of Unknown values
    :param equations_lst: ['x+y = 40', '2*x+4*y = 108'] -> list of strings
    :param unkn_lst:  ['x', 'y'] -> list of strings
    :return: {(26,14)}' -> FiniteSet of Integers
    """
    A, b = sy.linear_eq_to_matrix(replace_equ(equations_lst), unkn_lst)
    return sy.linsolve((A, b), unkn_lst)


def replace_equ(equations_lst):
    """
    :param equations_lst: list of equations
    :return: list of equations without "="
    """
    return [(s.replace("=", "-(") + ')') for s in equations_lst]


def even_num(unkn_lst):
    """
    :param unkn_lst: list of Unknown values
    :return: return the Unknown values in even form
    """
    return ["2*(" + n + ")" for n in unkn_lst]


def odd_num(unkn_lst):
    """
    :param unkn_lst: list of Unknown values
    :return: return the Unknown values in odd form
    """
    return ["2*(" + n + ') + 1' for n in unkn_lst]


def consecutive_num(unkn_lst):
    """
    :param unkn_lst: list of Unknown values
    :return: Returns disappear in consecutive form
    """
    lst = []
    counter = 1
    for n in unkn_lst:
        lst.append(n + ' + ' + str(counter))
        counter += 1
    return lst


if __name__ == '__main__':
    equations_smp = ['(2*k-2)+(2*k+2)=3*(2*k)-12']
    # print(replace_equ(equations_smp))
    unkn = ['2*k-2', '2*k', '2*k+2']
    print(solve(equations_smp, unkn))
    # print(solve(equations_smp, unkn))
