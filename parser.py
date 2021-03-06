import spacy
import solver
import re, copy
key_words_num = {'one':1, 'two':2, 'three':3, 'One':1, 'Two':2, 'Three':3, 'A':1, 'a':1}
key_words_op = {'difference':'-', 'sum':'+', 'exceeds':'-', 'less than':'-', 'less':'-', 'more':'-'}
key_words_params = {'numbers', 'number', 'integers', 'integer'}
key_words_create = {'of', 'is', 'by'}
op_params = ['x', 'y', 'z', 'w','a','b','c','d','e','f']
nlp = spacy.load('en_core_web_sm')

# nlp = spacy.load('en_core_web_sm')
# doc = nlp(u'If the first and third of three consecutive even integers are added, the result is 12 less than three times the second integer. find the integers')
# for token in doc:
#     print(token.text)
# print([token.text for token in doc[9].rights])  # ['on']
# print(doc[2].n_lefts)  # 2
# print(doc[2].n_rights)  # 1


def parse_sen(sen):
    """
    parses a mathematical question sentence into equations.
    """
    nlp = spacy.load('en_core_web_sm')
    is_another = ('another' in sen) or ('second' in sen)
    reg_times = 'than \d+ times'
    find_times = re.findall(reg_times, sen)

    params_found = False
    nlp_sen = nlp(sen.replace('  ', ' '))
    my_equis = []
    curr_op = ''
    params, unit_params = [], []

    for i, word in enumerate(nlp_sen):
        if word.text in key_words_params and not params_found:
            params = create_params(word.lefts)
            unit_params = copy.deepcopy(params)
            params_found = True
        if word.text in key_words_op.keys():
            curr_op = key_words_op[word.text]
        if word.text in key_words_create and is_num(nlp_sen[i+1].text):
            if is_another:
                params.append('y')
                unit_params.append('y')
                is_another = False
            if word.text == 'is' and curr_op == '':
                if find_times:
                    params[1] = rmv_non_digits(find_times[0]) + '*' + params[1]
                    find_times = []
                right_childs = list(word.rights)
                if right_childs and str(right_childs[0]) in key_words_op.keys():
                    curr_op = key_words_op[str(right_childs[0])]
                elif nlp_sen[i+2].text in key_words_op.keys():
                    curr_op = key_words_op[nlp_sen[i+2].text]
            elif curr_op == '':
                continue
            eq = create_eq(params, curr_op, rmv_non_digits(nlp_sen[i+1].text))
            if eq:
                my_equis.append(eq)
                curr_op = ''
    return my_equis, unit_params


def create_params(sons):
    params = []
    num_params = -1
    for son in sons:
        if son.text in key_words_num or is_num(son.text):
            if is_num(son.text):
                try:
                    num_params = int(son.text)
                except:
                    return []
            else:
                num_params = key_words_num[son.text]
            if num_params > 4:
                return []
            for i in range(num_params):
                params.append(op_params[i])
        if son.text == 'consecutive':
            params = solver.consecutive_num(['x']*num_params)
        if son.text == 'even':
            params = solver.even_num(params)
        if son.text == 'odd':
            params = solver.odd_num(params)
    if num_params == -1:
        return []
    return params


def create_eq(params, op, num):
    '''
    creates eq in the form of: param1 [op] param2 [op]... = num
    '''
    if not params or op == '':
        return

    equi = ''
    length = len(params)

    for i in range(length):
        equi += params[i]
        if i != length - 1:
            equi += op

    equi += '=' + num
    return equi


def is_num(s):
    return any(i.isdigit() for i in s)


def rmv_non_digits(num):
    return ''.join(i for i in num if i.isdigit() or i == '-')


if __name__ == '__main__':
    sen = 'A number is 12 less than another.  The sum of the numbers is 28.  find the Numbers.'
    # sen = 'The sum of two numbers is 91.  The larger number is 1 more than 4 times the smaller number. Find the numbers.'
    print(parse_sen(sen))
    # print(create_eq(['x', 'y'], '+', '6'))
    # print(key_words_op['less'])
