def solution(participant, completion):
    part = {}
    for p in participant :
        if p in part.keys():
            part[p] += 1
        else:
            part[p] = 1
    for c in completion:
        if part[c] != 0:
            part[c] -= 1
    for key,value in part.items():
        if value == 1:
            answer = key
            
    return answer