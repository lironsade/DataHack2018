import re
key_words_num = {'one':1, 'two':2, 'three':3}
key_words_op = {'difference':'-', 'sum':'+', 'exceeds':'-', 'less than':'-'}
key_words_params = {'numbers', 'number', 'integers', 'integer'}
key_words_create = {'of', 'is', 'by'}


def parse_sen(sen):
    """
    parses a mathematical question sentence into equations.
    """
    sen = sen.lower() # lowercase
    arr_sen = sen.replace('  ', ' ').split() # breakdown to words
    # arr_sen = [x.lower() for x in arr_sen]
    my_equis = []
    num_params = 0
    curr_op = ''
    for i, word in enumerate(arr_sen):
        if word in key_words_params:
            if arr_sen[i-1] in key_words_num.keys():
                num_params = key_words_num[arr_sen[i-1]]
            elif arr_sen[i-1].isdigit():
                num_params = arr_sen[i-1]
        elif word in key_words_op.keys():
            curr_op = key_words_op[word]
        elif (word in key_words_create) and is_num(arr_sen[i+1]):
            eq = create_eq(num_params, curr_op, rmv_non_digits(arr_sen[i+1]))
            if eq:
                my_equis.append(eq)
        elif word == 'another':
            num_params += 1
    return my_equis


def create_eq(num_params, op, num):
    '''
    creates eq in the form of: param1 [op] param2 [op]... = num
    '''
    optional_params = ['x', 'y', 'z']
    equi = ''

    for i in range(num_params):
        equi += optional_params[i]
        if i != num_params - 1:
            equi += op

    equi += '=' + num
    return equi


def is_num(s):
    return any(i.isdigit() for i in s)


def rmv_non_digits(num):
    return ''.join(i for i in num if i.isdigit() or i == '-')


if __name__ == '__main__':
    sen = 'one number exceeds another by -5, and their sum is 29; find them.'
    print(parse_sen(sen))
