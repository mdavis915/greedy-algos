import sys
from collections import deque, OrderedDict

def fifo(reqs, capacity):
    cache = set()
    queue = deque()
    count = 0

    for page in reqs:
        if page not in cache:
            count += 1
            if len(cache) == capacity:
                removed = queue.popleft()
                cache.remove(removed)
            cache.add(page)
            queue.append(page)

    return count

def lru(reqs, capacity):
    cache = OrderedDict()
    count = 0

    for page in reqs:
        if page in cache:
            cache.move_to_end(page)
        else:
            count += 1
            if len(cache) == capacity:
                cache.popitem(last=False)
            cache[page] = 1

    return count

def main():
    if len(sys.argv) < 2:
        print("Usage: python cache_sim.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        k, m = map(int, f.readline().split())
        reqs = list(map(int, f.readline().split()))

    print(f"FIFO  : {fifo(reqs, k)}")
    print(f"LRU   : {lru(reqs, k)}")

main()