import spacy
import solver
key_words_num = {'one':1, 'two':2, 'three':3, 'One':1, 'Two':2, 'Three':3}
key_words_op = {'difference':'-', 'sum':'+', 'exceeds':'-', 'less than':'-'}
key_words_params = {'numbers', 'number', 'integers', 'integer'}
key_words_create = {'of', 'is', 'by'}
op_params = ['x', 'y', 'z', 'w']

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
    nlp_sen = nlp(sen.replace('  ', ' '))
    my_equis = []
    num_params = 0
    params = []
    curr_op = ''
    for i, word in enumerate(nlp_sen):
        if word.text in key_words_params:
            params = create_params(word.lefts)
        if word.text in key_words_op.keys():
            curr_op = key_words_op[word.text]
        if (word.text in key_words_create) and is_num(nlp_sen[i+1].text):
            eq = create_eq(params, curr_op, rmv_non_digits(nlp_sen[i+1].text))
            if eq:
                my_equis.append(eq)
        if word.text == 'another':
            params.append('y')
    return my_equis


def create_params(sons):
    params = []
    num_params = -1
    for son in sons:
        if son.text in key_words_num or is_num(son.text):
            if is_num(son.text):
                num_params = int(son.text)
            else:
                num_params = key_words_num[son.text]
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
    if not params:
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
    sen = 'The sum of 2 integers is 36. The difference of the same 2 numbers is 4. Find the integers.'
    # sen = 'The sum of three consecutive odd integers is -273. What are the integers?'
    print(parse_sen(sen))
    # print(create_eq(['x', 'y'], '+', '6'))
