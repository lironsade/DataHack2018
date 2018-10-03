sen = 'one number exceeds another by 5, and their sum is 29; find them.'
key_words_num = {'one':1, 'two':2, 'three':3}
key_words_op = {'difference':'-', 'sum':'+', 'exceeds':'-'}
key_words_params = {'numbers', 'number', 'integers', 'integer'}
key_words_create = {'of', 'is', 'by'}


def parse_sen():
    arr_sen = sen.split()
    arr_sen = [x.lower() for x in arr_sen]
    num_params = 0
    curr_op = ''
    for i, word in enumerate(arr_sen):
        if word in key_words_params:
            if arr_sen[i-1] in key_words_num.keys():
                num_params = key_words_num[arr_sen[i-1]]
            if arr_sen[i-1].isdigit():
                num_params = arr_sen[i-1]
        if word in key_words_op.keys():
            curr_op = key_words_op[word]
        if (word in key_words_create) and num_there(arr_sen[i+1]):
            create_smpl(num_params, curr_op, rmv_non_digits(arr_sen[i+1]))
        if word == 'another':
            num_params += 1


def num_there(s):
    return any(i.isdigit() for i in s)


def rmv_non_digits(num):
    return ''.join(i for i in num if i.isdigit())


def create_smpl(num_params, op, num):
    optional_params = ['x', 'y', 'z']
    equi = ''

    for i in range(num_params):
        equi += optional_params[i]
        if i != num_params - 1:
            equi += op

    equi += '=' + num
    print(equi)

parse_sen()