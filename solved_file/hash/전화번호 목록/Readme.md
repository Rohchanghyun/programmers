# <span style="color: #f0b752">전화번호 목록</span>

## <span style="color: #a6acec">내 풀이</span>

```python
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            return answer
            
    return answer
```

`phone_book` 을 문자열 순으로 sort 한 뒤 바로 앞의 문자열과 바로 뒤의 문자열을 비교한다(접두어만 비교하면 되기 때문)



## <span style="color: #a6acec">정답</span>

```python
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
```





## <span style="color: #a6acec">회고</span>

밑의 코드는 내가 처음 실행했을 때의 코드로, 20개의 테스트 중 13,14 항목에서 틀리고 효율성 테스트 4개중 3,4 에서 시간초과가 나왔다

```python
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] in phone_book[j]:
                answer = False
                return answer
            
    return answer
```

이때는 접두어만 비교하면 된다는 것을 몰라서 for문을 두번이나 쓰며 모든 문자열을 비교하였다. 

하지만 이후 문제를 파악하고 `startswith` 로 바로 다음의 문자열만 비교하여 답을 찾았더니 통과하였다