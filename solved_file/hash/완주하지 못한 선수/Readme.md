# <span style="color: #f0b752">완주하지 못한 선수</span>

## <span style="color: #a6acec">내 풀이</span>

```python
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
```

- `part` : dict 타입
	- <span style="color: #88c8ff">key</span> = 참여한 사람
	- <span style="color: #ed6663">value</span> = 같은 이름의 사람 수

`participant` 리스트에서 key,value 를 받아와 저장한다

`completion` 리스트에서 iter 를 돌며 같은 이름이 있는 key 의 value 를 -1 한다

그 후 part 에 만약 value 가 1이 남아있다면 answer 에 string 타입으로 저장한다

## <span style="color: #a6acec">정답</span>

```python
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```





## <span style="color: #a6acec">회고</span>

밑의 코드는 내가 처음 실행했을 때의 코드로, 효율성 테스트에서 5개 테스트 전부 다 시간초과가 나왔다.

```python
def solution(participant, completion):
    answer = ''
    for a in completion:
        if a in participant:
            participant.remove(a)
    answer = participant[0]
    return answer
```

원인으로 생각한 코드는 

```python
for a in completion:
        if a in participant:
            participant.remove(a)
```

여기에서 시간 복잡도가 많이 올라갔을 것이라고 판단하여 iter 를 돌며 list 내에 string 을 제거하는 방법보다는 dict 타입에서 value 를 count 하는것이 더 빠를 것이라고 판단했다