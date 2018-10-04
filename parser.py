import spacy
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
    nlp_sen = nlp(sen)
    my_equis = []
    num_params = 0
    params = []
    curr_op = ''
    for i, word in enumerate(nlp_sen):
        if word.text in key_words_params:
            if nlp_sen[i-1].text in key_words_num.keys():
                num_params = key_words_num[nlp_sen[i-1].text]
            if nlp_sen[i-1].text.isdigit():
                num_params = nlp_sen[i-1].text
        if word.text in key_words_op.keys():
            curr_op = key_words_op[word.text]
        if word.text in key_words_create and is_num(nlp_sen[i+1].text):
            eq = create_eq(num_params, curr_op, rmv_non_digits(nlp_sen[i+1].text))
            if eq:
                my_equis.append(eq)
        if word.text == 'another':
            num_params += 1
    return my_equis


def create_params(sons):
    params = []
    num_params = -1
    for i in range(len(sons)):
        if sons[i].text in key_words_num:
            num_params = key_words_num[sons[i].text]
            for i in range(num_params):
                params.append(op_params[i])
        if sons[i].text == 'consecutive':
            params = consecutive(['x']*num_params)
        if sons[i].text == 'even':
            params = even(params)
        if sons[i].text == 'odd':
            params = odd(params)
    if num_params == -1:
        return []
    return params

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
    sen = 'what is one plus one'
    print(parse_sen(sen))
