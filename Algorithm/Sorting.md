# 정렬 알고리즘
버블, 삽입, 선택 정렬
## 버블 정렬
- 시간 복잡도: `O(n^2)`
- 공간 복잡도: 제자리 정렬 알고리즘
- 작은 데이터셋에 적합

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
``` python
# 버블 정렬 사용 예시
arr_bubble = [64, 34, 25, 12, 22, 11, 90]
sorted_arr_bubble = bubble_sort(arr_bubble)
print("버블 정렬 결과:", sorted_arr_bubble)
```

## 삽입 정렬
- 시간 복잡도 최악:`O(n^2)`, 최선:`O(n)`
- 공간 복잡도: 제자리 정렬 알고리즘
- 작은 데이터셋에 적합
- 거의 정렬 되어 있을 때 효과적!

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

```python
# 삽입 정렬 사용 예시
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = insertion_sort(arr)
print("정렬 결과:", sorted_arr)
```

## 선택 정렬
- 시간 복잡도: `O(n^2)`
- 공간 복잡도: 제자리 정렬 알고리즘
- 그냥 비효율적

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```
``` python
# 선택 정렬 사용 예시
arr_selection = [64, 34, 25, 12, 22, 11, 90]
sorted_arr_selection = selection_sort(arr_selection)
print("선택 정렬 결과:", sorted_arr_selection)
```