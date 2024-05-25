
def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    str_len = len(string)
    
    for index, sub in enumerate(string):
        if sub in ["A", "E", "I", "O", "U"]:
            kevin_score += str_len - index
        else:
            stuart_score += str_len -index
    
    if kevin_score == stuart_score:
        print("Draw")
    elif kevin_score > stuart_score:
        print(f'Kevin {kevin_score}')
    else:
        print(f'Stuart {stuart_score}')

if __name__ == '__main__':
    s = input()
    minion_game(s)