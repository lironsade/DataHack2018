import parser

def check_over_data(df):
    """
    :param df: data frame of panda's json
    :return: success rate, indexes of wrong answers
    """
    count = 0
    success = 0
    wrongs = []
    for index, row in df.iterrows():
        if row['id'].startswith("algebra"):
            count += 1
            equations = parser.parse_sen(row['text'])
            if check_element(equations, row['equations']):
                success += 1
            else:
                wrongs.append(index)
    return success/count, df, wrongs


def check_element(equations, label):
    """
    :return: return true if the equations matches the label
    """
    if len(equations) != len(label[1:]):
        return False
    for equ in equations:
        if "equ: " + equ not in label[1:]:
            return False
    return True
