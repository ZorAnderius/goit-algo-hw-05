def binary_search(arr: list, key: int) -> int:
    low = 0
    hight = len(arr) - 1
    mid = 0
    steps = 0
    nearest_elem = None
    while low <= hight:
        mid = (low + hight) // 2
        steps += 1
        
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            nearest_elem = arr[mid]
            hight = mid - 1
        else:
            return (steps, arr[mid])
        
    return (steps, nearest_elem) if nearest_elem else (steps, arr[-1])

def task2():
    numbers = [-1, 3.9, 5.6, 8.1, 10, 12, 15, 18, 20, 22, 24]
    print(binary_search(numbers, 80.2))

if __name__ == '__main__':
    task2()