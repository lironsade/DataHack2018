import model
import pandas as pd

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
            ans = model.solve_problem(row['text'])
            df[index]['my_ans'] = ans
            if check_ans(ans, row['ans']):
                success += 1
            else:
                wrongs.append(index)
    return success/count, df, wrongs

def check_ans(ans, ans_label):
    if len(ans) != len(ans_label):
        return False
    for answer in ans:
        if answer not in ans:
            return False
    return True

def check_equations(equations, equation_label):
    """
    :return: return true if the equations matches the label
    """
    if len(equations) != len(equation_label[1:]):
        return False
    for equ in equations:
        if "equ: " + equ not in equation_label[1:]:
            return False
    return True

tags = ['id', 'text', 'ans']
df = pd.read_json("data/number_word_std.dev.json")