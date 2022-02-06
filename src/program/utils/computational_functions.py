from collections import deque
import random
import time
# binary
# for binary insertion sort
# returns index where target should go in the list
# all elements are unique
def binary_search(data, target):
    low = 0
    high = len(data)
    if target < min(data):
        return 0
    elif target > max(data):
        return len(data)
    else:
        while True:
            mid = (high+low) // 2
            if data[mid] < target < data[mid+1]:
                return mid+1
            elif target < data[mid]:
                high=mid
            elif target > data[mid]:
                low=mid
            else:
                return 'error: input list was not a set'

def binary_insertion_sort(data):
    queue = deque(data)
    sorted = [queue.popleft()]
    # could this be while queue?
    while queue:
        item = queue.popleft()
        index = binary_search(sorted, item)
        bigger = sorted[index:]
        del sorted[index:]
        sorted.append(item)
        sorted.extend(bigger)
    return sorted

#  list = set([random.randint(1, 1000) for i in range(100)])
#  t1 = time.time()
#  l1 = binary_insertion_sort(list)
#  t2 = time.time()
#  l2 = sorted(list)
#  t3 = time.time()
#  print(t2-t1)
#  print(t3-t2)
#  print(l1 == l2)
