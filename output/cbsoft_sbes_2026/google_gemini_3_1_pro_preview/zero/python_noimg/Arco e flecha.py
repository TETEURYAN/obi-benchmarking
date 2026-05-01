
import sys
from bisect import bisect_right

class SortedList:
    def __init__(self):
        self.buckets = []
        self.bucket_size = 1000

    def add(self, val):
        if not self.buckets:
            self.buckets.append([val])
            return
        
        for i, bucket in enumerate(self.buckets):
            if val <= bucket[-1]:
                idx = bisect_right(bucket, val)
                bucket.insert(idx, val)
                if len(bucket) > self.bucket_size * 2:
                    self.split(i)
                return
        
        self.buckets[-1].append(val)
        if len(self.buckets[-1]) > self.bucket_size * 2:
            self.split(len(self.buckets) - 1)

    def split(self, i):
        bucket = self.buckets[i]
        mid = len(bucket) // 2
        new_bucket = bucket[mid:]
        del bucket[mid:]
        self.buckets.insert(i + 1, new_bucket)

    def count_less_equal(self, val):
        count = 0
        for bucket in self.buckets:
            if val >= bucket[-1]:
                count += len(bucket)
            else:
                count += bisect_right(bucket, val)
                break
        return count

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    
    sl = SortedList()
    
    P = 0
    out = []
    
    idx = 1
    for _ in range(N):
        X = int(input_data[idx])
        Y = int(input_data[idx+1])
        idx += 2
        
        XR = X + P
        YR = Y + P
        
        dist_sq = XR * XR + YR * YR
        
        P = sl.count_less_equal(dist_sq)
        out.append(str(P))
        
        sl.add(dist_sq)
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
