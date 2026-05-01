import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    
    records = []
    for _ in range(n):
        typ = data[idx]; idx += 1
        x = int(data[idx]); idx += 1
        records.append((typ, x))
    
    # Process records to assign timestamps to events
    # Events are R and E records
    # Between consecutive events, if no T record, 1 second passed
    # T records between events specify the time between them
    
    # We need to track time carefully
    # current_time starts at 0
    # For each event, we need to know its timestamp
    
    # Strategy: iterate through records, tracking current time
    # When we see a T record, it adds to pending time before next event
    # When we see an event (R or E), its time = previous_event_time + accumulated_T + (1 if no T between them)
    
    # Actually: "If no T X between two consecutive events, exactly 1 second passed"
    # So between consecutive events, the time difference is either:
    # - 1 second (if no T between them)
    # - X seconds (if T X is between them)
    # Note: there could be multiple T records between events? Probably not, but let's handle it
    # Actually re-reading: "T X indicating that X seconds passed between the previous event and the next event"
    # So T X replaces the default 1 second
    
    # Let's collect events with their timestamps
    events = []  # list of (timestamp, type, friend)
    
    current_time = 0
    pending_time = None  # if T was seen, this is the time to next event
    last_event_time = 0
    first_event = True
    
    for (typ, x) in records:
        if typ == 'T':
            pending_time = x
        else:
            # It's an event R or E
            if first_event:
                current_time = 0
                first_event = False
            else:
                if pending_time is not None:
                    current_time = last_event_time + pending_time
                    pending_time = None
                else:
                    current_time = last_event_time + 1
            last_event_time = current_time
            events.append((current_time, typ, x))
    
    # Now process events to compute response times
    # For each friend, track pending received messages (stack/queue of receive times)
    # Rules: friend never sends new message until response received
    # So for each friend, there's at most one pending message at a time
    
    from collections import defaultdict
    
    pending_receive = {}  # friend -> receive_time (if waiting for response)
    total_response = {}  # friend -> total response time
    has_unanswered = set()  # friends with unanswered messages
    all_friends = set()
    
    for (timestamp, typ, x) in events:
        all_friends.add(x)
        if typ == 'R':
            # Sara received message from x
            pending_receive[x] = timestamp
        else:
            # Sara sent message to x (E)
            if x in pending_receive:
                recv_time = pending_receive.pop(x)
                response_time = timestamp - recv_time
                if x not in total_response:
                    total_response[x] = 0
                total_response[x] += response_time
            # If E without pending R, it's still an event but no response time to add
    
    # Friends with unanswered messages: those still in pending_receive
    unanswered = set(pending_receive.keys())
    
    result = []
    for friend in sorted(all_friends):
        if friend in unanswered:
            result.append(f"{friend} -1")
        else:
            t = total_response.get(friend, 0)
            result.append(f"{friend} {t}")
    
    print('\n'.join(result))

main()