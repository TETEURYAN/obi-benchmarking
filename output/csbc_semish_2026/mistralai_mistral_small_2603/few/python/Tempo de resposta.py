
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    records = []
    index = 1
    for _ in range(n):
        typ = data[index]
        x = int(data[index + 1])
        records.append((typ, x))
        index += 2

    time_elapsed = 0
    received = {}
    sent = {}
    waiting = {}
    response_times = {}
    last_time = 0

    for typ, x in records:
        if typ == 'T':
            time_elapsed += x
        else:
            if typ == 'R':
                received[x] = received.get(x, 0) + 1
                waiting[x] = waiting.get(x, 0) + 1
            elif typ == 'E':
                if x in waiting and waiting[x] > 0:
                    waiting[x] -= 1
                    if x in response_times:
                        response_times[x] += time_elapsed - last_time
                    else:
                        response_times[x] = time_elapsed - last_time
                sent[x] = sent.get(x, 0) + 1
            last_time = time_elapsed

    friends = set(received.keys()).union(set(sent.keys()))
    result = []
    for friend in sorted(friends):
        if friend in waiting and waiting[friend] > 0:
            result.append((friend, -1))
        else:
            total = response_times.get(friend, 0)
            result.append((friend, total))

    for friend, total in result:
        print(f"{friend} {total}")

if __name__ == "__main__":
    main()
