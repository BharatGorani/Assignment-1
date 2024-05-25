import itertools
string_to_use = input()

def print_new_list(string_to_use):
    list_to_print = [] 
    for k,g in itertools.groupby(string_to_use):
        g = len(list(g))
        list_to_print.append((int(g),int(k)))  
    print(*list_to_print,sep=" ")

print_new_list(string_to_use)
