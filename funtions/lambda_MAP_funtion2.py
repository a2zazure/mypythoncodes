def string_odd_even(string):
    if len(string)%2 == 0:
        return 'EVEN'
    else:
        return string[0]

string_list=['ram','sham','minakshi']

list_final=list(map(string_odd_even,string_list))
print(list_final)
