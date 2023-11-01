# Iterator and Generator
이터레이터와 제너레이터

## Iterator
값을 순차적으로 반환할 수 있는 객체
> **Iterable** : 반복할 수 있는 것 <br>
ex) 리스트, 딕셔너리, 문자열, 튜플 등

- 클래스를 사용하여 정의
- `__iter__()`와 `__next__()` 두 가지 메서드를 구현해야 함
- `__iter__()` 메서드는 이터레이터 자신을 반환
- `__next__()` 메서드는 다음 값을 반환하고, 더 이상 반환할 값이 없으면 **StopIteration** 예외를 발생

```python
class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value <= self.max_value:
            result = self.current_value
            self.current_value += 1
            return result
        else:
            raise StopIteration

my_iterator = MyIterator(3)
for num in my_iterator:
    print(num)
```

## Generator
이터레이터를 직접 만들 때 사용하는 코드
- `yield` 키워드를 사용하여 값을 반환
- 함수를 사용하여 정의
- 일반 함수와 달리, 함수를 호출해도 함수 내부의 코드가 실행되지 않음 (*Lazy Evaluation*)
- 메모리 효율적, 대량의 데이터를 다룰 때 유용

```python
# Generator expression1 - yield
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))
```


```python
# Generator expression2 - Generator comprehension
import time

def longtime_job():
    print("job start")
    time.sleep(1)
    return "done"

list_job = (longtime_job() for i in range(5))   # Generator comprehension
print(next(list_job))
```
<br>

###### Reference : https://wikidocs.net/134909