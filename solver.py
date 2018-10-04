import sympy as sy


def solve(equations_lst, unkn_lst):
    """solves the problem from list of equation and list of Unknown values
    :param equations_lst: ['x+y = 40', '2*x+4*y = 108'] -> list of strings
    :param unkn_lst:  ['x', 'y'] -> list of strings
    :return: {(26,14)}' -> list of float or ints
    """
    unkn_lst_s = unkn_lst[:]
    s_case = False
    if handle_unkn(unkn_lst_s):
        s_case = True
        unkn_lst = ['x']
    A, b = sy.linear_eq_to_matrix(replace_equ(equations_lst), unkn_lst)
    sol = [eval(str(x)) for b in sy.linsolve((A, b), unkn_lst) for x in b]
    if not s_case:
        return sol
    return [eval(i.replace('x', str(sol[0]))) for i in unkn_lst_s]


def handle_unkn(unkn_lst):
    """
    :param unkn_lst: list of Unknown values
    :return: if this shit special
    """
    for i in unkn_lst:
        if len(i) > 1:
            return True
    return False


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
    for i, n in enumerate(unkn_lst):
        if i == 0:
            lst.append(n)
        else:
            lst.append(n + ' + ' + str(i))
    return lst


if __name__ == '__main__':
    equations_smp = ['2*(x) + 1+2*(x + 1) + 1+2*(x + 2) + 1=-273']
    s_unkn = ['2*(x) + 1', '2*(x + 1) + 1', '2*(x + 2) + 1']
    print(solve(equations_smp, s_unkn))
