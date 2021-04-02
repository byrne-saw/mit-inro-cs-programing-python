s = '1.23,2.4,3.123'

def string_sum(s):
    split_string = s.split(',')
    string_summed = 0
    for i in split_string:
        string_summed = string_summed + float(i)
    # return string_summed
    print(string_summed)

string_sum(s)


