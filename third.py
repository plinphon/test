def solution(word):
    if len(word)==1 or len(word)==2:
        return word
    else:
        return solution(word[1:-1])
    
print(solution("fefeefffb"))
