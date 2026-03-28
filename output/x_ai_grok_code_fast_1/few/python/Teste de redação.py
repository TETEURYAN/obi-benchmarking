import sys
import random
import string

input_data = sys.stdin.read().split()
N = int(input_data[0])
M = int(input_data[1])

def generate_word():
    length = random.randint(1, 10)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

distinct_count = M // 2
distinct_words = set()
while len(distinct_words) < distinct_count:
    distinct_words.add(generate_word())

distinct_list = list(distinct_words)

total_words = random.randint(N, M)
additional_needed = total_words - distinct_count
if additional_needed > 0:
    for _ in range(additional_needed):
        distinct_list.append(random.choice(distinct_list))

random.shuffle(distinct_list)
print(' '.join(distinct_list))