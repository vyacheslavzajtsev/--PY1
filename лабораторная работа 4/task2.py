def get_count_char(str_):
    str_ = str_.lower().split(' ')
    str_ = ''.join(str_)
    dict_ = {}
    for i in str_:
        if i.isalpha() and i not in dict_:
            dict_[i] = str_.count(i)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
d = get_count_char(main_str)


def get_count2(dict_):
    new = {}
    b = sum(dict_.values())
    for k in dict_:
        new[k] = int((dict_[k] / b) * 100)
    return new


print(get_count2(d))
