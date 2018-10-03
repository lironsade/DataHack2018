sen = 'Find two numbers whose sum is 62 and whose difference is 6.'
key_words_num = {'one':1, 'two':2, 'three':3}
key_words_op = {'difference':'-', 'sum':'+'}


def parse_sen():
    arr_sen = sen.split()
    my_equi = []
    # my_params =
    num_params = 0
    curr_op = ''
    for i, word in enumerate(arr_sen):
        if word in key_words_num.keys():
            num_params = key_words_num[word]
        if word in key_words_op.keys():
            curr_op = key_words_op[word]
        if word == 'is':
            create_smpl(num_params, curr_op, arr_sen[i+1])


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